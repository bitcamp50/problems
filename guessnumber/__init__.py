import check50

@check50.check()
def exists():
    """guessnumber.py exists"""
    check50.exists("guessnumber.py")
    # This line is conceptual, assuming testing.py is prepared for testing
    check50.include("testing.py")

@check50.check(exists)
def test_level_1_fixed_guess():
    """Level 1 gameplay with fixed guess works"""
    check50.run("python3 testing.py")\
        .stdin("1")\
        .stdin("5")\
        .stdout("You got it in 1 guess!", regex=True)\
        .exit(0)

@check50.check(exists)
def test_level_2_fixed_guess():
    """Level 2 gameplay with fixed guess works"""
    check50.run("python3 testing.py")\
        .stdin("2")\
        .stdin("50")\
        .stdout("You got it in 1 guess!", regex=True)\
        .exit(0)

@check50.check(exists)
def test_level_3_fixed_guess():
    """Level 3 gameplay with fixed guess works"""
    check50.run("python3 testing.py")\
        .stdin("3")\
        .stdin("500")\
        .stdout("You got it in 1 guess!", regex=True)\
        .exit(0)

@check50.check(exists)
def test_invalid_input_guess():
    """Handles non-numeric guess input"""
    check50.run("python3 testing.py")\
        .stdin("1")\
        .stdin("not a number", prompt=True)\
        .stdout("Please enter a valid number. Non-numeric entries count as wrong guesses.", regex=True)\
        .stdin("5")\
        .stdout("You got it in 2 guesses!", regex=True)\
        .exit(0)

@check50.check(exists)
def test_play_again_yes_then_no():
    """Player chooses to play again and then chooses not to"""
    check50.run("python3 testing.py")\
        .stdin("1")\
        .stdin("5", prompt=True)\
        .stdout("You got it in 1 guess!", regex=True)\
        .stdin("y")\
        .stdin("1")\
        .stdin("5", prompt=True)\
        .stdout("You got it in 1 guess!", regex=True)\
        .stdin("n")\
        .stdout("Goodbye!", regex=True)\
        .exit(0)

def regex(pattern):
    """Match case-insensitively with any characters on either side"""
    return fr'^.*{pattern}.*$'
