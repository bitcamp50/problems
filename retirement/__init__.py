import check50

@check50.check()
def exists():
    """retirement.py exists"""
    check50.exists("retirement.py")

@check50.check(exists)
def test_25_65():
    """input of 25 and 65 yields output \"You have 40 years left until you can retire.\" and \"It's 2015, so you can retire in 2055.\""""
    check50.run("python3 retirement.py").stdin("25").stdin("65").stdout("You have 40 years left until you can retire.").stdout("It's 2015, so you can retire in 2055.").exit(0)

@check50.check(exists)
def test_15_40():
    """input of 15 and 40 yields output \"You have 25 years left until you can retire.\" and \"It's 2015, so you can retire in 2040.\""""
    check50.run("python3 retirement.py").stdin("15").stdin("40").stdout("You have 25 years left until you can retire.").stdout("It's 2015, so you can retire in 2040.").exit(0)
    
@check50.check(exists)
def test_str():
    """input of \"three\" and \"four\" results in ValueError"""
    check50.run("python3 retirement.py").stdin("three").stdin("four").exit(1)

@check50.check(exists)
def test_float():
    """input of \"25.5\" and \"65.5\" results in ValueError"""
    check50.run("python3 retirement.py").stdin("25.5").stdin("65.5").exit(1)