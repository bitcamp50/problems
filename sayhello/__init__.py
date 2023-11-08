import check50


@check50.check()
def exists():
    """sayhello.py exists"""
    check50.exists("sayhello.py")

@check50.check(exists)
def testoto():
    """input of Oto yields output of 'Hello, Oto, nice to meet you!'"""
    check50.run("python3 sayhello.py").stdin("Oto", prompt=True).stdout("Hello, Oto, nice to meet you!").exit()

@check50.check(exists)
def testgiorgi():
    """input of Giorgi yields output of 'Hello, Giorgi, nice to meet you!'"""
    check50.run("python3 sayhello.py").stdin("Giorgi", prompt=False).stdout("Hello, Giorgi, nice to meet you!").exit()

@check50.check(exists)
def testbitcamp():
    """input of Bitcamp yields output of 'Hello, Bitcamp, nice to meet you!'"""
    check50.run("python3 sayhello.py").stdin("Bitcamp", prompt=False).stdout("Hello, Bitcamp, nice to meet you!").exit()