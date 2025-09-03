# import the necessary libraries
from github import Github, Auth
import subprocess
import docker
from git import Repo
import os

# How do you create a function for Pylint and black formatting, if they are command line tools?
# How do I create a funciton to run Pylint and Black on a Python file?
###########################################################################
# Create linting and formatting function
###########################################################################
def lint_and_format(python_file: str, requirements_path: str ):
    try:
        # Install dependencies from requirements.txt
        print("Installing dependencies from requirements.txt...")
        subprocess.run(['pip', 'install', '-r', requirements_path], check=True)
        
        # Run Pylint
        print(f"Running Pylint on {python_file}...")
        pylint_result = subprocess.run(['pylint', python_file], capture_output=True, text=True)
        print(pylint_result.stdout)
        if pylint_result.returncode != 0:
            print(f"Pylint found issues in {python_file}.")
        
        # Run Black
        print(f"Formatting {python_file} with Black...")
        black_result = subprocess.run(['black', python_file], capture_output=True, text=True)
        print(black_result.stdout)
        if black_result.returncode == 0:
            print(f"{python_file} formatted successfully.")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return None
    except NotADirectoryError as e:
        print(f"Not a directory: {e}")
        return None
    except PermissionError as e:
        print(f"Permission denied: {e}")


