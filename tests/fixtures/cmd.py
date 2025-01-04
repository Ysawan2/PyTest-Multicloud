from lib import cmd

import pytest

@pytest.fixture
def cmd_run():
    return cmd.CmdRunner()
