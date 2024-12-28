import os
import subprocess

def init_dvc():
    """Initialize DVC in the project."""
    try:
        print("Initializing DVC...")
        result = subprocess.run(["dvc", "init"], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during DVC initialization: {e.stderr}")

def add_remote(remote_path):
    """Set up local storage for DVC."""
    try:
        print(f"Adding remote storage at: {remote_path}")
        result = subprocess.run(
            ["dvc", "remote", "add", "-d", "-f", "localstorage", remote_path],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while adding remote: {e.stderr}")


def track_file(file_path):
    """Add a file to DVC tracking."""
    try:
        print(f"Tracking file: {file_path}")
        result = subprocess.run(["dvc", "add", file_path], check=True, capture_output=True, text=True)
        print(result.stdout)

        # Add the corresponding .dvc file to git
        result = subprocess.run(["git", "add", f"{file_path}.dvc"], check=True, capture_output=True, text=True)
        print(result.stdout)

        # Commit changes to git
        result = subprocess.run(["git", "commit", "-m", f"Track {file_path} with DVC"], check=True, capture_output=True, text=True)
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while tracking the file: {e.stderr}")

def push_data():
    """Push data to the remote DVC storage."""
    try:
        print("Pushing data to remote storage...")
        result = subprocess.run(["dvc", "push"], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while pushing data: {e.stderr}")
