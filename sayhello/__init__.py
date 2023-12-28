import check50
import check50_custom_js as custom_js

@check50.check()
def exists():
    """sayhello.js exists"""
    check50.exists("sayhello.js")

@check50.check(exists)
def function_defined():
    """Function 'createGreeting' is defined"""
    with custom_js.capture_stdout():
        inter = custom_js.interface("sayhello.js")
    custom_js.function_exists("createGreeting", inter)

@check50.check(function_defined)
def greets_by_name():
    """Program greets by name"""
    test_greeting("Alice", "Hello, Alice, nice to meet you!")
    test_greeting("Brian", "Hello, Brian, nice to meet you!")

def test_greeting(name, expected):
    inter = custom_js.interface("sayhello.js")
    result = inter.call("createGreeting", name).strip()
    if result != expected:
        raise check50.Mismatch(expected, result)
