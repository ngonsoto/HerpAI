from agents.model_router import ModelRouter
import os
from src.config_loader import AgentConfig, AppConfig, Config

class VirologyAgent:
    """
    VirologyAgent is responsible for analyzing HSV latency and reactivation patterns
    using an AI language model routed via ModelRouter.
    """

    def __init__(self):
        cfg = AppConfig.load()
        self.agent_cfg: AgentConfig = cfg.agents["virology"]
        self.llm = ModelRouter(agent_name="virology", config=self.agent_cfg)
        self.prompt_version = self.agent_config.prompt_version

    def analyze_latency_and_reactivation(self, virus_type="HSV-2"):
        """
        Analyze HSV latency/reactivation genes and triggers using an LLM.

        Args:
            virus_type (str): 'HSV-1' or 'HSV-2'

        Returns:
            str: Model-generated analysis in structured format.
        """
        if virus_type not in ["HSV-1", "HSV-2"]:
            raise ValueError("Invalid virus_type. Must be 'HSV-1' or 'HSV-2'.")

        prompt = self._build_prompt(virus_type)
        return self.llm.query(prompt)

    def _build_prompt(self, virus_type):
        """
        Loads the LLM prompt from an external markdown (.md) file, replaces {{virus_type}} with the actual value,
        and returns the formatted prompt string based on the selected version.

        Args:
            virus_type (str): The HSV type to analyze.

        Returns:
            str: Prompt string to send to the LLM.
        """
        prompt_path = os.path.join("prompts", f"virology_prompt_{self.prompt_version}.md")

        # Read the prompt from the markdown file
        with open(prompt_path, "r") as file:
            prompt = file.read()

        # Replace placeholder with actual virus type
        prompt = prompt.replace("{{virus_type}}", virus_type)

        return prompt