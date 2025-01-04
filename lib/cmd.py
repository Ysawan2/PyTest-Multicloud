import subprocess

class CmdRunner:
    def run_command(self, cmd, shell=True, timeout=2*60):
        output = subprocess.run(cmd, shell=shell, timeout=timeout)
        if output.stderr:
            return output.stderr
        return output.stdout
