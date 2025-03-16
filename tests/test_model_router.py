import unittest
from unittest.mock import patch, Mock
from agents.model_router import ModelRouter
from src.config_loader import AppConfig, AgentConfig

class TestModelRouter(unittest.TestCase):

    @patch('agents.model_router.requests.post')
    @patch('src.config_loader.AppConfig.load')
    def test_query_claude_success(self, mock_config_load, mock_post):
        # Disable caching explicitly for testing purposes
        mock_config_load.return_value = AppConfig(
            default_model_provider="claude",
            agents={
                "virology": AgentConfig(
                    model_provider="claude",
                    model="claude-3-7-sonnet-latest",
                    prompt_version="v1",
                    cache=False,  # disable caching explicitly here
                    max_tokens=2500,
                    temperature=0.4
                )
            }
        )

        # Mock successful Claude API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "content": [{"text": "Test response from Claude"}]
        }
        mock_post.return_value = mock_response

        router = ModelRouter(agent_name="virology")
        result = router.query("Test prompt")

        self.assertEqual(result, "Test response from Claude")
        mock_post.assert_called_once()

    def test_openai_not_implemented(self):
        router = ModelRouter(agent_name="drug_design")
        router.provider = "openai"
        with self.assertRaises(NotImplementedError):
            router.query("test prompt")

if __name__ == '__main__':
    unittest.main()