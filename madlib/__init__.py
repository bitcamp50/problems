import check50
from re import escape

@check50.check()
def exists():
    """madlib.py exists"""
    check50.exists("madlib.py")

@check50.check(exists)
def test_basic_story():
    """creates a basic story with noun, verb, adjective, and adverb"""
    (check50.run("python3 madlib.py")
            .stdin("dog")
            .stdin("walk")
            .stdin("blue")
            .stdin("quickly")
            .stdout("Do you walk your blue dog quickly\? That's hilarious!")
            .exit())

@check50.check(exists)
def test_different_story():
    """creates a different story with another set of inputs"""
    (check50.run("python3 madlib.py")
            .stdin("cat")
            .stdin("jump")
            .stdin("green")
            .stdin("slowly")
            .stdout("Do you jump your green cat slowly\? That's hilarious!")
            .exit())

@check50.check(exists)
def test_edge_case_empty_input():
    """handles empty input for noun, verb, adjective, and adverb"""
    expected_output = r"Do you\s*your\s*\s*\s*\? That's hilarious!"
    (check50.run("python3 madlib.py")
            .stdin("")
            .stdin("")
            .stdin("")
            .stdin("")
            .stdout(expected_output, regex=True)
            .exit())

@check50.check(exists)
def test_numerical_input():
    """handles numerical input for noun, verb, adjective, and adverb"""
    expected_output = r"Do you 456 your 789 123 0\? That's hilarious!"
    (check50.run("python3 madlib.py")
            .stdin("123")
            .stdin("456")
            .stdin("789")
            .stdin("0")
            .stdout(expected_output, regex=True)
            .exit())

def regex(output):
    """match case-insensitively with only whitespace on either side"""
    return fr'^\s*{escape(output)}\s*$'