# from app import get_message, login


# def test_get_message():
#     assert get_message() == "Hello from DevOps!"


# def test_login():
#     assert login("Saket") == "Welcome, Saket!"


# def test_login_rejects_empty_username():
#     try:
#         login("")
#     except ValueError as error:
#         assert str(error) == "Username is required"
#     else:
#         assert False, "Expected ValueError"

from app import app
def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["status"] == "Hello from Azure Container App!"

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"
