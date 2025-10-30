# tests/e2e/conftest.py

import subprocess
import time
import pytest
from playwright.sync_api import sync_playwright
import requests

@pytest.fixture(scope='session')
def fastapi_server():
    """
    Starts the FastAPI server before running E2E tests.
    Stops it after all tests are done.
    """
    # Start the FastAPI application
    fastapi_process = subprocess.Popen(['python3', 'main.py'])
    
    server_url = 'http://127.0.0.1:8000/'
    timeout = 30  # Wait up to 30 seconds for server to start
    start_time = time.time()
    server_up = False
    
    print("Starting FastAPI server...")
    
    # Keep checking if the server is ready
    while time.time() - start_time < timeout:
        try:
            response = requests.get(server_url)
            if response.status_code == 200:
                server_up = True
                print("FastAPI server is up and running.")
                break
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(1)
    
    if not server_up:
        fastapi_process.terminate()
        raise RuntimeError("FastAPI server failed to start within timeout period.")
    
    yield
    
    # Shut down the server after tests complete
    print("Shutting down FastAPI server...")
    fastapi_process.terminate()
    fastapi_process.wait()
    print("FastAPI server has been terminated.")

@pytest.fixture(scope="session")
def playwright_instance_fixture():
    """
    Manages the Playwright instance lifecycle.
    """
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance_fixture):
    """
    Launches a browser for testing.
    """
    browser = playwright_instance_fixture.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    """
    Creates a new browser page for each test.
    """
    page = browser.new_page()
    yield page
    page.close()