import check50
import random

@check50.check()
def exists():
    """password_generator.py exists."""
    check50.exists("passgen.py")
    check50.include("testing.py")

@check50.check(exists)
def test_valid_input():
    """Test valid inputs"""
    result = f"Your password is\nabc@!12"
    check50.run("python3 testing.py").stdin("7").stdin("2").stdin("2").stdout(result, regex=False).exit()

@check50.check(exists)
def test_invalid_input():
    """Test invalid inputs"""
    result = f"Your password is\nabc@!12"
    check50.run("python3 testing.py")\
    .stdin("cat").stdin("dog")\
    .stdin("table")\
    .stdin("7")\
    .stdin("2")\
    .stdin("2")\
    .stdout(result, regex=False).exit()