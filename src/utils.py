# src/utils.py
import json
import re

def extract_json_from_markdown(response: str) -> dict:
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