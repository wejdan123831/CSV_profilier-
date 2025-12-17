# only read csv file 

from pathlib import Path
from csv import DictReader
from typing import List, Dict, Any , Tuple 
import io 

def read_csv(file_path: Path) -> Tuple[List[Dict], List[str]]:     
    
    
    file_path = Path(file_path) 
    
    if not file_path.exists():
        raise FileNotFoundError(f" the fil is not at the path : {file_path}")

    data = []
    headers = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = DictReader(file)
        headers = reader.fieldnames or []
        for row in reader:
            data.append(row)
            
    return data , headers 