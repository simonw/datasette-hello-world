from datasette.cli import cli
from click.testing import CliRunner
import sqlite3


def test_verify():
    runner = CliRunner()
    result = runner.invoke(cli, ["hello-world"])
    assert result.exit_code == 0
    assert result.output.strip() == "Hello world"
