import check50

@check50.check()
def exists():
    """Test if checkout.py exists."""
    check50.exists("checkout.py")


@check50.check(exists)
def test_subtotal():
    """Test if values are calculated correctly."""
    check50.run("python3 checkout.py")\
        .stdin("1")\
        .stdin("1")\
        .stdin("2")\
        .stdin("3")\
        .stdin("4")\
        .stdin("5")\
        .stdout("Subtotal: $27.00\nTax: $1.49\nTotal: $28.48", regex=False)\
        .exit(0)

@check50.check(exists)
def test_subtotal_2():
    """Test if values are calculated correctly 2"""
    check50.run("python3 checkout.py")\
        .stdin("25")\
        .stdin("2")\
        .stdin("10")\
        .stdin("1")\
        .stdin("4")\
        .stdin("1")\
        .stdout("Subtotal: $64.00\nTax: $3.52\nTotal: $67.52", regex=False)\
        .exit(0)

@check50.check(exists)
def test_subtotal_3():
    """Test if values are calculated correctly 3"""
    check50.run("python3 checkout.py")\
        .stdin("16")\
        .stdin("4")\
        .stdin("3")\
        .stdin("54")\
        .stdin("1")\
        .stdin("2")\
        .stdout("Subtotal: $228.00\nTax: $12.54\nTotal: $240.54", regex=False)\
        .exit(0)
