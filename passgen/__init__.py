import check50
import re
import string

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
    text = "12#Abcde"
    expected_output = test_regex(text, n1, n2, n3)
    first_run = check50.run("python passgen.py").stdin(n3).stdin(n2).stdin(n1).stdout().exit()
    if expected_output:
        check50.run("python passgen.py").stdin(n3).stdin(n2).stdin(n1).stdout(first_run).exit()
    
def test_regex(txt, n1,n2,n3):
    pattern = re.compile(fr'^Your password is\n(?=.*\d{{{int(n1)}}})(?=.*[\W_]{{{int(n2)}}})[A-Za-z\d\W_]{{{int(n3)}}}$')
    return pattern.match(txt)
