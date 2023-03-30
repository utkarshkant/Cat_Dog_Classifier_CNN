# file containing all utility functions

# imports
import os
from box.exceptions import BoxValueError    # exception handler
import yaml
from CAT_DOG_CLASSIFIER_CNN import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    """
    Reads the yaml file and returns a ConfigBox.

    Args:
        path (str): Path to the input yaml file

    Raises:
        ValueError: if yaml file is empty
        e: empty yaml file

    Returns:
        ConfigBox: ConfigBox object
    """

    try:
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path: list, verbose=True):
    """
    Creates a list of directories
    
    Args:
        path (list): list of paths to directories
        ignore_log (bool, optional): ignore if multiple directories needs to be created. Defaults to True
    """

    for path in path:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves JSON data

    Args:
        path (Path): path to JSON file
        data (dict): data to be saved in JSON file
    """

    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads data from JSON files

    Args:
        path (Path): Path to JSON file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """

    with open(path) as f:
        content = json.load(f)

    logger.info(f"JSON file loaded successfully from: {path}")

    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to the binary file
    """

    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved successfully at {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    load binary data

    Args:
        path (Path): path to the binary file

    Returns:
        Any: object stored in the file
    """

    data = joblib.load(path)
    logger.info(f"binary file loaded successfully from {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size of file in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """

    size_in_kb = round(os.path.getsize(path) / 1024)
    
    return f"~ {size_in_kb} KB"


