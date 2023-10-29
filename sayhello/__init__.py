import check50


@check50.check()
def exists():
    """sayhello.py exists არსებობს"""
    check50.exists("sayhello.py")

@check50.check(exists)
def testhello():
    """input of HELLO yields output of hello"""
    check50.run("python3 sayhello.py").stdin("HELLO", prompt=False).stdout("hello").exit()

@check50.check(exists)
def testcs50():
    """პირველი სატესტო შეტყობინება ქართულად"""
    check50.run("python3 sayhello.py").stdin("THIS IS CS50", prompt=False).stdout("this is cs50").exit()

@check50.check(exists)
def testnumber():
    """input of 50 yields output of 50"""
    check50.run("python3 sayhello.py").stdin("50", prompt=False).stdout("50").exit()