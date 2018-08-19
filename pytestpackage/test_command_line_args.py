import pytest

# CLI TO RUN WITH BROWSER ARG: py.test -s -v test_command_line_args.py --browser chrome

def test_command_line_methodA(oneTimeSetUp, setUp):
    print("Running method A")

def test_command_line_methodB(oneTimeSetUp, setUp):
    print("Running method B")