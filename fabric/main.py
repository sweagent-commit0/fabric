"""
CLI entrypoint & parser configuration.

Builds on top of Invoke's core functionality for same.
"""
import getpass
from pathlib import Path
from invoke import Argument, Collection, Exit, Program
from invoke import __version__ as invoke
from paramiko import __version__ as paramiko, Agent
from . import __version__ as fabric
from . import Config, Executor

class Fab(Program):
    pass
program = make_program()