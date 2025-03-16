import unittest
from unittest.mock import patch
from agents.transmission_prevention_agent import TransmissionPreventionAgent

class TestTransmissionPreventionAgent(unittest.TestCase):

    def test_init(self):
        agent = TransmissionPreventionAgent()
        self.assertEqual(agent.agent_name, "transmission_prevention")

    @patch('agents.base_agent.BaseAgent.run')
    @patch('agents.base_agent.BaseAgent.get_json')
    def test_agent_workflow(self, mock_get_json, mock_run):
        # Mock the BaseAgent.run() and BaseAgent.get_json() methods
        mock_run.return_value = "Sample response from Claude"
        mock_get_json.return_value = {"key": "value"}

        agent = TransmissionPreventionAgent()
        agent.run()
        output = agent.get_json()

        self.assertEqual(output, {"key": "value"})
        mock_run.assert_called_once()
        mock_get_json.assert_called_once()

if __name__ == "__main__":
    unittest.main()
