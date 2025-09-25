from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_root():
    """
    Test the root endpoint to ensure it returns a 200 OK status and the correct JSON payload.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_item():
    """
    Test the /items/{item_id} endpoint with a valid item ID and a query parameter.
    """
    response = client.get("/items/42?q=testquery")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "testquery"}


def test_read_item_no_query():
    """
    Test the /items/{item_id} endpoint with a valid item ID but without the optional query parameter.
    """
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": None}


def test_read_item_invalid_id():
    """
    Test the /items/{item_id} endpoint with an invalid item ID to ensure it returns a 422 Unprocessable Entity error.
    """
    response = client.get("/items/foo")
    assert response.status_code == 422