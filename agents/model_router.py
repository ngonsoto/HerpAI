import os  # For accessing environment variables
import requests  # To make HTTP requests to Claude's API
import json
import hashlib
from src.config_loader import AppConfig, AgentConfig  # Adjust the import path based on your actual structure

class ModelRouter:
    """
    This class selects the appropriate language model based on the configuration.
    """

    def __init__(self, agent_name="default"):
        """
        Initialize the ModelRouter with a specific agent name, loading settings from AppConfig.
        """
        self.agent_name = agent_name
        self.config = AppConfig.load()

        agent_config = self.config.agents.get(agent_name, {})
        self.provider = agent_config.model_provider or self.config.default_model_provider
        self.model = agent_config.model or "claude-3-7-sonnet-latest"

    def query(self, prompt):
        """
        This is the main method to send the prompt to the selected model.
        It checks which provider is set and calls the respective internal method.
        """
        if self.provider == "claude":
            return self._query_claude(prompt)
        elif self.provider == "openai":
            return self._query_openai(prompt)
        else:
            return f"[ERROR] Unsupported model provider: {self.provider}"

    def _query_claude(self, prompt):
        """
        Send a request to Claude (Anthropic) API with conditional caching capability.
        """

        # Load cache setting from config
        agent_config = self.config.agents.get(self.agent_name, AgentConfig(model_provider=self.config.default_model_provider, model="default-model"))
        should_cache = agent_config.cache

        prompt_hash = hashlib.sha256(prompt.encode()).hexdigest()
        cache_dir = os.path.join("cache", self.agent_name)
        os.makedirs(cache_dir, exist_ok=True)
        cache_filepath = os.path.join(cache_dir, f"{prompt_hash}.json")

        # If caching enabled, check for existing cached response
        if should_cache and os.path.exists(cache_filepath):
            with open(cache_filepath, "r") as f:
                cached_response = json.load(f)
                return cached_response["response"]

        headers = {
            "x-api-key": os.getenv("SONNET_API_KEY"),
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }

        payload = {
            "model": self.model,
            "max_tokens": self.config.agents.get(self.agent_name, AgentConfig(model_provider=self.config.default_model_provider, model="default-model")).max_tokens,
            "messages": [{"role": "user", "content": prompt}]
        }

        response = requests.post("https://api.anthropic.com/v1/messages", headers=headers, json=payload)

        if response.status_code == 200:
            response_content = response.json()["content"][0]["text"]

            # Cache the response only if enabled in config
            if should_cache:
                with open(cache_filepath, "w") as f:
                    json.dump({"response": response_content}, f, indent=2)

            return response_content

        return f"[Claude API Error {response.status_code}] {response.text}"

    def _query_openai(self, prompt):
        """
        OpenAI query is not yet implemented.
        """
        raise NotImplementedError("OpenAI query is not implemented yet.")

    import json
import re

def extract_json_from_markdown(response: str) -> dict:
    # Match content between triple backticks labeled json
    match = re.search(r"```json\s*(\{.*?\})\s*```", response, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            print("⚠️ Could not decode JSON block.")
            return {}
    else:
        print("⚠️ No JSON block found in response.")
        return {}