from exam import Exam, Question
from exam_parser import ExamParser
from requirement import Requirement
from blamer import Blamer
from file_manager import FileManager
from pathlib import Path
from typing import *

class Pipeline:
    def __init__(self):
        self.exam: Exam = None
        self.requirements: List[Requirement] = []
        self.blamer: Blamer = None
        self.blamings = []
        return
    
    
    def load_exam(self, file_path: Path):
        self.exam = Exam(file_path=file_path)
        return
    
    
    def extract_questions(self, model: str):
        exam_parser = ExamParser(prompt_template_path='knowledge/prompts/exam_parsing.md', model=model)
        parsed_exam = exam_parser.parse(exam_text=self.exam)
        questions = parsed_exam.get('questions')
        self.exam.set_questions(questions)
        return
    
    
    def load_requirement(self, file_path: Path, on_single_question: bool):
        requirement = Requirement(file_path=file_path, on_single_question=on_single_question)
        self.requirements.append(requirement)
        return
    
    
    def load_blamer(self, model: str):
        self.blamer = Blamer(prompt_template_path='knowledge/prompts/requirement_analysis.md', model=model)
        return
    
    
    def blame(self):
        for requirement in self.requirements:
            if requirement.on_single_question:
                for question in self.exam.questions:
                    self.blame_question(question=question, requirement=requirement)
            else:
                self.blame_exam(requirement=requirement)
        return
    
    
    def blame_exam(self, requirement: Union[str, Requirement]):
        exam_text = self.exam.raw_text
        blaming = self.blamer.blame(exam_text=exam_text, requirement=requirement)
        print(blaming)
        self.blamings.append(blaming)
        return
    
    
    def blame_question(self, question: Question, requirement: Union[str, Requirement]):
        exam_text = question.question_text
        blaming = self.blamer.blame(exam_text=exam_text, requirement=requirement)
        print(blaming)
        self.blamings.append(blaming)
        return
    