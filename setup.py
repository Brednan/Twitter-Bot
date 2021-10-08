import sys
from cx_Freeze import setup, Executable

setup(
    name='Twitter Follow Bot',
    version='V1',
    description='An app that allows you to submit twitter accounts, goes through each one, and follows the user that you specify.',
    executables=[Executable("GUI.py", base="Win32GUI")]
)