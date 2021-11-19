import os
import click
import pytest
from . import core
from .framework.settings import VARS, NAME, VERSION, COVERAGERC_PATH
from .framework.settings import APPDIR, TESTDIR

PROJECT_NAME = NAME

context_settings = {"help_option_names": ["-h", "--help"]}


@click.group(context_settings=context_settings)
@click.version_option(prog_name=PROJECT_NAME.capitalize(), version=VERSION)
@click.pass_context
def cli(ctx):
    pass


@click.group(name="system")
def system_group():
    pass


@system_group.command(name="vars")
def vars_cli():
    print(VARS)


@system_group.command(name="version")
def version_cli():
    print(VERSION)


@system_group.command(name="selftest")
def selftest_cli():
    os.chdir(TESTDIR)
    pytest.main(["-x", "-v", TESTDIR])


@system_group.command(name="selfcoverage")
def selfcoverage_cli():
    os.chdir(APPDIR)
    pytest.main([f"--cov-config={COVERAGERC_PATH}", f"--cov={NAME}", "--cov-report", "term-missing", APPDIR])


@click.command(name="core")
def core_cli():
    print("hello world")


cli.add_command(core_cli)
cli.add_command(system_group)
main = cli
