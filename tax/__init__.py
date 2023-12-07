import check50

@check50.check()
def exists():
    """tax.py exists"""
    check50.exists("tax.py")

@check50.check(exists)
def test_wisconsin_tax():
    """calculates tax correctly for Wisconsin residents"""
    (check50.run("python3 tax.py")
            .stdin("50")
            .stdin("WI")
            .stdout("The subtotal is \$50.00.\nThe tax is \$2.75.\nThe total is \$52.75.", regex=True)
            .exit(0))

@check50.check(exists)
def test_non_wisconsin():
    """displays total without tax for non-Wisconsin residents"""
    (check50.run("python3 tax.py")
            .stdin("50")
            .stdin("MN")
            .stdout("The total is \$50.00", regex=True)
            .exit(0))

@check50.check(exists)
def test_zero_order_amount():
    """handles zero order amount"""
    (check50.run("python3 tax.py")
            .stdin("0")
            .stdin("WI")
            .stdout("The subtotal is \$0.00.\nThe tax is \$0.00.\nThe total is \$0.00.", regex=True)
            .exit(0))

@check50.check(exists)
def test_negative_order_amount():
    """handles negative order amount"""
    (check50.run("python3 tax.py")
            .stdin("-10")
            .stdin("WI")
            .stdout("", regex=False)
            .exit(1))

@check50.check(exists)
def test_invalid_state_input():
    """handles invalid state input"""
    (check50.run("python3 tax.py")
            .stdin("50")
            .stdin("XYZ")
            .stdout("", regex=False)
            .exit(1))

@check50.check(exists)
def test_non_numeric_order_amount():
    """handles non-numeric order amount"""
    (check50.run("python3 tax.py")
            .stdin("abc")
            .stdin("WI")
            .stdout("", regex=False)
            .exit(1))