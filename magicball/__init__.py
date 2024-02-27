import check50

@check50.check()
def exists():
    """magicball.py exists"""
    check50.exists("magicball.py")
    check50.include("testing.py")

@check50.check(exists)
def test_valid_input_question_Y():
    """Handles question input with '?' character and answer Yes"""
    check50.run("python3 testing.py")\
        .stdin("Will I be rich and famous?")\
        .stdout("Yes", regex=False)\
        .exit(0)

@check50.check(exists)
def test_valid_input_question_N():
    """Handles question input with '?' character and answer No"""
    check50.run("python3 testing2.py")\
        .stdin("Will I be famous?")\
        .stdout("No", regex=False)\
        .exit(0)

@check50.check(exists)
def test_valid_input_question_N():
    """Handles question input with '?' character and answer Ask again later"""
    check50.run("python3 testing3.py")\
        .stdin("Will I be famous?")\
        .stdout("Ask again later", regex=False)\
        .exit(0)
    
@check50.check(exists)
def test_invalid_input_question():
    """Handles question input without '?' character"""
    question = "I will not rich\n"
    check = check50.run("python3 testing.py")
    check.stdin(question)
    check.stdout("This is not a question")
    check.stdin("Will I be rich and famous?\n")
    check.stdout("Yes")
    check.exit(0)

@check50.check(exists)
def test_invalid_input_question():
    """Handles question with blank input"""
    question = "\n"
    check = check50.run("python3 testing.py")
    check.stdin(question)
    check.stdout("This is not a question")
    check.stdin("Will I be rich and famous?\n")
    check.stdout("Yes")
    check.exit(0)
        

