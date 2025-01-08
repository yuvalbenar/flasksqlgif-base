# test.py
import pytest
import requests
import os

@pytest.fixture
def base_url():
    # Get the base URL from the environment, default to flaskgif:5000
    return os.getenv("FLASK_APP_URL", "http://flaskgif:5000")

def test_flask_app(base_url):
    response = requests.get(base_url)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    # Optionally test the content
    assert "Expected Content" in response.text, "Response does not contain expected content"
