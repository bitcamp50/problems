import check50

@check50.check()
def exists():
    """employee.py exists"""
    check50.exists("employee.py")

@check50.check(exists)
def remove_employee():
    """Chris Jones is removed from the list"""
    # Ensuring Chris Jones is not in the final output
    output = check50.run("python3 employee.py").stdin("Chris Jones").stdout()
    if "Chris Jones" in output:
        raise check50.Failure("Chris Jones should not be in the list after being removed.")

@check50.check(remove_employee)
def retains_others():
    """List correctly retains other employees after removal"""
    # Verifying other employees are still listed after removal
    output = check50.run("python3 employee.py").stdin("Chris Jones").stdout()
    required_employees = ["John Smith", "Jackie Jackson", "Amanda Cullen", "Jeremy Goodwin"]
    for employee in required_employees:
        if employee not in output:
            raise check50.Failure(f"{employee} is missing from the list after removal.")

@check50.check(exists)
def reject_nonexistent_employee():
    """Program behaves correctly when attempting to remove a non-existent employee"""
    # Check if the list remains unchanged after attempting to remove a non-existent employee
    initial_output = check50.run("python3 employee.py").stdout()
    modified_output = check50.run("python3 employee.py").stdin("Nonexistent Name").stdout()
    if initial_output != modified_output:
        raise check50.Failure("The list should remain unchanged when a non-existent employee name is entered.")
