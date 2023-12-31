"""
    The utility file utils.py is compose of functions that are used frequently 
    and does not adhere to any specific components of the project.
"""

import os
from box.exceptions import BoxValueError
import yaml
from text_summarizer.logging.logger import logging
from ensure import ensure_annotations
from box import ConfigBox # To access values like d.key insted of d["key"]
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a yaml file and return a ConfigBox object.

    Parameters:
    -----------
    path_to_yaml: Path

    Raises:   
    --------
    BoxValueError: If the yaml file does not exist.
    e: If the yaml file is empty.

    Returns:   
    --------
    ConfigBox: ConfigBox object
    """
    try:
        with open(path_to_yaml, "r") as file_object:
            config = yaml.safe_load(file_object)
            logging.info(f"Read yaml file: {path_to_yaml}")
            return ConfigBox(config)
    except BoxValueError:
        raise ValueError(f"Yaml file is empty: {path_to_yaml}")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool=True):
    """
    Create directory from the list of directories.
    
    Parameters:
    -----------
    path_to_directories: list of path of directories
    verbose: bool
    """

    for directory in path_to_directories:
        directory = Path(directory)
        os.makedirs(directory, exist_ok=True)
        if verbose:
            logging.info(f"Created directory at: {directory}")


@ensure_annotations
def get_size(path_to_file: Path) -> str:
    """
    Get the size of a file.

    Parameters:
    -----------
    path_to_file: Path of the file.

    Returns:   
    --------
    str: Size of the file in Kilo-bytes.
    """
    size_in_kb = round(os.path.getsize(path_to_file)/1024)
    return f"~ {size_in_kb} KB"

