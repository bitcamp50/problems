import check50
import random

@check50.check()
def exists():
    """password_generator.py exists."""
    check50.exists("passgen.py")
    check50.include("testing.py")

@check50.check(exists)
def test_valid_input():
    
    result = f"Your password is\nabc@!12"
    check50.run("python3 testing.py").stdin("7").stdin("2").stdin("2").stdout(result, regex=False).exit()