import check50
import re

@check50.check()
def exists():
    """guessnumber.py exists"""
    check50.exists("guessnumber.py")

@check50.check(exists)
def test_level_1():
    """Level 1 gameplay works"""
    # Simulate gameplay where the expected random number is 5 for level 1
    check50.run("python3 guessnumber.py").stdin("1").stdin("1", prompt=True)\
        .stdout("Too low. Guess again:", regex=True).stdin("10", prompt=True)\
        .stdout("Too high. Guess again:", regex=True).stdin("5", prompt=True)\
        .stdout("You got it in 3 guesses!", regex=True).exit(0)

@check50.check(exists)
def test_level_2():
    """Level 2 gameplay works"""
    # Assuming a mock or predetermined random function that selects 50 for level 2
    check50.run("python3 guessnumber.py").stdin("2").stdin("1", prompt=True)\
        .stdout("Too low. Guess again:", regex=True).stdin("100", prompt=True)\
        .stdout("Too high. Guess again:", regex=True).stdin("50", prompt=True)\
        .stdout("You got it in 3 guesses!", regex=True).exit(0)

@check50.check(exists)
def test_level_3():
    """Level 3 gameplay works"""
    # Assuming a mock or predetermined random function that selects 500 for level 3
    check50.run("python3 guessnumber.py").stdin("3").stdin("1", prompt=True)\
        .stdout("Too low. Guess again:", regex=True).stdin("1000", prompt=True)\
        .stdout("Too high. Guess again:", regex=True).stdin("500", prompt=True)\
        .stdout("You got it in 3 guesses!", regex=True).exit(0)

@check50.check(exists)
def test_non_numeric_guess():
    """Handles non-numeric guesses"""
    check50.run("python3 guessnumber.py").stdin("1").stdin("abc", prompt=True)\
        .stdout(".*", regex=True).stdin("5", prompt=True)\
        .stdout("You got it in 2 guesses!", regex=True).exit(0)

@check50.check(exists)
def test_play_again():
    """Prompts to play again and exits on 'n'"""
    check50.run("python3 guessnumber.py").stdin("1").stdin("5", prompt=True)\
        .stdout("You got it in 1 guess!", regex=True).stdin("n")\
        .stdout("Goodbye!", regex=True).exit(0)

def regex(pattern):
    """Match case-insensitively with any characters on either side"""
    return fr'^.*{re.escape(pattern)}.*$'
