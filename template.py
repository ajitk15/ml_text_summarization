import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s : %(message)s]')

project_name = "text_summarization"

list_of_files = [
    ".github.com/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", 
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__main__.py",
    f"src/{project_name}/constants/__main__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]

for file in list_of_files:
    file = Path(file)
    filedir, filename = os.path.split(file)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info("Creating directory: {}".format(filedir))

    if (not os.path.exists(file)) or (os.path.getsize(file) == 0):
        logging.info("Creating file: {}".format(file))
        with open(file, "w") as f:
            pass
    else:
        logging.info("File already exists: {}".format(file))