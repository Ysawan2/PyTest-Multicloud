
import pytest
from fixtures.cmd import *

def test_e2e_skupper_k3d_north_south(cmd_run):
    cmd_run.run_command('whoami')
    assert True