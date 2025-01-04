import subprocess

def run(cmd):
    output = subprocess.run(cmd, shell=True, timeout=2*60)
    return output.stdout
