import check50

@check50.check()
def exists():
    """anagram.py exists"""
    check50.exists("anagram.py")

@check50.check(exists)
def test_anagrams():
    """Correctly identifies anagrams"""
    check50.run("python3 anagram.py")\
        .stdin("note")\
        .stdin("tone")\
        .stdout("\"note\" and \"tone\" are anagrams.")\
        .exit(0)

@check50.check(exists)
def test_non_anagrams():
    """Correctly identifies non-anagrams"""
    check50.run("python3 anagram.py")\
        .stdin("hello")\
        .stdin("world")\
        .stdout(".*are not anagrams.", regex=True)\
        .exit(0)

@check50.check(exists)
def test_different_lengths():
    """Identifies strings of different lengths as not anagrams"""
    check50.run("python3 anagram.py")\
        .stdin("hello")\
        .stdin("worldly")\
        .stdout(".*are not anagrams.", regex=True)\
        .exit(0)

@check50.check(exists)
def test_same_word():
    """Identifies the same word as an anagram"""
    check50.run("python3 anagram.py")\
        .stdin("test")\
        .stdin("test")\
        .stdout("\"test\" and \"test\" are anagrams.")\
        .exit(0)

@check50.check(exists)
def test_case_insensitive():
    """Identifies anagrams regardless of case"""
    check50.run("python3 anagram.py")\
        .stdin("Tone")\
        .stdin("Note")\
        .stdout("\"tone\" and \"note\" are anagrams.", regex=True)\
        .exit(0)
