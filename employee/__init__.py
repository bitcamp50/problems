import check50

@check50.check()
def exists():
    """employee.py exists"""
    check50.exists("employee.py")

@check50.check(exists)
def remove_employee():
    """removes an employee correctly"""
    initial_employees = ["John Smith", "Jackie Jackson", "Chris Jones", "Amanda Cullen", "Jeremy Goodwin"]
    name_to_remove = "Chris Jones"
    remaining_employees = [employee for employee in initial_employees if employee != name_to_remove]
    output = check50.run("python3 employee.py").stdin(name_to_remove).stdout()
    for employee in remaining_employees:
        if employee not in output:
            raise check50.Failure(f"Expected to find {employee} in the list after removal.")
    if name_to_remove in output:
        raise check50.Failure(f"Did not expect to find {name_to_remove} in the list after removal.")

@check50.check(exists)
def retains_others_after_removal():
    """retains other employees after one is removed"""
    name_to_remove = "Chris Jones"
    output = check50.run("python3 employee.py").stdin(name_to_remove).stdout()
    if "There are 4 employees:" not in output:
        raise check50.Failure("Expected to find 'There are 4 employees:' after removing one employee.")

@check50.check(exists)
def handles_nonexistent_employee():
    """behaves correctly when attempting to remove a non-existent employee"""
    nonexistent_name = "Nonexistent Name"
    output = check50.run("python3 employee.py").stdin(nonexistent_name).stdout()
    if "Nonexistent Name" in output:
        raise check50.Failure("Program should not output the non-existent employee name in the final list.")
