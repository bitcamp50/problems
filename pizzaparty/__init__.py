import check50

@check50.check()
def exists():
    """pizzaparty.py exists"""
    check50.exists("pizzaparty.py")

@check50.check(exists)
def test_even_distribution():
    """correctly calculates even distribution of pizza slices"""
    (check50.run("python3 pizzaparty.py")
            .stdin("8")
            .stdin("2")
            .stdin("8")
            .stdout("Each person gets 2 pieces of pizza.\nThere are 0 leftover pieces.")
            .exit(0))

@check50.check(exists)
def test_leftover_slices():
    """handles leftover slices correctly"""
    (check50.run("python3 pizzaparty.py")
            .stdin("5")
            .stdin("2")
            .stdin("6")
            .stdout("Each person gets 2 pieces of pizza.\nThere are 2 leftover pieces.")
            .exit(0))

@check50.check(exists)
def test_large_group():
    """handles large group correctly"""
    (check50.run("python3 pizzaparty.py")
            .stdin("20")
            .stdin("8")
            .stdin("10")
            .stdout("Each person gets 4 pieces of pizza.\nThere are 0 leftover pieces.")
            .exit(0))

@check50.check(exists)
def test_single_pizza():
    """correctly handles a single pizza"""
    (check50.run("python3 pizzaparty.py")
            .stdin("3")
            .stdin("1")
            .stdin("8")
            .stdout("Each person gets 2 pieces of pizza.\nThere are 2 leftover pieces.")
            .exit(0))