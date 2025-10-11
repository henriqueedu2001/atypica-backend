from ingestor import Ingestor
from llm import LLM
from langchain_core.prompts import PromptTemplate
import json
import re

class Blamer:
    def __init__(self):
        self.requirement = None
        self.exam_text = None
        self.prompt_template = None
        self.prompt = None
        self.answer = None
        self.answer_json = None
        return
    
    
    def blame(self):
        llm = LLM(model='gemma3:12b')
        self.answer = llm.ask(self.prompt)
        return
    
    
    def parse_answer(self):
        self.answer_json = AnswerParser.extract_json_from_string(self.answer)
        return
    
    
    def load_requirement(self, req_file_path: str):
        self.requirement = self._load_doc(req_file_path)
        return
    
    
    def load_exam(self, exam_text: str):
        self.exam_text = exam_text
        return
        
    
    def load_prompt_template(self, prompt_template_file_path: str):
        self.prompt_template = self._load_doc(prompt_template_file_path)
        return

    
    def generate_prompt(self):
        prompt_template = PromptTemplate.from_template(self.prompt_template)
        prompt_data = {
            'requirement': self.requirement,
            'exam_text': self.exam_text
        }
        self.prompt = prompt_template.invoke(prompt_data).to_string()
        return
    
    
    def _load_doc(self, file_path: str) -> str:
        with open(file_path, 'r', encoding='utf-8') as file:
            req_text = file.read()
            return req_text
        return


class AnswerParser:
    def extract_json_from_string(text: str) -> dict:
        match = re.search(r'```json\s*(\{.*?\})\s*```', text, re.DOTALL)
        if not match:
            raise ValueError('No JSON blocks found')
        json_str = match.group(1)
        
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            raise ValueError(f'Error while decoding JSON: {e}') from e