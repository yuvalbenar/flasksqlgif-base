import pytest
import requests

def test_flask_app():
    base_url = 'http://flaskgif:5000'  # Flask app inside Docker
    response = requests.get(base_url)
   # assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
