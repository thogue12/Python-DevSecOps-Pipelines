import subprocess
import os
import docker

###########################################################################
### --------- Function to Push Image to Docker Hub --------- ###
###########################################################################
def push_image_to_docker_hub(
    image_name:str, tag: str, 
    username: str, password: str
    ):
    
    try:
        print("logging into Docker Hub...")
        subprocess.run(
            ['docker','login', '-u', username, '-p', password,],
            check=True        
            )
        print("Login successful.")
        
        print("tagging image...")
        subprocess.run(['docker','tag',  image_name, f"{username}/{image_name.split(':')[0]}:{tag}"], check=True)
        print(f"Pushing image {image_name}:{tag} to Docker Hub...")
        subprocess.run(['docker', 'push', f"{username}/{image_name.split(':')[0]}:{tag}"],check=True)
        print(f"Image {image_name}:{tag} pushed successfully.")
        
    except subprocess.CalledProcessError as e:
        print(f"Error pushing image to Docker Hub: {e}")
        return None
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return None
    except NotADirectoryError as e:
        print(f"Not a directory: {e}")
        return None
    except PermissionError as e:
        print(f"Permission denied: {e}")
        return None
    except docker.errors.APIError as e:
        print(f"Error logging into Docker Hub: {e}")
    except docker.errors.DockerException as e:
        print(f"Error with Docker client: {e}")
        return None



###########################################################################
### --------- Function to Push Image to GHCR --------- ###
###########################################################################
