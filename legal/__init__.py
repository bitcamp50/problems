import check50

@check50.check()
def exists():
    """legal.py exists"""
    check50.exists("legal.py")

@check50.check(exists)
def test_old_enough():
    """displays legal driving message for ages 16 and older"""
    (check50.run("python3 legal.py")
            .stdin("16")
            .stdout("You are old enough to legally drive.", regex=False)
            .exit(0))
    (check50.run("python3 legal.py")
            .stdin("35")
            .stdout("You are old enough to legally drive.", regex=False)
            .exit(0))

@check50.check(exists)
def test_not_old_enough():
    """displays not legal driving message for ages under 16"""
    (check50.run("python3 legal.py")
            .stdin("15")
            .stdout("You are not old enough to legally drive.", regex=False)
            .exit(0))

@check50.check(exists)
def test_edge_case():
    """handles edge cases correctly"""
    (check50.run("python3 legal.py")
            .stdin("16")
            .stdout("You are old enough to legally drive.", regex=False)
            .exit(0))
    (check50.run("python3 legal.py")
            .stdin("15.9")
            .exit(1))

@check50.check(exists)
def test_non_numeric_input():
    """handles non-numeric age input"""
    (check50.run("python3 legal.py")
            .stdin("abc")
            .exit(1))
