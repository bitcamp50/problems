import check50
import check50_custom_js as custom_js

@check50.check()
def exists():
    """hello.js exists."""
    check50.exists("hello.js")

@check50.check(exists)
def prints_hello():
    """prints "hello, world\n" """
    from re import match

    # Using the custom_js interface to execute the JavaScript file
    with custom_js.capture_stdout() as stdout:
        custom_js.interface("hello.js")

    actual = stdout.getvalue()
    expected = "[Hh]ello, world!?\n"
    if not match(expected, actual):
        help = None
        if match(expected[:-1], actual):
            help = r"did you forget a newline ('\n') at the end of your printf string?"
        raise check50.Mismatch("hello, world\n", actual, help=help)
