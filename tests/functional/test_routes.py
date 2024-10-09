from iebank_api import app
import pytest

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country':'ES'})
    assert response.status_code == 200

def test_update_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts/1' page is posted to (PUT)
    THEN check the response is valid
    """
    response = testing_client.put('/accounts/1', json={'name': 'John Doe'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['name'] == 'Jane Doe'

def test_delete_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts/1' page is requested (DELETE)
    THEN check the response is valid
    """
    # First, create an account to delete
    response = testing_client.post('/accounts', json={'name': 'Mark Smith', 'currency': '€', 'country': 'ES'})
    assert response.status_code == 200
    account_id = response.get_json()['id']

    # Now delete the account
    delete_response = testing_client.delete(f'/accounts/{account_id}')
    assert delete_response.status_code == 200

    # Check that the account no longer exists
    get_response = testing_client.get(f'/accounts/{account_id}')
    assert get_response.status_code == 404

def test_create_account_invalid_input(testing_client):
    # Missing 'name' field
    response = testing_client.post('/accounts', json={'currency': '€', 'country': 'ES'})
    assert response.status_code == 400

def test_update_account_invalid_input(testing_client):
    # Invalid input for updating account (e.g., missing 'name')
    response = testing_client.put('/accounts/1', json={})
    assert response.status_code == 400

