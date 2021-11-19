import os

import click
import pytest
from .framework.settings import VARS, NAME, VERSION, COVERAGERC_PATH
# mod = f"{_pgk_name}.framework.settings"
# NAME = _import_fun(mod, "NAME")
# VERSION = _import_fun(mod, "VERSION")
# COVERAGERC_PATH = _import_fun(mod, "COVERAGERC_PATH")

from .framework.settings import APPDIR, TESTDIR

# mod = f"{_pgk_name}.framework.derived_settings"
# APPDIR = _import_fun(mod, "APPDIR")
# TESTDIR = _import_fun(mod, "TESTDIR")

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
def vars_command():
    print(VARS)


@system_group.command(name="version")
def version_command():
    print(VERSION)


@system_group.command(name="selftest")
def selftest_command():
    os.chdir(TESTDIR)
    pytest.main(["-x", "-v", TESTDIR])

print([f"--cov-config={COVERAGERC_PATH}", f"--cov={NAME}", "--cov-report", "term-missing", APPDIR])

@system_group.command(name="selfcoverage")
def selfcoverage_command():
    os.chdir(APPDIR)
    pytest.main([
        f"--cov-config={COVERAGERC_PATH}", 
        f"--cov={NAME}", 
        "--cov-report", 
        "term-missing", 
        APPDIR])

# @click.command(name='hello-world')
# def hello():
#     print('hello world')

# cli.add_command(hello)
cli.add_command(system_group)
main = cli
