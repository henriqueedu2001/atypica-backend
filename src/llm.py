import json
import re
from pathlib import Path
import ollama

class LLM:
    def __init__(self, model: str):
        self.model = model
        return

    def ask(self, query: str) -> str:
        answer = ollama.generate(model=self.model, prompt=query)
        answer = answer.get('response')
        return answer
    
    
    def load_prompt(prompt_template_path: Path):
        return
    
    
    def extract_json_from_answer(text: str) -> dict:
        match = re.search(r'```json\s*(\{.*?\})\s*```', text, re.DOTALL)
        if not match:
            raise ValueError('No JSON blocks found')
        json_str = match.group(1)
        
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            raise ValueError(f'Error while decoding JSON: {e}') from e