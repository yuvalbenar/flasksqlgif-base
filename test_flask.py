# test.py
import pytest
import requests

def test_flask_app():
    url = "http://flaskgif:5000"
    response = requests.get(url)
    assert response.status_code == 200
