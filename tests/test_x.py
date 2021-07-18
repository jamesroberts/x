
def test_get(client):
    response = client.get('/get')
    assert response.status_code == 200
    assert response.get_data() is not None


def test_post(client):
    response = client.post('/post', data={"test": "data"})
    assert response.status_code == 200
    assert response.get_data() is not None
