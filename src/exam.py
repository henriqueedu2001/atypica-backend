from file_manager import FileManager
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from typing import *

class Question:
    def __init__(self, question_number: int, question_text: str):
        self.question_number = question_number
        self.question_text = question_text
        return
    
    
    def __str__(self):
        return self.question_text
    

class Exam:
    def __init__(
        self,
        header: str = None,
        questions: List[Question] = [],
        footer: str = None,
        raw_text: str = None,
        file_path: Union[str, Path] = None,
        load_on_creation: bool = True
    ):
        self.header: str = header
        self.questions: List[Question] = questions
        self.footer: str = footer
        # loading from pdf
        self.file_path: Union[str, Path] = file_path
        self.raw_text: str = raw_text
        self.pdf_loader: PyPDFLoader = None
        if load_on_creation: self.load_exam()
        return
    
    
    def load_exam(self):
        loader = PyPDFLoader(FileManager.cast_path(self.file_path))
        documents = loader.load()
        self.raw_text = ''.join([page.page_content for page in documents])
        self.pdf_loader = loader
        return
    
    
    def set_questions(self, questions: List[str]):
        for index, question in enumerate(questions):
            self.questions.append(Question(question_number=index, question_text=question))
        return
    
    
    def __str__(self):
        return self.raw_text