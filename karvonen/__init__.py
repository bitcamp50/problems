import check50

@check50.check()
def exists():
    """karvonen.py exists"""
    check50.exists("karvonen.py")

@check50.check(exists)
def test_valid_output():
    """produces correct heart rate table for valid inputs"""
    check50.run("python3 karvonen.py").stdin("65").stdin("22").stdout("Resting Pulse: 65\s+Age: 22\s*\nIntensity\s*\|\s*Rate\s*\n-+\s*\|-\+\s*\n55%\s*\|\s*138 bpm\s*\n60%\s*\|\s*145 bpm\s*\n65%\s*\|\s*151 bpm").exit(0)

@check50.check(exists)
def test_invalid_input():
    """rejects invalid inputs for age and resting heart rate"""
    check50.run("python3 karvonen.py").stdin("abc").reject().stdin("65").stdin("xyz").reject().stdin("22").stdout("Resting Pulse: 65\s+Age: 22\s*\nIntensity\s*\|\s*Rate\s*\n-+\s*\|-\+\s*\n55%\s*\|\s*138 bpm\s*\n60%\s*\|\s*145 bpm\s*\n65%\s*\|\s*151 bpm").exit(0)

@check50.check(exists)
def test_high_intensities():
    """correctly calculates target heart rates at high intensities"""
    check50.run("python3 karvonen.py").stdin("65").stdin("22").stdout("85%\s*\|\s*178 bpm\s*\n90%\s*\|\s*185 bpm\s*\n95%\s*\|\s*191 bpm").exit(0)
