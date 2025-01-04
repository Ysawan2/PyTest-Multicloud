from lib.cmd import run

import pytest

@pytest.fixture
def cmd_run():
    return run
