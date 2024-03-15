import check50

@check50.check()
def exists():
    """Test if paint.py exists."""
    check50.exists("test_paint.py")
    check50.exists("paint.py")


@check50.check(exists)
def test_investment():
    """Test calculation of the correct values"""
    check50.run("python3 paint.py")\
        .stdin("12")\
        .stdin("30")\
        .stdout("You will need to purchase 2 gallons of\npaint to cover 360 square feet.", regex=False)\
        .exit(0)
    

@check50.check(exists)
def test_investment_values():
    """Test calculation of the other correct values"""
    check50.run("python3 paint.py")\
        .stdin("30")\
        .stdin("15")\
        .stdout("You will need to purchase 2 gallons of\npaint to cover 420 square feet.", regex=False)\
        .exit(0)

@check50.check(exists)
def test_value_error():
    """Test for a string as an input"""
    check50.run("python3 paint.py")\
        .stdin("asdf")\
        .exit(1)