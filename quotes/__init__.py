import check50

@check50.check()
def exists():
    """quotes.py exists"""
    check50.exists("quotes.py")

@check50.check(exists)
def test_obi_wan():
    """input of \"These aren't the droids you're looking for.\" and \"Obi-Wan Kenobi\" yields output \"Obi-Wan Kenobi says, 'These aren't the droids you're looking for.'\""""
    
    check50.run("python3 quotes.py").stdin("These aren't the droids you're looking for.").stdin("Obi-Wan Kenobi").stdout("Obi-Wan Kenobi says, 'These aren't the droids you're looking for.'").exit(0)

@check50.check(exists)
def test_linus_torvalds():
    """input of \"Talk is cheap. Show me the code.\" and \"Linus Torvalds\" yields output \"Linus Torvalds says, 'Talk is cheap. Show me the code.'\""""
    
    check50.run("python3 quotes.py").stdin("Talk is cheap. Show me the code.").stdin("Linus Torvalds").stdout("Linus Torvalds says, 'Talk is cheap. Show me the code.'").exit(0)

@check50.check(exists)
def test_john_johnson():
    """input of \"First, solve the problem. Then, write the code.\" and \"John Johnson\" yields output \"\""""
    
    check50.run("python3 quotes.py").stdin("First, solve the problem. Then, write the code.").stdin("John Johnson").stdout("John Johnson says, 'First, solve the problem. Then, write the code.'").exit(0)

@check50.check(exists)
def test_kent_beck():
    """input of \"Make it work, make it right, make it fast.\" and \"Kent Beck\" yields output \"Kent Beck says, 'Make it work, make it right, make it fast.'\""""
    
    check50.run("python3 quotes.py").stdin("Make it work, make it right, make it fast.").stdin("Kent Beck").stdout("Kent Beck says, 'Make it work, make it right, make it fast.'").exit(0)