import os
from pathlib import Path


project_name = "job_recommender"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/helper_functions.py",
    f"{project_name}/job_api.py",
    f"{project_name}/logger/logger.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/exception/exception_handler.py",  
    f"{project_name}/exception/__init__.py",
    "app.py",
    "mcp_server.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    ".env",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")
