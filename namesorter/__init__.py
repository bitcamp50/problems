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