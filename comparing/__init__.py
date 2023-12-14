import check50

@check50.check()
def exists():
    """comparing.py exists"""
    check50.exists("comparing.py")

@check50.check(exists)
def test_largest_number():
    """identifies the largest number correctly"""
    (check50.run("python3 comparing.py")
            .stdin("1")
            .stdin("51")
            .stdin("2")
            .stdout("The largest number is 51.", regex=False)
            .exit(0))

@check50.check(exists)
def test_all_numbers_different():
    """checks that all numbers are different and identifies the largest"""
    (check50.run("python3 comparing.py")
            .stdin("20")
            .stdin("10")
            .stdin("15")
            .stdout("The largest number is 20.", regex=False)
            .exit(0))

@check50.check(exists)
def test_duplicate_numbers():
    """exits program if not all numbers are different"""
    (check50.run("python3 comparing.py")
            .stdin("5")
            .stdin("5")
            .stdin("10")
            .exit(1))

@check50.check(exists)
def test_all_numbers_same():
    """exits program if all numbers are the same"""
    (check50.run("python3 comparing.py")
            .stdin("7")
            .stdin("7")
            .stdin("7")
            .exit(1))

@check50.check(exists)
def test_non_numeric_input():
    """handles non-numeric input"""
    (check50.run("python3 comparing.py")
            .stdin("abc")
            .stdin("10")
            .stdin("20")
            .exit(1))
