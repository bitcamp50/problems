import check50

@check50.check()
def exists():
    """employee.py exists"""
    check50.exists("employee.py")

@check50.check(exists)
def test_remove_employee():
    """correctly removes an employee from the list"""
    check50.run("python3 employee.py").stdout("There are 5 employees:\s*John Smith\s*Jackie Jackson\s*Chris Jones\s*Amanda Cullen\s*Jeremy Goodwin\s*").stdin("Chris Jones").stdout("There are 4 employees:\s*John Smith\s*Jackie Jackson\s*Amanda Cullen\s*Jeremy Goodwin\s*").exit(0)

@check50.check(exists)
def test_remove_nonexistent_employee():
    """handles attempts to remove a nonexistent employee"""
    check50.run("python3 employee.py").stdout("There are 5 employees:").stdin("Giorgi").stdout("Employee Giorgi not found in the list.").exit(0)

@check50.check(exists)
def test_remove_all_employees():
    """allows all employees to be removed one by one"""
    program = check50.run("python3 employee.py")
    for employee in ["John Smith", "Jackie Jackson", "Chris Jones", "Amanda Cullen", "Jeremy Goodwin"]:
        program.stdout(employee, regex=False).stdin(employee)
    program.stdout("There are 0 employees:").exit(0)
