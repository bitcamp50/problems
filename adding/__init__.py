import check50

@check50.check()
def exists():
    """adding.py exists"""
    check50.exists("adding.py")

@check50.check(exists)
def test_sum_five_numbers():
    """correctly adds five numbers"""
    check50.run("python3 adding.py").stdin("1").stdin("2").stdin("3").stdin("4").stdin("5").stdout("The total is 15.").exit(0)

@check50.check(exists)
def test_sum_five_different_numbers():
    """correctly adds a different set of five numbers"""
    check50.run("python3 adding.py").stdin("-1").stdin("-2").stdin("3").stdin("4").stdin("5").stdout("The total is 9.").exit(0)

@check50.check(exists)
def test_sum_five_zeros():
    """correctly adds five zeros"""
    check50.run("python3 adding.py").stdin("0").stdin("0").stdin("0").stdin("0").stdin("0").stdout("The total is 0.").exit(0)

@check50.check(exists)
def test_non_numeric_input():
    """handles non-numeric input"""
    check50.run("python3 adding.py").stdin("abc").stdin("1").stdin("2").stdin("3").stdin("4").stdout("", regex=False).exit(0)
