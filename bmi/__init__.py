import check50

@check50.check()
def exists():
    """bmi.py exists"""
    check50.exists("bmi.py")

@check50.check(exists)
def test_normal_weight():
    """correctly calculates BMI and identifies normal weight"""
    (check50.run("python3 bmi.py")
            .stdin("68")
            .stdin("150")
            .stdout("Your BMI is 22.8.\nYou are within the ideal weight range.", regex=False)
            .exit(0))

@check50.check(exists)
def test_underweight():
    """correctly calculates BMI and identifies underweight"""
    (check50.run("python3 bmi.py")
            .stdin("68")
            .stdin("100")
            .stdout("Your BMI is 15.2.\nYou are underweight. You should see your doctor.", regex=False)
            .exit(0))

@check50.check(exists)
def test_overweight():
    """correctly calculates BMI and identifies overweight"""
    (check50.run("python3 bmi.py")
            .stdin("68")
            .stdin("200")
            .stdout("Your BMI is 30.4.\nYou are overweight. You should see your doctor.", regex=False)
            .exit(0))

@check50.check(exists)
def test_non_numeric_input():
    """handles non-numeric input for weight and height"""
    (check50.run("python3 bmi.py")
            .stdin("abc")
            .stdin("68")
            .exit(1))
    (check50.run("python3 bmi.py")
            .stdin("150")
            .stdin("xyz")
            .exit(1))
