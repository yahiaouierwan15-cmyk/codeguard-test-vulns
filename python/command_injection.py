"""
Command Injection — intentionally vulnerable (CodeGuard AI test fixture)
DO NOT USE IN PRODUCTION
"""
import os
import subprocess

# VULN CWE-78: os.system with user input
def ping_host(hostname):
    os.system("ping -c 1 " + hostname)

# VULN CWE-78: subprocess.call with shell=True
def check_file(filename):
    subprocess.call(["ls", "-la", filename], shell=False)

# VULN CWE-78: os.popen with user input
def get_file_info(path):
    result = os.popen("file " + path)
    return result.read()

# VULN CWE-78: subprocess with user input concatenation
def run_script(script_name, args):
    cmd = f"python3 scripts/{script_name} {args}"
    subprocess.run(cmd, shell=True)