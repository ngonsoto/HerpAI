import unittest
from unittest.mock import mock_open, patch
from src.config_loader import AppConfig, AgentConfig

class TestConfigLoader(unittest.TestCase):
    SAMPLE_YAML = """
    app:
      default_model_provider: claude
      agents:
        virology:
          model_provider: claude
          model: claude-3-7-sonnet-latest
          prompt_version: v1
          cache: true
          max_tokens: 2500
          temperature: 0.4
    """

    def test_load_config(self):
        with patch("builtins.open", mock_open(read_data=self.SAMPLE_YAML)):
            config = AppConfig.load("config.yaml")

        self.assertIsInstance(config, AppConfig)
        self.assertEqual(config.default_model_provider, "claude")
        self.assertIn("virology", config.agents)
        
        virology_cfg = config.agents["virology"]
        self.assertEqual(virology_cfg.model_provider, "claude")
        self.assertEqual(virology_cfg.model, "claude-3-7-sonnet-latest")
        self.assertEqual(virology_cfg.prompt_version, "v1")
        self.assertTrue(virology_cfg.cache)
        self.assertEqual(virology_cfg.max_tokens, 2500)
        self.assertEqual(virology_cfg.temperature, 0.4)

    def test_cache_enabled(self):
        config = AppConfig.load("config.yaml")
        virology_config = config.agents["virology"]
        print(f"virology_config.cache: {virology_config.cache}")
        self.assertTrue(virology_config.cache)

    def test_agent_config(self):
        agent_config = AgentConfig(
            model_provider="claude",
            model="claude-3-7-sonnet-latest",
            prompt_version="v1",
            cache=True,
            max_tokens=2500,
            temperature=0.4
        )

        self.assertEqual(agent_config.model_provider, "claude")
        self.assertEqual(agent_config.model, "claude-3-7-sonnet-latest")
        self.assertEqual(agent_config.prompt_version, "v1")
        self.assertTrue(agent_config.cache)
        self.assertEqual(agent_config.max_tokens, 2500)
        self.assertEqual(agent_config.temperature, 0.4)

if __name__ == "__main__":
    unittest.main()
