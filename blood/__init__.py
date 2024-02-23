import check50
from re import escape

@check50.check()
def exists():
    """blood.py exists"""
    check50.exists("blood.py")

@check50.check(exists)
def test_legal_male():
    """A male with legal BAC level"""
    check50.run("python3 blood.py")\
        .stdin("180")\
        .stdin("male")\
        .stdin("2")\
        .stdin("5")\
        .stdin("2")\
        .stdout("Your BAC is 0.18\nIt is not legal for you to drive.", regex=True)\
        .exit(0)

@check50.check(exists)
def test_illegal_female():
    """A female with illegal BAC level"""
    check50.run("python3 blood.py")\
        .stdin("140")\
        .stdin("female")\
        .stdin("3")\
        .stdin("5")\
        .stdin("1")\
        .stdout("Your BAC is 0.35\nIt is not legal for you to drive.", regex=True)\
        .exit(0)

@check50.check(exists)
def test_non_numeric_input():
    """Handles non-numeric input gracefully"""
    check50.run("python3 blood.py")\
        .stdin("one hundred eighty")\
        .reject()\
        .stdin("180")\
        .stdin("male")\
        .stdin("two")\
        .reject()\
        .stdin("2")\
        .stdin("5")\
        .stdin("two")\
        .reject()\
        .stdin("2")\
        .stdout("Your BAC is 0.18", regex=True)\
        .exit(0)

def regex(output):
    """match case-insensitively with only whitespace on either side"""
    return fr'^\s*{escape(output)}\s*$'
