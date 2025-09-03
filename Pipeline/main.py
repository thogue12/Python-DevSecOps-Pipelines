# import the modules
from build_image import clone_repo, build_docker_image
from lint_formatting import lint_and_format
from unit_test import run_pytest, run_trivy_scan, owasp_zap_scan
from push_image import push_image_to_docker_hub
import subprocess
import os

###########################################################################
### ----------------------- Configuration ----------------------- ###
###########################################################################
image_name        = ""
local_path        = ""
dockerfile_path   = "Dockerfile"
python_file       = os.path.join(local_path, "main.py")
requirements_path = os.path.join(local_path, "requirements.txt")
repo              = ""
username          = ""
password          = ""
tag               = ""
###########################################################################
### ----------------------- Main Function ----------------------- ###
###########################################################################
def main():
    try:
        clone_repo(
            repo=repo,
            branch="testing",
            local_path=local_path
        )
        build_docker_image(
            dockerfile_path=dockerfile_path,
            image_name=image_name,
            local_path=local_path
        )
        lint_and_format(
            python_file = python_file,
            requirements_path= requirements_path
        )
        run_pytest(
            local_path=local_path
        ) 
        run_trivy_scan(
            image_name=image_name
        )
        owasp_zap_scan(
            image_name=image_name,
            format="openapi",
            target="http://0.0.0.0:8080",
            allow_issue_writing=False,
            cmd_options= "-a",
            dockerfile_path= dockerfile_path,
            local_path= local_path
        )
        
        push_image_to_docker_hub(
            image_name=image_name,
            tag=tag,
            username=username,
            password=password
        )
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Step failed: {e}")
        exit(1)

if __name__ == "__main__":
    main()