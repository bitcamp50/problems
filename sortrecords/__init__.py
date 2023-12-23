import check50

@check50.check()
def exists():
    """sortrecords.py exists"""
    check50.exists("sortrecords.py")

@check50.check(exists)
def test_sorted_output():
    """checks if employees are sorted by last name and correctly formatted"""
    expected_output = (
        "Name\s*\|\s*Position\s*\|\s*Separation Date\s*\n"
        "-+\s*\|\s*-+\s*\|\s*-+\s*\n"
        "Jacquelyn Jackson\s*\|\s*DBA\s*\|\s*\n"
        "Jake Jacobson\s*\|\s*Programmer\s*\|\s*\n"
        "John Johnson\s*\|\s*Manager\s*\|\s*2016-12-31\s*\n"
        "Michaela Michaelson\s*\|\s*District Manager\s*\|\s*2015-12-19\s*\n"
        "Sally Weber\s*\|\s*Web Developer\s*\|\s*2015-12-18\s*\n"
        "Tou Xiong\s*\|\s*Software Engineer\s*\|\s*2016-10-05"
    )
    check50.run("python3 sortrecords.py").stdout(expected_output, regex=True).exit(0)
