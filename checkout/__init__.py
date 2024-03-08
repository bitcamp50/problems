import check50

@check50.check()
def exists():
    """Test if checkout.py exists."""
    check50.exists("checkout.py")


@check50.check(exists)
def test_subtotal():
    """Test if tax is calculated correctly."""
    check50.run("python3 checkout.py")\
        .stdin("1")\
        .stdin("1")\
        .stdin("2")\
        .stdin("3")\
        .stdin("4")\
        .stdin("5")\
        .stdout("Subtotal: $27.00\nTax: $1.49\nTotal: $28.48", regex=True)\
        .exit(0)
    
    
# @check50.check(exists)
# def test_tax():
#     """Test if tax is calculated correctly."""
#     check50.run("python checkout.py", input="25 2 10 1 4 1", capture_output=True)
#     output = check50.get_output()
    
#     expected_tax = "$3.52"
#     assert expected_tax in output, f"Missing or incorrect tax. Expected: {expected_tax}"


# @check50.check(exists)
# def test_total():
#     """Test if total is calculated correctly."""
#     check50.run("python checkout.py", input="25 2 10 1 4 1", capture_output=True)
#     output = check50.get_output()
    
#     expected_total = "$67.52"
#     assert expected_total in output, f"Missing or incorrect total. Expected: {expected_total}"



# @check50.check(exists)
# def test_formatting():
#     """Test if output is formatted correctly."""
#     check50.run("python checkout.py", input="25 2 10 1 4 1", capture_output=True)
#     output = check50.get_output()
    
#     for line in output.splitlines():
#         if line.startswith("Enter"):
#             continue
        
#         parts = line.split()
#         assert len(parts) == 3, f"Incorrect line format: {line}"
        
#         assert parts[0].isdigit() and parts[1].isdigit(), f"Invalid quantity or price format: {line}"