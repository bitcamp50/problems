import check50
import random

@check50.check()
def exists():
    """password_generator.py exists."""
    check50.exists("pickwinner.py")
    check50.include("testing.py")

@check50.check(exists)
def test_valid_input():
    ''' Test With Valid inputs.'''
    names = ["Alice", "Bob", "Charlie"]
    the_file = check50.run("python3 testing.py")
    
    the_file.stdin(names[0]).stdin(names[1]).stdin(names[2]).stdin('').stdout(f"The winner is... Bob.", regex=False).exit(0)

@check50.check(exists)
def test_blank_input():
    ''' Test With No inputs.'''
    the_file = check50.run("python3 pickwinner.py")
    the_file.stdin("").stdout(f"The name list is empty", regex=False).exit(0)

@check50.check(exists)
def test_small_input():
    ''' Test With one character inputs.'''
    the_file = check50.run("python3 pickwinner.py")
    the_file.stdin("a").stdin("b").stdin("c").stdin("").stdout(f"The name list is empty", regex=False).exit(0)

@check50.check(exists)
def test_number_input():
    ''' Test With number inputs.'''
    the_file = check50.run("python3 pickwinner.py")
    the_file.stdin("11").stdin("22").stdin("33").stdin("").stdout(f"The name list is empty", regex=False).exit(0)