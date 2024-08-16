import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "text-classification"
required_files_paths = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'setup.py',
    'Dockerfile',
    'requirements.txt',
    'research/trails.ipynb'
]

for filepath in required_files_paths:
    filepath = Path(filepath)
    file_dir, filename = os.path.split(filepath)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir}, for file: {filename}. Skipping if already exists")

    if not (os.path.exists(filepath)):
        with open(filepath, 'w') as file:
            pass
            logging.info(f"Creating empty file: {filename}")
    
    else:
        logging.info(f"{filename} already exists")

