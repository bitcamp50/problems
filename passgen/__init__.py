import check50
import re

@check50.check()
def exists():
    """password.py exists"""
    check50.exists("passgen.py")

@check50.check(exists)
def test_valid_input():
    """validates correct password"""
    output = check50.run("python passgen.py").stdin("8").stdin("2").stdin("2").stdout()
    (check50.run("python3 passgen.py")
            .stdin("8")
            .stdin("2")
            .stdin("2")
            .stdout(re.compile(r"Your password is [a-zA-Z0-9$@!#%&*]+").search(output), regex=True)
            .exit(0))