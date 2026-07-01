def get_token(client):

    client.post(
        "/auth/register",
        json={
            "username":"employee",
            "password":"12345",
            "role":"Employee"
        }
    )


    response = client.post(
        "/auth/login",
        json={
            "username":"employee",
            "password":"12345"
        }
    )


    return response.json()["access_token"]



def test_create_booking(client):

    token = get_token(client)


    response = client.post(
        "/bookings/",
        headers={
            "Authorization":f"Bearer {token}"
        },
        json={
            "room_id":1,
            "booking_date":"2026-07-01",
            "start_time":"10:00:00",
            "end_time":"11:00:00"
        }
    )


    assert response.status_code == 200



def test_get_bookings(client):

    token=get_token(client)


    response=client.get(
        "/bookings/",
        headers={
            "Authorization":f"Bearer {token}"
        }
    )


    assert response.status_code == 200