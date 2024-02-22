import check50
import re

@check50.check()
def exists():
    """employee.py exists"""
    check50.exists("employee.py")

@check50.check(exists)
def remove_employee():
    """employee name can be removed"""
    check50.run("python3 employee.py").stdin("Chris Jones").stdout(not_contains("Chris Jones"), "Chris Jones was correctly removed.").exit(0)

@check50.check(remove_employee)
def retains_others():
    """retains other employees after removal"""
    output = check50.run("python3 employee.py").stdin("Chris Jones").stdout()
    required_employees = ["John Smith", "Jackie Jackson", "Amanda Cullen", "Jeremy Goodwin"]
    for employee in required_employees:
        if employee not in output:
            raise check50.Failure(f"missing {employee} in the output after removal")

@check50.check(exists)
def reject_nonexistent_employee():
    """handles removal of a name not in the list"""
    initial_output = check50.run("python3 employee.py").stdout()
    modified_output = check50.run("python3 employee.py").stdin("Nonexistent Name").stdout()
    if initial_output == modified_output:
        raise check50.Failure("Program does not handle non-existent employee names correctly")

def not_contains(name):
    """Returns a function that checks if the output does not contain the given name"""
    def check(output):
        if name in output:
            raise check50.Mismatch("", name, help=f"{name} should not be in the output.")
    return check
