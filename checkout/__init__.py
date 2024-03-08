import check50

from re import sub

@check50.check()
def exists():
    """Test if checkout.py exists."""
    check50.exists("test_checkout.py")

    check50.include("checkout.py")

@check50.check(exists)
def test_correct():
    """correct twttr.py passes all test_twttr checks"""
    test_implementation("correct_test", code=0)

@check50.check(exists)
def test_subtotal():
    """Test if values are calculated correctly."""
    check50.run("python3 checkout.py")\
        .stdin("1")\
        .stdin("1")\
        .stdin("2")\
        .stdin("3")\
        .stdin("4")\
        .stdin("5")\
        .stdout("Subtotal: $27.00\nTax: $1.49\nTotal: $28.48", regex=False)\
        .exit(0)

@check50.check(exists)
def test_subtotal_2():
    """Test if values are calculated correctly 2"""
    check50.run("python3 checkout.py")\
        .stdin("25")\
        .stdin("2")\
        .stdin("10")\
        .stdin("1")\
        .stdin("4")\
        .stdin("1")\
        .stdout("Subtotal: $64.00\nTax: $3.52\nTotal: $67.52", regex=False)\
        .exit(0)

@check50.check(exists)
def test_subtotal_3():
    """Test if values are calculated correctly 3"""
    check50.run("python3 checkout.py")\
        .stdin("16")\
        .stdin("4")\
        .stdin("3")\
        .stdin("54")\
        .stdin("1")\
        .stdin("2")\
        .stdout("Subtotal: $228.00\nTax: $12.54\nTotal: $240.54", regex=False)\
        .exit(0)



def test_implementation(filename, code=0):
    """test an implementation of checkout.py against student's checks in test_checkout.py, expect a given exit status"""

    check50.include(f"{filename}.py")

    patch_file(f"{filename}")

    return check50.run("pytest test_checkout.py").exit(code=code)

def patch_file(import_file):
    """patch a new version of calculate_total by updating import statement"""

    with open("checkout.py", "r") as f:
        checkout = sub(f"from \w* import calculate_total", f"from {import_file} import calculate_total", f.read())

    # Write new import statement to checkout.py
    with open("checkout.py", "w") as f:
        f.write(checkout)