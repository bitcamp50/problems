import check50

@check50.check()
def exists():
    """simple.py exists"""
    check50.exists("simple.py")

@check50.check(exists)
def test_valid_input():
    """correctly performs arithmetic operations with valid inputs"""
    (check50.run("python3 simple.py")
            .stdin("10")
            .stdin("5")
            .stdout("10 + 5 = 15\n10 - 5 = 5\n10 * 5 = 50\n10 / 5 = 2.0",regex=False)
            .exit(0))

@check50.check(exists)
def test_zero_division():
    """handles division by zero appropriately"""
    (check50.run("python3 simple.py")
            .stdin("10")
            .stdin("0")
            .stdout("", regex=False)
            .exit(1))

@check50.check(exists)
def test_negative_numbers():
    """correctly handles negative numbers"""
    (check50.run("python3 simple.py")
            .stdin("6")
            .stdin("3")
            .stdout("6 + 3 = 9\n6 - 3 = 3\n6 * 3 = 18\n6 / 3 = 2.0",regex=False)
            .exit(0))

@check50.check(exists)
def test_non_numeric_input():
    """handles non-numeric input gracefully"""
    (check50.run("python3 simple.py")
            .stdin("abc")
            .stdin("5")
            .stdout("", regex=False)
            .exit(1))
