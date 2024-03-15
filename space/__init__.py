import check50

@check50.check()
def exists():
    """space.py exists"""
    check50.exists("space.py")

@check50.check(exists)
def test_json_response():
    """space.py makes a successful request and parses JSON response"""
    result = check50.run("python3 space.py").stdout("API request successful").stdout("JSON parsing successful").exit(0)

@check50.check(exists)
def test_output_format():
    """space.py prints the correct output format"""
    result = check50.run("python3 space.py").stdout("{:<20}| {:<20}".format("name", "craft")).stdout("-" * 30)

    # Add more specific checks for names and crafts
    result.stdout("Jasmin Moghbeli").stdout("ISS")
    result.stdout("Andreas Mogensen").stdout("ISS")
    result.stdout("Satoshi Furukawa").stdout("ISS")
    # Add more names and crafts as needed

    result.exit(0)