import check50

@check50.check()
def exists():
    """guessnumber.py exists"""
    check50.exists("magicball.py")
    # This line is conceptual, assuming testing.py is prepared for testing
    check50.include("testing.py")



@check50.check(exists)
def test_invalid_input_guess():
    """Handles non-numeric guess input"""
    check50.run("python3 testing.py")\
        .stdin("fasdfasdfasdf?")\
        .stdout("Yes", regex=False)\
        .exit(0)


def regex(pattern):
    """Match case-insensitively with any characters on either side"""
    return fr'^.*{pattern}.*$'
