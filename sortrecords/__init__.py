import check50

@check50.check()
def exists():
    """sortrecords.py exists"""
    check50.exists("sortrecords.py")

@check50.check(exists)
def test_sorted_output():
    """checks if employees are sorted by last name and correctly formatted"""
    expected_output = (
        r"Name\s*\|\s*Position\s*\|\s*Separation Date\s*\n"
        r"-+\s*\|\s*-+\s*\|\s*-+\s*\n"
        r"Jacquelyn Jackson\s*\|\s*DBA\s*\|\s*\n"
        r"Jake Jacobson\s*\|\s*Programmer\s*\|\s*\n"
        r"John Johnson\s*\|\s*Manager\s*\|\s*2016-12-31\s*\n"
        r"Michaela Michaelson\s*\|\s*District Manager\s*\|\s*2015-12-19\s*\n"
        r"Sally Weber\s*\|\s*Web Developer\s*\|\s*2015-12-18\s*\n"
        r"Tou Xiong\s*\|\s*Software Engineer\s*\|\s*2016-10-05"
    )
    check50.run("python3 sortrecords.py").stdout(expected_output, regex=True).exit(0)
