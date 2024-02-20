import check50
import re

@check50.check()
def exists():
    """password_generator.py exists."""
    check50.exists("passgen.py")

@check50.check(exists)
def test_valid_input():
    """Valid input produces correct output."""
    check = check50.run("python passgen.py").stdin("8").stdin("2").stdin("2")
    output = check50.run("python passgen.py").stdin("8").stdin("2").stdin("2").stdout()
    assert re.match(r"Your Password is [a-zA-Z0-9$@!#%&*]+", output), "Invalid password format"

@check50.check(exists)
def test_non_integer_input():
    """Non-integer input prompts again."""
    check = check50.run("python passgen.py").stdin("abc").stdin("def").stdin("ghi")
    assert check.stdout() == "Please enter an integer.\n" * 3, "Non-integer input not handled properly"

@check50.check(exists)
def test_zero_minimum_length():
    """Minimum length of zero results in error."""
    check = check50.run("python passgen.py").stdin("0").stdin("1").stdin("1")
    assert check.stdout() == "Minimum length must be greater than zero.\n", "Minimum length zero not handled properly"