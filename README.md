# DevSecOps-Python-Pipeline

A modular, reusable Python-based DevSecOps pipeline for automating the build, test, security scan, and deployment of FastAPI applications in Docker. This project provides an all-in-one solution for CI/CD pipelines, container security, and code quality enforcement using Python functions.

---

🌐 **Project Goals**

- Enable engineers to automate DevSecOps pipelines through **modular Python functions**.  
- Provide reusable patterns for CI/CD, unit testing, and container security scanning.  
- Enforce security and compliance with integrated tools like **Trivy** and **OWASP ZAP**.  
- Support easy extension: new pipeline steps can be added by creating a new Python file with a function and referencing it in `main.py`.

---

🧱 **Pipeline Modules**

🔁 **Core Pipeline Jobs**

- **Clone Repo**  
  - Clones a target FastAPI GitHub repository  
  - Module file: `clone_repo.py`  

- **Build Docker Image**  
  - Builds Docker image from the repository’s Dockerfile  
  - Module file: `build_docker.py`  

- **Lint & Format**  
  - Runs `pylint` for static analysis  
  - Runs `black` for code formatting  
  - Module file: `lint_format.py`  

- **Unit Testing**  
  - Runs `pytest` for automated unit tests  
  - Module file: `unit_test.py`  

- **Trivy Scan (Dockerized)**  
  - Runs a containerized **Trivy** image to scan Docker images for vulnerabilities  
  - No local installation required beyond Docker  
  - Module file: `trivy_scan.py`  

- **OWASP ZAP Scan (Dockerized)**  
  - Runs a containerized **OWASP ZAP** image to perform automated web application security tests  
  - No local installation required beyond Docker  
  - Module file: `owasp_zap.py`  

- **Push to Docker Hub**  
  - Pushes the Docker image to Docker Hub  
  - Module file: `push_docker.py`  

> Each module is independent and can be extended. For example, to add additional tests or steps in `unit_test.py`, simply add new functions and call them in `main.py`.

---

⚙️ **Setup**

1. **Clone the repository**  
```bash
git clone <repo-url>
cd <repo-folder>

    Create and activate a virtual environment

python -m venv venv
# Activate
source venv/bin/activate   # Linux/macOS
# or
venv\Scripts\activate      # Windows


Install dependencies:


    subprocess and os are standard Python libraries and require no installation.

    PyGithub
    
    gitpython

    docker

    Docker setup

    Ensure Docker is installed and running.

    No local installation of Trivy or OWASP ZAP is required — they are pulled and run as Docker containers.

    Authenticate with Docker Hub

    docker login

🚀 Usage

Run the pipeline:

python main.py

The pipeline executes all stages in order.
New functions or stages can be added by creating a Python file with the function and importing it in main.py.

🔧 Extending the Pipeline

    Create a new Python file with the desired function.

    Import the function into main.py.

    Call the function at the appropriate point in the pipeline.

This design allows teams to easily extend or modify the DevSecOps workflow without touching other parts of the codebase.

💡 CI/CD & DevSecOps Tooling

    Code quality enforcement: ✅ pylint, ✅ black

    Unit testing: ✅ pytest

    Container vulnerability scanning: ✅ Trivy (via Docker container)

    Web application security testing: ✅ OWASP ZAP (via Docker container)