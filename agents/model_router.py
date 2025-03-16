# model_router.py

import os  # For accessing environment variables
import requests  # To make HTTP requests to Claude's API
# You can also import openai here if GPT-4 will be supported

class ModelRouter:
    """
    This class is responsible for selecting the appropriate language model (Claude, GPT, etc.)
    and routing the prompt to the correct API.
    """

    def __init__(self, agent_name="default"):
        """
        Initialize the ModelRouter with a specific agent name.
        It determines which model provider (claude/openai) and model to use based on environment variables.
        """
        self.agent_name = agent_name
        # Determine the model provider for this agent (e.g., 'claude' or 'openai')
        self.provider = os.getenv(f"{agent_name.upper()}_MODEL_PROVIDER", os.getenv("DEFAULT_MODEL_PROVIDER", "claude"))
        # Get the model name/version to use (e.g., 'claude-sonnet-3.7' or 'gpt-4')
        self.model = os.getenv(f"{agent_name.upper()}_MODEL", "claude-sonnet-3.7")

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
        Send a request to Claude (Anthropic) API with the user prompt.
        Returns the response content or an error message.
        """
        # Set the headers required by Claude API
        headers = {
            "x-api-key": os.getenv("SONNET_API_KEY"),  # Your Claude API key
            "anthropic-version": "2023-06-01",         # API version
            "content-type": "application/json"
        }

        # Set the body (payload) of the API request
        payload = {
            "model": self.model,
            "max_tokens": 1000,  # Maximum number of tokens in the response
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        # Send POST request to Claude API
        response = requests.post("https://api.anthropic.com/v1/messages", json=payload, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            return response.json().get("content", "[No Claude response content]")
        return f"[Claude API Error {response.status_code}] {response.text}"

    def _query_openai(self, prompt):
        """
        Send a request to OpenAI's API with the user prompt.
        Returns the response content or an error message.
        """
        import openai  # Import OpenAI SDK
        openai.api_key = os.getenv("OPENAI_API_KEY")  # Set your OpenAI key

        # Send request to OpenAI's chat model
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful biomedical research assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5  # Controls randomness in the response
        )

        return response["choices"][0]["message"]["content"]