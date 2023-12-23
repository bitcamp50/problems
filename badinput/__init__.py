import check50

@check50.check()
def exists():
    """badinput.py exists"""
    check50.exists("badinput.py")

@check50.check(exists)
def test_valid_input():
    """accepts valid input and calculates years correctly"""
    check50.run("python3 badinput.py").stdin("4").stdout("It will take 18 years to double your initial investment.").exit(0)

@check50.check(exists)
def test_zero_input():
    """rejects zero as invalid input and keeps prompting"""
    check50.run("python3 badinput.py").stdin("0").stdout("Sorry. That's not a valid input.").stdin("4").stdout("It will take 18 years to double your initial investment.").exit(0)

@check50.check(exists)
def test_non_numeric_input():
    """rejects non-numeric input and keeps prompting"""
    check50.run("python3 badinput.py").stdin("ABC").stdout("Sorry. That's not a valid input.").stdin("4").stdout("It will take 18 years to double your initial investment.").exit(0)

@check50.check(exists)
def test_multiple_bad_inputs():
    """handles multiple consecutive bad inputs before receiving valid input"""
    check50.run("python3 badinput.py").stdin("0").stdout("Sorry. That's not a valid input.").stdin("XYZ").stdout("Sorry. That's not a valid input.").stdin("4").stdout("It will take 18 years to double your initial investment.").exit(0)
