import check50

@check50.check()
def exists():
    """multistate.py exists"""
    check50.exists("multistate.py")

@check50.check(exists)
def test_wisconsin_eau_claire():
    """calculates tax correctly for Wisconsin Eau Claire county"""
    (check50.run("python3 multistate.py")
            .stdin("10")
            .stdin("Wisconsin")
            .stdin("Eau Claire")
            .stdout("The tax is $0.50.\nThe total is $10.50.", regex=False)
            .exit(0))

@check50.check(exists)
def test_wisconsin_dunn():
    """calculates tax correctly for Wisconsin Dunn county"""
    (check50.run("python3 multistate.py")
            .stdin("10")
            .stdin("Wisconsin")
            .stdin("Dunn")
            .stdout("The tax is $0.50.\nThe total is $10.50.", regex=False)
            .exit(0))

@check50.check(exists)
def test_illinois():
    """calculates tax correctly for Illinois residents"""
    (check50.run("python3 multistate.py")
            .stdin("10")
            .stdin("Illinois")
            .stdout("The tax is $0.80.\nThe total is $10.80.", regex=False)
            .exit(0))

@check50.check(exists)
def test_other_states():
    """no tax for residents of other states"""
    (check50.run("python3 multistate.py")
            .stdin("10")
            .stdin("California")
            .stdout("The total is $10.00", regex=False)
            .exit(0))

@check50.check(exists)
def test_non_numeric_order_amount():
    """handles non-numeric order amount"""
    (check50.run("python3 multistate.py")
            .stdin("abc")
            .exit(1))
