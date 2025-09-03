import subprocess
import os
import docker

###########################################################################
### --------- Function to Run Pytest --------- ###
###########################################################################

def run_pytest(local_path:str):
    try:
        print(f"Running Pytest in {local_path}...")
        subprocess.run([ 'pytest', local_path], check=True)
        print("Pytest completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Pytest: {e}")
        return None
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return None
    except NotADirectoryError as e:
        print(f"Not a directory: {e}")
        return None
    except PermissionError as e:
        print(f"Permission denied: {e}")
        
###########################################################################      
### --------- Function for Trivy Image Scan --------- ###
###########################################################################

def run_trivy_scan(image_name: str):
    # install trivy as a docker container
    try:
        print(f"Pulling Trivy Image...")
        subprocess.run(['docker', 'pull', 'aquasec/trivy:latest'], check=True)
        print("Trivy pulled successfully.")  

        subprocess.run(['docker', 'run', '--rm', 'aquasec/trivy:latest'], check=True )
        print(f"creating Docker container for Trivy...")


        subprocess.run(['trivy','image', image_name], check=True)

        print(f"Trivy Scan on: {image_name} complete.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Trivy scan: {e}")
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


###########################################################################
### --------- Function for Owasp ZAP --------- ###
###########################################################################


def owasp_zap_scan(
    image_name: str, format: str, target: str,local_path: str,
    cmd_options: str, allow_issue_writing: bool, dockerfile_path: str,):
    
    try:
        
        print (f"Pulling OWASP ZAP Docker image...")
        subprocess.run(['docker', 'pull', 'zaproxy/zap-stable'], check=True)
        print("OWASP ZAP pulled successfully.")
        print(f"Creating OWASP ZAP container for {image_name}...")
        subprocess.run(['docker', 'run', '--rm', '-v', f"{os.getcwd()}:/zap/wrk/:rw", 'zaproxy/zap-stable'], check=True)
        print("OWASP ZAP container created successfully.")
    
        # Build docker container for  Fast API application
        print("building Python Fast API application container...")
        subprocess.run(['docker', 'build', '-t', image_name,local_path], check=True)
        print(f"Python Fast API application container {image_name} built successfully.")
        
        print(f"Running OWASP ZAP scan on {image_name}...")
        cmd = [
            "docker", "run", "--rm",
            "-v", f"{os.getcwd()}:/zap/wrk/:rw",
            "zaproxy/zap-stable", "zap.sh",
            "-cmd", "-autorun", "/zap/wrk/zap.yaml",
            "-f", format,
            "-r", "zap_report.html",
            "-I" if not allow_issue_writing else "",
            "-z", cmd_options,
            target
        ]
        
        print(f"[ZAP Scan] Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            print("ZAP stdout:", result.stdout)
            print("ZAP stderr:", result.stderr)
        
        print("OWASP ZAP scan completed successfully.")
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "report_path": "./zap_report.html"
        }
    except subprocess.CalledProcessError as e:
        print(f"Error running OWASP ZAP scan: {e}")
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
    except RuntimeError as e:
            print(f"ZAP scan failed:\n{e}")
    

