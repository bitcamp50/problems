import check50

@check50.check()
def exists():
    """pizzaparty.py exists"""
    check50.exists("pizzaparty.py")

@check50.check(exists)
def test_even_distribution():
    """correctly calculates even distribution of pizza slices"""
    (check50.run("python3 pizzaparty.py")
            .stdin("8", prompt=False)
            .stdin("2", prompt=False)
            .stdin("8", prompt=False)
            .stdout("How many people\? 8\nHow many pizzas do you have\? 2\n8 people with 2 pizzas\nEach person gets 2 pieces of pizza.\nThere are 0 leftover pieces.")
            .exit(0))

@check50.check(exists)
def test_leftover_slices():
    """handles leftover slices correctly"""
    (check50.run("python3 pizzaparty.py")
            .stdin("5", prompt=False)
            .stdin("2", prompt=False)
            .stdin("6", prompt=False)
            .stdout("How many people\? 5\nHow many pizzas do you have\? 2\n5 people with 2 pizzas\nEach person gets 2 pieces of pizza.\nThere are 2 leftover pieces.")
            .exit(0))

@check50.check(exists)
def test_large_numbers():
    """handles large numbers correctly"""
    (check50.run("python3 pizzaparty.py")
            .stdin("100", prompt=False)
            .stdin("25", prompt=False)
            .stdin("8", prompt=False)
            .stdout("How many people\? 100\nHow many pizzas do you have\? 25\n100 people with 25 pizzas\nEach person gets 2 pieces of pizza.\nThere are 0 leftover pieces.")
            .exit(0))