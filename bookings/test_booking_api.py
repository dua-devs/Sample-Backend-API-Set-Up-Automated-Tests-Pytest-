import pytest

pytestmark = pytest.mark.django_db


def test_create_booking_success(client):
    payload = {
        "user_id": 1,
        "flight_id": 10,
        "seats": 2,
        "travel_date": "2026-02-20",
    }

    response = client.post("/api/bookings/", data=payload, content_type="application/json")

    assert response.status_code == 201
    data = response.json()
    assert data["user_id"] == 1
    assert data["flight_id"] == 10
    assert data["seats"] == 2
    assert "id" in data


def test_fetch_bookings_returns_list(client):
    response = client.get("/api/bookings/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_availability_missing_params(client):
    response = client.get("/api/availability/")
    assert response.status_code == 400
