import check50

@check50.check()
def exists():
    """multistate.py exists"""
    check50.exists("multistate.py")

@check50.check(exists)
def test_wisconsin_eau_claire():
    """correctly calculates tax for Wisconsin Eau Claire county"""
    (check50.run("python3 multistate.py")
            .stdin("10")
            .stdin("Wisconsin")
            .stdin("Eau Claire")
            .stdout("The tax is $0.55.\nThe total is $10.55.", regex=False)
            .exit(0))

@check50.check(exists)
def test_wisconsin_dunn():
    """correctly calculates tax for Wisconsin Dunn county"""
    (check50.run("python3 multistate.py")
            .stdin("10")
            .stdin("Wisconsin")
            .stdin("Dunn")
            .stdout("The tax is $0.54.\nThe total is $10.54.", regex=False)
            .exit(0))

@check50.check(exists)
def test_illinois():
    """correctly calculates tax for Illinois residents"""
    (check50.run("python3 multistate.py")
            .stdin("10")
            .stdin("Illinois")
            .stdout("The tax is $0.80.\nThe total is $10.80.", regex=False)
            .exit(0))

@check50.check(exists)
def test_other_state():
    """correctly handles states with no tax"""
    (check50.run("python3 multistate.py")
            .stdin("10")
            .stdin("California")
            .stdout("The total is $10.00", regex=False)
            .exit(0))

@check50.check(exists)
def test_invalid_input():
    """handles invalid state input"""
    (check50.run("python3 multistate.py")
            .stdin("10")
            .stdin("Atlantis")
            .exit(1))

@check50.check(exists)
def test_non_numeric_order_amount():
    """handles non-numeric order amount"""
    (check50.run("python3 multistate.py")
            .stdin("abc")
            .stdin("Wisconsin")
            .exit(1))
