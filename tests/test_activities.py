from urllib.parse import quote


def test_get_activities(client):
    # Arrange: client fixture provides a fresh app with initial activities

    # Act
    resp = client.get("/activities")

    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "Programming Class" in data
    # Ensure participants key exists for a known activity
    assert "participants" in data["Chess Club"]
