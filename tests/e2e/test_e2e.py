# tests/e2e/test_e2e.py

import pytest

@pytest.mark.e2e
def test_hello_world(page, fastapi_server):
    """
    Test that the homepage displays 'Hello World'.
    This confirms the server is running and serving the template correctly.
    """
    # Navigate to the homepage
    page.goto('http://localhost:8000')
    
    # Check that the h1 tag contains "Hello World"
    assert page.inner_text('h1') == 'Hello World'

@pytest.mark.e2e
def test_calculator_add(page, fastapi_server):
    """
    Test the addition functionality through the browser.
    Simulates a user filling in numbers and clicking the Add button.
    """
    # Go to the homepage
    page.goto('http://localhost:8000')
    
    # Fill in the input fields
    page.fill('#a', '10')
    page.fill('#b', '5')
    
    # Click the Add button
    page.click('button:text("Add")')
    
    # Wait for the result to appear (with timeout of 5 seconds)
    page.wait_for_function(
        "document.getElementById('result').innerText !== ''",
        timeout=5000
    )
    
    # Check that the result is displayed correctly
    assert page.inner_text('#result') == 'Calculation Result: 15'

@pytest.mark.e2e
def test_calculator_divide_by_zero(page, fastapi_server):
    """
    Test that dividing by zero shows the correct error message.
    """
    # Go to the homepage
    page.goto('http://localhost:8000')
    
    # Fill in the input fields - attempting to divide by zero
    page.fill('#a', '10')
    page.fill('#b', '0')
    
    # Click the Divide button
    page.click('button:text("Divide")')
    
    # Wait for the error message to appear
    page.wait_for_function(
        "document.getElementById('result').innerText !== ''",
        timeout=5000
    )
    
    # Check that the error message is displayed
    assert page.inner_text('#result') == 'Error: Cannot divide by zero!'