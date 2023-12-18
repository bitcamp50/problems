import check50

@check50.check()
def exists():
    """converter.py exists"""
    check50.exists("converter.py")

@check50.check(exists)
def test_fahrenheit_to_celsius_lower():
    """correctly converts Fahrenheit to Celsius (lowercase input)"""
    (check50.run("python3 converter.py")
            .stdin("c")
            .stdin("32")
            .stdout("The temperature in Celsius is 0.", regex=False)
            .exit(0))

@check50.check(exists)
def test_fahrenheit_to_celsius_upper():
    """correctly converts Fahrenheit to Celsius (uppercase input)"""
    (check50.run("python3 converter.py")
            .stdin("C")
            .stdin("32")
            .stdout("The temperature in Celsius is 0.", regex=False)
            .exit(0))

@check50.check(exists)
def test_celsius_to_fahrenheit_lower():
    """correctly converts Celsius to Fahrenheit (lowercase input)"""
    (check50.run("python3 converter.py")
            .stdin("f")
            .stdin("0")
            .stdout("The temperature in Fahrenheit is 32.", regex=False)
            .exit(0))

@check50.check(exists)
def test_celsius_to_fahrenheit_upper():
    """correctly converts Celsius to Fahrenheit (uppercase input)"""
    (check50.run("python3 converter.py")
            .stdin("F")
            .stdin("0")
            .stdout("The temperature in Fahrenheit is 32.", regex=False)
            .exit(0))

@check50.check(exists)
def test_invalid_input():
    """handles invalid temperature conversion option"""
    (check50.run("python3 converter.py")
            .stdin("X")
            .stdin("32")
            .exit(1))

@check50.check(exists)
def test_non_numeric_temperature():
    """handles non-numeric temperature input"""
    (check50.run("python3 converter.py")
            .stdin("C")
            .stdin("abc")
            .exit(1))
