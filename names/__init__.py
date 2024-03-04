import check50

@check50.check()
def exists():
    """names.py exists"""
    check50.exists("names.py")

@check50.check(exists)
def test_valid_months():
    """correctly converts numbers to corresponding months"""
    months = {
        "1": "January",
        "2": "February",
        "3": "March",
        "4": "April",
        "5": "May",
        "6": "June",
        "7": "July",
        "8": "August",
        "9": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }
    for number, month in months.items():
        (check50.run("python3 names.py")
                .stdin(number)
                .stdout(f"The name of the month is {month}", regex=True)
                .exit(0))

@check50.check(exists)
def test_invalid_input():
    """displays error message for values outside 1-12"""
    (check50.run("python3 names.py")
            .stdin("13")
            .stdout("", regex=True)
            .exit(0))
    (check50.run("python3 names.py")
            .stdin("0")
            .stdout("", regex=True)
            .exit(0))

@check50.check(exists)
def test_non_numeric_input():
    """handles non-numeric input"""
    (check50.run("python3 names.py")
            .stdin("abc")
            .stdout("", regex=True)
            .exit(0))
