import check50

@check50.check()
def exists():
    """Test if currency_converter.py exists."""
    check50.exists("currency_converter.py")


@check50.check(exists=True)
def test_prompts():
    """Test if program prompts for euros and exchange rate."""
    check50.run("python currency_converter.py", capture_output=True)
    output = check50.get_output()
    
    # Check if prompts for euros and exchange rate are present
    euro_prompt = "euros"
    rate_prompt = "exchange rate"
    assert euro_prompt in output, f"Missing prompt for euros."
    assert rate_prompt in output, f"Missing prompt for exchange rate."


@check50.check(exists=True)
def test_conversion():
    """Test if conversion is calculated correctly."""
    check50.run("python currency_converter.py", input="81 137.51", capture_output=True)
    output = check50.get_output()
    
    # Check if converted amount and exchange rate are present
    expected_amount = "$111.38"
    expected_rate = "137.51"
    assert expected_amount in output, f"Missing or incorrect converted amount."
    assert expected_rate in output, f"Missing or incorrect exchange rate."


@check50.check(exists=True)
def test_formatting():
    """Test if output is formatted correctly."""
    check50.run("python currency_converter.py", input="81 137.51", capture_output=True)
    output = check50.get_output()
    
    # Check if output mentions euros, U.S. dollars, and exchange rate
    euro_unit = "euros"
    usd_unit = "U.S. dollars"
    assert euro_unit in output, f"Output should mention euros."
    assert usd_unit in output, f"Output should mention U.S. dollars."
    assert "exchange rate" in output, f"Output should mention exchange rate."