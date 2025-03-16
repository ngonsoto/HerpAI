# virology_agent.py

import os
import requests

class VirologyAgent:
    def __init__(self):
        self.name = "Virology Agent"
        self.api_key = os.getenv("SONNET_API_KEY")
        self.model = os.getenv("SONNET_MODEL", "claude-sonnet-3.7")
        self.api_url = "https://api.anthropic.com/v1/messages"

    def analyze_latency_and_reactivation(self, virus_type="HSV-2"):
        prompt = f"""
        As a molecular virology expert, identify the key genes involved in latency and reactivation of {virus_type}.
        Also list typical reactivation triggers based on known studies.
        Format response as:
        - Latency Genes: [...]
        - Replication Genes: [...]
        - Reactivation Triggers: [...]
        """

        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }

        payload = {
            "model": self.model,
            "max_tokens": 1000,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(self.api_url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json().get("content", "No response content received.")
        else:
            return f"API Error {response.status_code}: {response.text}"