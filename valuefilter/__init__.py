import check50

@check50.check()
def exists():
    """valuefilter.py exists"""
    check50.exists("valuefilter.py")

@check50.check(exists)
def test_even_numbers():
    """correctly filters out only even numbers from a mixed list"""
    check50.run("python3 valuefilter.py").stdin("1 2 3 4 5 6 7 8").stdout("The even numbers are 2 4 6 8.").exit(0)

@check50.check(exists)
def test_all_even_numbers():
    """correctly handles a list of all even numbers"""
    check50.run("python3 valuefilter.py").stdin("2 4 6 8").stdout("The even numbers are 2 4 6 8.").exit(0)

@check50.check(exists)
def test_no_even_numbers():
    """correctly handles a list with no even numbers"""
    check50.run("python3 valuefilter.py").stdin("1 3 5 7").stdout("The even numbers are ").exit(0)

@check50.check(exists)
def test_empty_input():
    """handles empty input correctly"""
    check50.run("python3 valuefilter.py").stdin("").stdout("The even numbers are ").exit(0)
