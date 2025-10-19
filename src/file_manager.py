import os
import json
from pathlib import Path
from typing import *

class FileManager:
    def cast_path(path: Union[str, Path]):
        if type(path) is not Path: return Path(path)
        return path
    
    
    def load_text(file_path: Path) -> str:
        casted_file_path = FileManager.cast_path(file_path)
        with open(casted_file_path, 'r', encoding='utf-8') as file:
            req_text = file.read()
            return req_text
        return
    
    
    def save_json(file_path: Path, json_content: str):
        casted_file_path = FileManager.cast_path(file_path)
        with open(casted_file_path, 'w', encoding='utf-8') as file:
            json.dump(json_content, file, ensure_ascii=False, indent=4)
        return
    
    
    def load_json(file_path: Path) -> json:
        casted_file_path = FileManager.cast_path(file_path)
        with open(casted_file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
        return