import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep", # For GitHub workflows
    f"src/{project_name}/__init__.py", # For Python package initialization (we can use it directly like model.etc)
    f"src/{project_name}/components/__init__.py", # For components package
    f"src/{project_name}/utils/__init__.py", # For utils package
    f"src/{project_name}/config/__init__.py", # For config package
    f"src/{project_name}/config/configuration.py" # For configuration file
    "config/config.yaml", # For configuration file
    "dvc.yaml", # For DVC configuration
    "params.yaml", # For parameters
    "requirements.txt", # For Python dependencies
    "setup.py", # For package setup
    "research/trials.ipynb" # For Jupyter notebook
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")
    
    if not os.path.exists(filepath) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating file: {filepath}")
    
    else:
        logging.info(f"File already exists: {filepath}, skipping creation.") 