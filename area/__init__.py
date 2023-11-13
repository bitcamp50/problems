import check50

@check50.check()
def exists():
    """area.py exists"""
    check50.exists("area.py")

@check50.check(exists)
def test_15_20():
    """input of 15 and 20 yields output \"You entered dimensions of 15 feet by 20 feet.\", \"The area is\", \"300 square feet\" and \"27.871 square meters\""""
    check50.run("python3 area.py").stdin("15").stdin("20").stdout("You entered dimensions of 15 feet by 20 feet.").stdout("The area is").stdout("300 square feet").stdout("27.871 square meters").exit(0)

@check50.check(exists)
def test_10_25():
    """input of 10 and 25 yields output \"You entered dimensions of 10 feet by 25 feet.\", \"The area is\", \"300 square feet\" and \"27.871 square meters\""""
    check50.run("python3 area.py").stdin("10").stdin("25").stdout("You entered dimensions of 10 feet by 25 feet.").stdout("The area is").stdout("250 square feet").stdout("23.226 square meters").exit(0)
    
@check50.check(exists)
def test_str():
    """input of \"three\" and \"four\" results in ValueError"""
    check50.run("python3 area.py").stdin("three").stdin("four").exit(1)

@check50.check(exists)
def test_float():
    """input of \"25.5\" and \"65.5\" results in ValueError"""
    check50.run("python3 area.py").stdin("25.5").stdin("65.5").exit(1)