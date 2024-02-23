import check50

@check50.check()
def exists():
    """validating.py exists"""
    check50.exists("validating.py")

@check50.check(exists)
def test_invalid_first_name():
    """Rejects invalid first name"""
    check50.run("python3 validating.py")\
        .stdin("J")\
        .stdin("James")\
        .stdin("55555")\
        .stdin("JJ-1234")\
        .stdout(".*\"J\" is not a valid first name. It is too short.", regex=True)\
        .exit(0)

@check50.check(exists)
def test_invalid_last_name():
    """Rejects empty last name"""
    check50.run("python3 validating.py")\
        .stdin("Jimmy")\
        .stdin("")\
        .stdin("55555")\
        .stdin("JJ-1234")\
        .stdout(".*The last name must be filled in.", regex=True)\
        .exit(0)

@check50.check(exists)
def test_invalid_zip():
    """Rejects non-numeric ZIP code"""
    check50.run("python3 validating.py")\
        .stdin("Jimmy")\
        .stdin("James")\
        .stdin("ABCDE")\
        .stdin("JJ-1234")\
        .stdout(".*The ZIP code must be numeric.", regex=True)\
        .exit(0)

@check50.check(exists)
def test_invalid_employee_id():
    """Rejects incorrectly formatted employee ID"""
    check50.run("python3 validating.py")\
        .stdin("Jimmy")\
        .stdin("James")\
        .stdin("55555")\
        .stdin("A12-1234")\
        .stdout(".*A12-1234 is not a valid ID.", regex=True)\
        .exit(0)

@check50.check(exists)
def test_valid_input():
    """Accepts valid input with no errors"""
    check50.run("python3 validating.py")\
        .stdin("Jimmy")\
        .stdin("James")\
        .stdin("55555")\
        .stdin("TK-421")\
        .stdout(".*TK-421 is not a valid ID.", regex=True)\
        .exit(0)

@check50.check(exists)
def test_multiple_errors():
    """Handles multiple errors"""
    check50.run("python3 validating.py")\
        .stdin("J")\
        .stdin("")\
        .stdin("ABCDE")\
        .stdin("A12-1234")\
        .stdout(".*(not a valid first name|must be filled in|must be numeric|not a valid ID)", regex=True)\
        .exit(0)
