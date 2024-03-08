import check50

@check50.check()
def exists():
    """Test if interest.py exists."""
    check50.exists("test_interest.py")
    check50.exists("interest.py")


@check50.check(exists)
def test_investment():
    """Test calculation of the investment"""
    check50.run("python3 interest.py")\
        .stdin("1500")\
        .stdin("4.3")\
        .stdin("4")\
        .stdout("After 4 years at 4.3%, the investment will\nbe worth $1758.", regex=False)\
        .exit(0)
    

@check50.check(exists)
def test_investment_values():
    """Test calculation of the investment with different inputs"""
    check50.run("python3 interest.py")\
        .stdin("1300")\
        .stdin("2.3")\
        .stdin("6")\
        .stdout("After 6 years at 2.3%, the investment will\nbe worth $1479.", regex=False)\
        .exit(0)

@check50.check(exists)
def test_value_error():
    """Test for a string as an input"""
    check50.run("python3 interest.py")\
        .stdin("asdf")\
        .exit(1)