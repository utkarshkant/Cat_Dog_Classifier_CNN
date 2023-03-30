# imports
import os
from pathlib import Path
import logging

# log template files and folders creation
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# directory name
project_name = 'CAT_DOG_CLASSIFIER_CNN'

# directory and files to be created
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "research/trials.ipynb",
    "setup.py"
]

# file and directory creations
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # create directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass        # create an empty file
            logging.info(f"Creating directory: {filepath}")
    else:
        logging.info(f"{filepath} file already exists")