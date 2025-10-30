# tests/integration/test_fastapi_calculator.py

import pytest
from fastapi.testclient import TestClient
from main import app

# ---------------------------------------------
# Fixture to create a test client
# ---------------------------------------------

@pytest.fixture
def client():
    """
    Creates a test client for making requests to the FastAPI app.
    This simulates API calls without actually running a server.
    """
    with TestClient(app) as client:
        yield client

# ---------------------------------------------
# Test Addition Endpoint
# ---------------------------------------------

def test_add_api(client):
    """
    Test that the /add endpoint correctly adds two numbers.
    """
    response = client.post('/add', json={'a': 10, 'b': 5})
    
    # Check that we got a successful response
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Check that the result is correct
    assert response.json()['result'] == 15, f"Expected result 15, got {response.json()['result']}"

# ---------------------------------------------
# Test Subtraction Endpoint
# ---------------------------------------------

def test_subtract_api(client):
    """
    Test that the /subtract endpoint correctly subtracts two numbers.
    """
    response = client.post('/subtract', json={'a': 10, 'b': 5})
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()['result'] == 5, f"Expected result 5, got {response.json()['result']}"

# ---------------------------------------------
# Test Multiplication Endpoint
# ---------------------------------------------

def test_multiply_api(client):
    """
    Test that the /multiply endpoint correctly multiplies two numbers.
    """
    response = client.post('/multiply', json={'a': 10, 'b': 5})
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()['result'] == 50, f"Expected result 50, got {response.json()['result']}"

# ---------------------------------------------
# Test Division Endpoint
# ---------------------------------------------

def test_divide_api(client):
    """
    Test that the /divide endpoint correctly divides two numbers.
    """
    response = client.post('/divide', json={'a': 10, 'b': 2})
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()['result'] == 5, f"Expected result 5, got {response.json()['result']}"

# ---------------------------------------------
# Test Division by Zero
# ---------------------------------------------

def test_divide_by_zero_api(client):
    """
    Test that the /divide endpoint properly handles division by zero.
    Should return a 400 error with an appropriate message.
    """
    response = client.post('/divide', json={'a': 10, 'b': 0})
    
    # Should get a 400 Bad Request error
    assert response.status_code == 400, f"Expected status code 400, got {response.status_code}"
    
    # Check that the error field exists
    assert 'error' in response.json(), "Response JSON does not contain 'error' field"
    
    # Check that the error message is correct
    assert "Cannot divide by zero!" in response.json()['error'], \
        f"Expected error message 'Cannot divide by zero!', got '{response.json()['error']}'"