import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, 
                    format='[%(asctime)s]: %(message)s')

project = 'text_summarizer'

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project}/__init__.py',
    f'src/{project}/components/__init__.py',
    f'src/{project}/utils/__init__.py',
    f'src/{project}/utils/common.py',
    f'src/{project}/logging/__init__.py',
    f'src/{project}/config/__init__.py',
    f'src/{project}/config/configuration.py',
    f'src/{project}/pipeline/__init__.py',
    f'src/{project}/entity/__init__.py',
    f'src/{project}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)
    
    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f'Created directory: {file_dir} for file: {file_name}')

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        logging.info(f'Creating file: {file_path}')
        with open(file_path, 'w') as f:
            pass
            logging.info(f'Created empty file: {file_path}')
    else:
        logging.info(f'File already exists: {file_name}')
