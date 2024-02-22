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
    # check = check50.run("python passgen.py").stdin("8").stdin("2").stdin("2").exit(0)
    n1 = 2
    n2 = 2
    n3 = 8
    text = "12#Abcde"
    check50.run("python passgen.py").stdin(n3).stdin(n2).stdin(n1).stdout(test_regex(text, n1,n2,n3),text,regex=True).exit()
    
def test_regex(txt, n1,n2,n3):
    pattern = re.compile(fr'^(?=.*\d{{{n1}}})(?=.*[\W_]{{{n2}}})[A-Za-z\d\W_]{{{n3}}}$')
    return pattern.match(txt)
# @check50.check(exists)
# def test_non_integer_input():
#     """Non-integer input prompts again."""
#     check = check50.run("python passgen.py").stdin("abc").stdin("def").stdin("ghi")
#     assert check.stdout() == "Please enter an integer.\n" * 3, "Non-integer input not handled properly"

# @check50.check(exists)
# def test_zero_minimum_length():
#     """Minimum length of zero results in error."""
#     check = check50.run("python passgen.py").stdin("0").stdin("1").stdin("1")
#     assert check.stdout() == "Minimum length must be greater than zero.\n", "Minimum length zero not handled properly"