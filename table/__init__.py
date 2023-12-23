import check50

@check50.check()
def exists():
    """table.py exists"""
    check50.exists("table.py")

@check50.check(exists)
def test_start_of_table():
    """checks the beginning of the table"""
    check50.run("python3 table.py").stdout("0 x 0 = 0\n0 x 1 = 0\n0 x 2 = 0").exit(0)

@check50.check(exists)
def test_middle_of_table():
    """checks the middle of the table"""
    check50.run("python3 table.py").stdout("6 x 6 = 36\n6 x 7 = 42\n6 x 8 = 48").exit(0)

@check50.check(exists)
def test_end_of_table():
    """checks the end of the table"""
    check50.run("python3 table.py").stdout("12 x 11 = 132\n12 x 12 = 144").exit(0)
