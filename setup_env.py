import os
import subprocess
import sys

def create_venv():
    subprocess.call([sys.executable, "-m", "venv", "venv"])
    print("Virtual environment created.")

def install_requirements(file):
    subprocess.call([os.path.join("venv", "Scripts", "pip"), "install", "-r", file])

if __name__ == "__main__":
    create_venv()
    for req in ["requirements.txt"]:
        install_requirements(req)
