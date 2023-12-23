import check50

@check50.check()
def exists():
    """filterrecords.py exists"""
    check50.exists("filterrecords.py")

@check50.check(exists)
def test_filter_by_last_name():
    """filters records by last name"""
    expected_output = (
        "Results:\s*\n"
        "Name\s*\|\s*Position\s*\|\s*Separation Date\s*\n"
        "-+\s*\|\s*-+\s*\|\s*-+\s*\n"
        "Jacquelyn Jackson\s*\|\s*DBA\s*\|\s*\n"
        "Jake Jacobson\s*\|\s*Programmer\s*\|\s*"
    )
    check50.run("python3 filterrecords.py").stdin("Jac").stdout(expected_output, regex=True).exit(0)

@check50.check(exists)
def test_filter_by_first_name():
    """filters records by first name"""
    expected_output = (
        "Results:\s*\n"
        "Name\s*\|\s*Position\s*\|\s*Separation Date\s*\n"
        "-+\s*\|\s*-+\s*\|\s*-+\s*\n"
        "Tou Xiong\s*\|\s*Software Engineer\s*\|\s*2016-10-05"
    )
    check50.run("python3 filterrecords.py").stdin("Tou").stdout(expected_output, regex=True).exit(0)

@check50.check(exists)
def test_no_results():
    """handles no matching results"""
    expected_output = "Results:\s*\nNo matching records found."
    check50.run("python3 filterrecords.py").stdin("XYZ").stdout(expected_output, regex=True).exit(0)
