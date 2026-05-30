import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_generate_testcases(client):
    response = client.post('/generate-testcases',
        data=json.dumps({
            'module': 'Login Page',
            'fields': 'Email, Password, Submit button'
        }),
        content_type='application/json'
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'result' in data
    assert len(data['result']) > 0

def test_generate_bugreport(client):
    response = client.post('/generate-bugreport',
        data=json.dumps({
            'description': 'Login button not working',
            'module': 'Login'
        }),
        content_type='application/json'
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'result' in data
    assert len(data['result']) > 0

def test_generate_testdata(client):
    response = client.post('/generate-testdata',
        data=json.dumps({
            'field_type': 'Email field'
        }),
        content_type='application/json'
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'result' in data
    assert len(data['result']) > 0

def test_empty_module(client):
    response = client.post('/generate-testcases',
        data=json.dumps({
            'module': '',
            'fields': ''
        }),
        content_type='application/json'
    )
    assert response.status_code == 200