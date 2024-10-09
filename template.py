
import os
from pathlib import Path


file_list = [
    "src/__init__.py",
    "src/detection.py",
    "src/setting.py",
    "model/.gitkeep",
    "logs/detection.logs",
    "app.py",
    "requirements.txt",
    "experiments/experiments.ipynb",
    "test_docs/.gitkeep",
    "Dockerfile",
    ".gitignore",
    ".dockerignore",
    "README.md"
]

for file in file_list:
    file = Path(file)
    folder, filename  = os.path.split(file)
    if folder != "":
        os.makedirs(folder,exist_ok=True)

    if not os.path.exists(folder) or( os.path.getsize(folder) == 0):
        with open(file=file,mode="w") as f:
            pass