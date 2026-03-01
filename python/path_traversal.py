"""
Path Traversal — intentionally vulnerable (CodeGuard AI test fixture)
DO NOT USE IN PRODUCTION
"""
import os

BASE_DIR = "/var/www/uploads"

# VULN CWE-22: no path sanitization
def read_user_file(filename):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "r") as f:
        return f.read()

# VULN CWE-22: direct path construction from user input
def download_file(file_path):
    full_path = BASE_DIR + "/" + file_path
    with open(full_path, "rb") as f:
        return f.read()

# VULN CWE-22: user-controlled directory
def list_directory(subdir):
    path = "/data/" + subdir
    return os.listdir(path)
