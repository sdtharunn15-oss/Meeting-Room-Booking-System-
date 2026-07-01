def test_register(client):

    response = client.post(
        "/auth/register",
        json={
            "username":"testuser",
            "password":"12345",
            "role":"Admin"
        }
    )

    assert response.status_code == 200



def test_login(client):

    response = client.post(
        "/auth/login",
        json={
            "username":"testuser",
            "password":"12345"
        }
    )

    assert response.status_code == 200

    assert response.json()["message"] == "Login successful"