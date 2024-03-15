import check50

@check50.check()
def exists():
    """Test if compound.py exists."""
    check50.exists("test_compound.py")
    check50.exists("compound.py")


@check50.check(exists)
def test_investment():
    """Test calculation of the correct values"""
    check50.run("python3 compound.py")\
        .stdin("1500")\
        .stdin("4.3")\
        .stdin("6")\
        .stdin("4")\
        .stdout("$1500 invested at 4.3% for 6 years\ncompounded 4 times per year is $1938.84.", regex=False)\
        .exit(0)

@check50.check(exists)
def test_investment():
    """Test calculation of the other correct values"""
    check50.run("python3 compound.py")\
        .stdin("2000")\
        .stdin("2.3")\
        .stdin("10")\
        .stdin("7")\
        .stdout("$2000 invested at 2.3% for 10 years\ncompounded 7 times per year is $2516.25.", regex=False)\
        .exit(0)


@check50.check(exists)
def test_value_error():
    """Test for a string as an input"""
    check50.run("python3 compound.py")\
        .stdin("asdf")\
        .exit(1)