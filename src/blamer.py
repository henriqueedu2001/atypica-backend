from ingestor import Ingestor
from llm import LLM
from langchain_core.prompts import PromptTemplate
from requirement import Requirement
from file_manager import FileManager
import json
import re
from pathlib import Path
from typing import *

class Blamer:
    def __init__(self, prompt_template_path: Path, model: str):
        self.prompt_template_path: Path = prompt_template_path
        self.model: str = model
        self.prompt_template: str = None
        self.prompt: str = None
        self.load_prompt_template()
        return
    
    
    def blame(self, exam_text: str, requirement: Union[str, Requirement]):
        self.compile_prompt(exam_text=exam_text, requirement=requirement)
        llm = LLM(model=self.model)
        answer = llm.ask(self.prompt)
        print(answer)
        answer = LLM.extract_json_from_answer(answer)
        return answer


    def load_prompt_template(self):
        self.prompt_template = FileManager.load_text(self.prompt_template_path)
        return
    
    
    def compile_prompt(self, exam_text: str, requirement: Union[str, Requirement]):
        prompt_template = PromptTemplate.from_template(self.prompt_template)
        prompt_data = {
            'requirement': requirement,
            'exam_text': exam_text
        }
        prompt = prompt_template.invoke(prompt_data).to_string()
        self.prompt = prompt
        return


exam_sample = '6) Karl Marx dizia que a história humana pode ser entendida como uma luta entre classes ou grupos, ou setores, ou formas de produção. Isso significa:\na) Conflitos de classes.\nb) Filosofia da linguagem.\nc) Expansão marítima.\nd) Desenvolvimento da metafísica.'
requirement = Requirement(file_path='knowledge/requirements/RF02.md')
blamer = Blamer(prompt_template_path='knowledge/prompts/requirement_analysis.md', model='gemma3:4b')
blamer.blame(exam_text=exam_sample, requirement=requirement)