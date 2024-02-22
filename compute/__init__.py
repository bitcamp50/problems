import check50
import re

@check50.check()
def exists():
    """stats.py exists"""
    check50.exists("stats.py")

@check50.check(exists)
def test_fixed_set():
    """calculates stats correctly for a fixed set of numbers"""
    input_numbers = ["100", "200", "1000", "300"]
    output = (check50.run("python3 stats.py")
              .stdin("100").stdin("200").stdin("1000").stdin("300").stdin("done")
              .stdout())
    # Verify the output contains the numbers
    verify_output(output, input_numbers, 400.0, 100, 1000, 400.25)
    output.exit(0)

@check50.check(exists)
def test_single_number():
    """calculates stats correctly for a single number"""
    input_numbers = ["500"]
    output = (check50.run("python3 stats.py")
              .stdin("500").stdin("done")
              .stdout())
    # When there's only one number, the std deviation is 0
    verify_output(output, input_numbers, 500, 500, 500, 0)
    output.exit(0)

@check50.check(exists)
def test_two_numbers():
    """calculates stats correctly for two numbers"""
    input_numbers = ["100", "400"]
    output = (check50.run("python3 stats.py")
              .stdin("100").stdin("400").stdin("done")
              .stdout())
    # Verify output for two numbers
    verify_output(output, input_numbers, 250, 100, 400, 150)
    output.exit(0)

def verify_output(output, numbers, mean, minimum, maximum, stddev):
    numbers_str = ", ".join(numbers)
    if not re.search(f"Numbers: {numbers_str}", output):
        raise check50.Failure(f"Expected output to list numbers: {numbers_str}")
    if not re.search(f"The average is {mean}.", output):
        raise check50.Failure(f"Expected correct average calculation: {mean}")
    if not re.search(f"The minimum is {minimum}.", output):
        raise check50.Failure(f"Expected correct minimum calculation: {minimum}")
    if not re.search(f"The maximum is {maximum}.", output):
        raise check50.Failure(f"Expected correct maximum calculation: {maximum}")
    if not re.search(f"The standard deviation is {stddev}.", output, re.DOTALL):
        raise check50.Failure(f"Expected correct standard deviation calculation: {stddev}")
