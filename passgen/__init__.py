import check50
import re
import string
import random

@check50.check()
def exists():
    """password_generator.py exists."""
    check50.exists("passgen.py")

@check50.check(exists)
def test_valid_input():
    """Valid input produces correct output."""
    n1 = '2'
    n2 = '2'
    n3 = '8'
    pattern = re.compile(fr'^(?=.*\d{{{int(n1)}}})(?=.*[\W_]{{{int(n2)}}})[A-Za-z\d\W_]{{{int(n3)}}}$')

    # Generate a random password
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=int(n3)))

    # Check if the generated password matches the specified pattern
    if pattern.match(password):
        expected_output = f"Your password is\n{password}"
    else:
        expected_output = None

    # Run the program and validate the output
    check50.run("python passgen.py").stdin(n3).stdin(n2).stdin(n1).stdout(expected_output, regex=True).exit()
