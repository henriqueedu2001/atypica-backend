from file_manager import FileManager
from pathlib import Path
from typing import *

class Example:
    def __init__(self, text: str, positive_example: bool, analysis: str):
        text: str = text
        positive_example: bool = positive_example
        analysis: str = analysis
        return
    

class Requirement:
    def __init__(self,
            id: str = None,
            name: str = None,
            type: Literal['functional', 'non functional'] = None,
            description: str = None,
            criteria: str = None,
            examples: List[Example] = None,
            file_path: Path = None,
            load_on_creation: bool = True
        ):
        # requirement definition
        self.id: str = id
        self.name: str = name
        self.type: Literal['functional', 'non functional'] = type
        description: str = description
        self.criteria: str = criteria
        examples: List[Example] = examples
        # loading from markdown file
        self.file_path: Union[str, Path] = file_path
        self.raw_text: str = 'empty requirement'
        self.loaded_req: bool = False
        if load_on_creation: self.load_requirement()
        return
    
    
    def load_requirement(self):
        self.raw_text = FileManager.load_text(self.file_path)
        self.loaded_req: bool = True
        return
    
    
    def __str__(self):
        return self.raw_text
