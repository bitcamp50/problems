import check50

@check50.check()
def exists():
    """Test if currency.py exists."""
    check50.exists("test_currency.py")

    check50.exists("currency.py")


@check50.check(exists)
def test_subtotal():
    """Test if a number is converted correctly."""
    check50.run("python3 currency.py")\
        .stdin("81")\
        .stdin("137.51")\
        .stdout("81 euros at an exchange rate of 137.51 is\n111.38 U.S. dollars.", regex=False)\
        .exit(0)

@check50.check(exists)
def test_conversion():
    """Test different inputs for conversion"""
    check50.run("python3 currency.py")\
        .stdin("50")\
        .stdin("1.1")\
        .stdout("50 euros at an exchange rate of 1.1 is\n0.55 U.S. dollars.", regex=False)\
        .exit(0)
    
@check50.check(exists)
def test_value_error():
    """Test for a string as an input"""
    check50.run("python3 currency.py")\
        .stdin("asdf")\
        .exit(1)