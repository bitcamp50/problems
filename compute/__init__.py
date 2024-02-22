import check50

@check50.check()
def exists():
    """compute.py exists"""
    check50.exists("compute.py")

@check50.check(exists)
def test_valid_input():
    """correctly calculates statistics for valid inputs"""
    check50.run("python3 compute.py")\
        .stdin("100")\
        .stdin("200")\
        .stdin("1000")\
        .stdin("300")\
        .stdin("done")\
        .stdout("Numbers: 100, 200, 1000, 300")\
        .stdout("The average is 400.")\
        .stdout("The minimum is 100.")\
        .stdout("The maximum is 1000.")\
        .stdout(r"The standard deviation is (400\.25|437\.82)")\
        .exit(0)

@check50.check(exists)
def test_single_input():
    """handles a single input correctly"""
    check50.run("python3 compute.py")\
        .stdin("500")\
        .stdin("done")\
        .stdout("Numbers: 500")\
        .stdout("The average is 500.")\
        .stdout("The minimum is 500.")\
        .stdout("The maximum is 500.")\
        .stdout("The standard deviation is 0.0")\
        .exit(0)

@check50.check(exists)
def test_no_input():
    """handles no input before 'done' correctly"""
    check50.run("python3 compute.py")\
        .stdin("done")\
        .stdout("Numbers: ")\
        .stdout("The average is 0.")\
        .stdout("The minimum is 0.")\
        .stdout("The maximum is 0.")\
        .stdout("The standard deviation is 0.0")\
        .exit(0)
