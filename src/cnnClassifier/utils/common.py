import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from pydantic import validate_arguments
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@validate_arguments

def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    Args:
        path_to_yaml (Path): Path to the YAML file.
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:  
        raise e     
    
@validate_arguments
def create_directories(path_to_directories:list,verbose = True): 
    """
    Creates list of direcotries 
    Args:
        path_to_directories (list): List of paths to directories to be created.
        verbose (bool): If True, logs the creation of directories.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")
        

@validate_arguments
def save_json(path: Path, data: dict):
    """
    Saves a dictionary to a JSON file.
    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved in the JSON file.
    """ 
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    logger.info(f"Saved JSON file at: {path}")

@validate_arguments
def get_size(path: Path) -> str:
    """ get size of file or directory
    Args:
        path (Path): Path to the file or directory.
    Returns:   
        str: size in KB
    """ 
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"

