# import the necessary libraries
from github import Github, Auth
import subprocess
import docker
from git import Repo
import os

###########################################################################
### --------- Function to Checkout/ Clone a GitHub repository --------- ###
###########################################################################
def clone_repo(repo: str, branch: str, local_path: str):
    try:
        print(f"Cloning repository {repo} on branch {branch}...")
        Repo.clone_from(repo, local_path, branch=branch)
        print("Repository cloned successfully.")
    except Exception as e:
        print(f"Error cloning repository: {e}")
        return None
    
###########################################################################
###### ------------- Function to Build a Docker image ---------------######
###########################################################################
def build_docker_image(dockerfile_path: str,image_name: str, local_path: str ):
    try:
        # Build the Docker image
        print(f"Building Docker image {image_name} from {dockerfile_path}...")
        client = docker.from_env()
        image, build_logs = client.images.build(
            path= local_path, dockerfile=dockerfile_path, tag=image_name
        )
        for chunk in build_logs:
            if 'stream' in chunk:
                print(chunk['stream'].strip())
        print(f"Docker image {image_name} built successfully.")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return None
    except NotADirectoryError as e:
        print(f"Not a directory: {e}")
        return None
    except PermissionError as e:
        print(f"Permission denied: {e}")


