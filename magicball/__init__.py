import check50

@check50.check()
def exists():
    """magicball.py exists"""
    check50.exists("magicball.py")
    check50.include("testing.py")

@check50.check(exists)
def test_valid_input_question():
    """Handles question input with '?' character"""
    check50.run("python3 testing.py")\
        .stdin("Will I be rich and famous?")\
        .stdout("Yes", regex=False)\
        .exit(0)

@check50.check(exists)
def test_invalid_input_question():
    """Handles question input without '?' character"""
    question = "I will not rich"
    check = check50.run("python3 magicball.py")
    check.stdin(question)
    while True:
        output = check.stdout()
        if "This is not a question" in output:
            check.stdin("Will I be rich and famous?\n")
        elif "Yes" in output:
            break
        else:
            raise check50.Failure("Unexpected output: {}".format(output))
        

