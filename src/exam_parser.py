from llm import LLM
from file_manager import FileManager
from exam import Exam
from langchain_core.prompts import PromptTemplate
from pathlib import Path

class ExamParser:
    def __init__(self, prompt_template_path: Path, model: str):
        self.prompt_template_path: Path = prompt_template_path
        self.model: str = model
        self.prompt_template: str = None
        self.prompt: str = None
        self.load_prompt_template()
        return
    
    
    def load_prompt_template(self):
        self.prompt_template = FileManager.load_text(self.prompt_template_path)
        return
    
    
    def compile_prompt(self, exam_text: str):
        prompt_template = PromptTemplate.from_template(self.prompt_template)
        prompt_data = { 'exam_text': exam_text }
        prompt = prompt_template.invoke(prompt_data).to_string()
        self.prompt = prompt
        print(prompt)
        return
    
    
    def parse(self, exam_text: str):
        self.compile_prompt(exam_text=exam_text)
        llm = LLM(model=self.model)
        answer = llm.ask(self.prompt)
        print(answer)
        answer = LLM.extract_json_from_answer(answer)
        return answer


exam = Exam(file_path='files/PROVA_FIC_05.pdf')
exam_parser = ExamParser(prompt_template_path='knowledge/prompts/exam_parsing.md', model='gemma3:12b')
parsed_exam = exam_parser.parse(exam_text=exam.raw_text)
FileManager.save_json('artifacts/fff.json', parsed_exam)