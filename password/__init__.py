import check50

@check50.check()
def exists():
    """password.py exists"""
    check50.exists("password.py")

@check50.check(exists)
def test_correct_password():
    """validates correct password"""
    (check50.run("python3 password.py")
            .stdin("abc$123", prompt=True)
            .stdout("Welcome!", regex=False)
            .exit(0))

@check50.check(exists)
def test_incorrect_password():
    """rejects incorrect password"""
    (check50.run("python3 password.py")
            .stdin("12345", prompt=True)
            .stdout("I don't know you.", regex=False)
            .exit(0))

@check50.check(exists)
def test_case_sensitivity():
    """ensures password validation is case sensitive"""
    (check50.run("python3 password.py")
            .stdin("ABC$123", prompt=True)
            .stdout("I don't know you.", regex=False)
            .exit(0))

@check50.check(exists)
def test_empty_password():
    """handles empty password input"""
    (check50.run("python3 password.py")
            .stdin("")
            .stdout("I don't know you.", regex=False)
            .exit(0))
