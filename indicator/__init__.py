import check50

@check50.check()
def exists():
    """indicator.py exists"""
    check50.exists("indicator.py")

@check50.check(exists)
def test_very_weak_password():
    """Identifies very weak passwords correctly"""
    check50.run("python3 indicator.py").stdin("12345").stdout("The password '12345' is a very weak password.").exit(0)

@check50.check(exists)
def test_weak_password():
    """Identifies weak passwords correctly"""
    check50.run("python3 indicator.py").stdin("abcdef").stdout("The password 'abcdef' is a weak password.").exit(0)

@check50.check(exists)
def test_strong_password():
    """Identifies strong passwords correctly"""
    check50.run("python3 indicator.py").stdin("abc123xyz").stdout("The password 'abc123xyz' is a strong password.").exit(0)

@check50.check(exists)
def test_very_strong_password():
    """Identifies very strong passwords correctly"""
    check50.run("python3 indicator.py").stdin("1337h@xor!").stdout("The password '1337h@xor!' is a very strong password.").exit(0)

@check50.check(exists)
def test_mixed_case_password():
    """Identifies passwords with mixed case as strong or very strong correctly"""
    check50.run("python3 indicator.py").stdin("Abc123Xyz").stdout("The password 'Abc123Xyz' is a strong password.", regex=True).exit(0)
    check50.run("python3 indicator.py").stdin("A1b2C3@d4!").stdout("The password 'A1b2C3@d4!' is a very strong password.", regex=True).exit(0)
