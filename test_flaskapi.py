from manage import app

client = app.test_client()

def test_app():
    response = client.get('/')

    assert response.status_code == 200
    assert type(response.data) == bytes