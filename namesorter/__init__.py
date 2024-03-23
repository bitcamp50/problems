import check50

@check50.check()
def exists():
    """namesorter.py exists"""
    check50.exists("namesorter.py")

@check50.check(exists)
def test_sorted_output():
    """namesorter.py creates correctly sorted output"""
    check50.run("python3 namesorter.py").exit(1)
    correct_output = ["Total of 7 names", "-----------------", "Johnson, Jim", "Jones, Aaron", "Jones, Chris", "Ling, Mai", "Swift, Geoffrey", "Xiong, Fong", "Zarnecki, Sabrina"]
    with open("sorted_names.txt", "r") as file:
        lines = file.readlines()
    if lines != correct_output:
        raise check50.Failure(f"Expected sorted_names.txt to contain sorted names with correct format but got {lines}.")

@check50.check(exists)
def test_correct_total_count():
    """namesorter.py correctly counts total number of names"""
    check50.include("names_unsorted.txt")
    check50.run("python3 namesorter.py names_unsorted.txt").exit(0)
    check50.exists("sorted_names.txt")
    output = check50.read("sorted_names.txt").strip().split("\n")
    
    # The first line should contain the total count of names in the format "Total of X names"
    expected_count = 7  # Change this based on the number of names in names_unsorted.txt
    total_line = output[0]
    expected_line = f"Total of {expected_count} names"
    
    if total_line != expected_line:
        raise check50.Failure(f"Expected the first line to be '{expected_line}', but got '{total_line}'.")

@check50.check(exists)
def test_empty_file():
    """namesorter.py handles empty input file correctly"""
    check50.include("empty.txt")
    check50.run("python3 namesorter.py empty.txt").exit(0)
    check50.exists("sorted_names.txt")
    correct_output = ["Total of 0 names", "-----------------"]
    output = check50.read("sorted_names.txt").strip().split("\n")
    if output != correct_output:
        raise check50.Failure("Expected sorted_names.txt to indicate no names but found otherwise.")
