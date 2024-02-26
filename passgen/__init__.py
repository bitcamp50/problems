import check50
import re
import string
import random

@check50.check()
def exists():
    """password_generator.py exists."""
    check50.exists("passgen.py")
    check50.include("testing.py")

# @check50.check(exists)
# def test_valid_input():
#     """Valid input produces correct output."""
#     n1 = '2'
#     n2 = '2'
#     n3 = '8'
#     pattern = re.compile(fr'^(?=.*\d{{{int(n1)}}})(?=.*[\W_]{{{int(n2)}}})[A-Za-z\d\W_]{{{int(n3)}}}$')
#     random.seed(42)
#     # Generate a random password
#     password = ''.join(random.choices(string.ascii_letters, k=4) + random.choices(string.digits,k=2) + random.choices(string.punctuation,k=2))
    
#     # Check if the generated password matches the specified pattern
#     if pattern.match(password):
#         expected_output = f"Your password is\n{password}"
#     else:
#         expected_output = None

#     # Run the program and validate the output
#     if expected_output is not None:
#         check50.run("python passgen.py").stdin(n3).stdin(n2).stdin(n1).stdout(expected_output, regex=True).exit()
#     else:
#         check50.run("python passgen.py").stdin(n3).stdin(n2).stdin(n1).exit()

@check50.check(exists)
def test_valid_input():
    result = "<hb2:O3"
    check50.run("python passgen.py").stdin("7").stdin("2").stdin("2").stdout(f"Your password is\n{result}", regex=True).exit()

def regex(pattern):
    """Match case-insensitively with any characters on either side"""
    return fr'^.*{pattern}.*$'
