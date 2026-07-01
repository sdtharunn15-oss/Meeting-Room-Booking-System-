def get_token(client):

    client.post(
        "/auth/register",
        json={
            "username":"admin",
            "password":"12345",
            "role":"Admin"
        }
    )


    response = client.post(
        "/auth/login",
        json={
            "username":"admin",
            "password":"12345"
        }
    )

    return response.json()["access_token"]



def test_create_room(client):

    token = get_token(client)


    response = client.post(
        "/rooms",
        headers={
            "Authorization":f"Bearer {token}"
        },
        json={
            "room_name":"Conference Room",
            "capacity":20,
            "floor":2,
            "amenities":"Projector"
        }
    )


    assert response.status_code == 200



def test_get_rooms(client):

    response = client.get("/rooms/")

    assert response.status_code == 200