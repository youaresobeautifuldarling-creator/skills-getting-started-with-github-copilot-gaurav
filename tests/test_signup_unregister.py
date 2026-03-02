from urllib.parse import quote


def test_signup_success(client):
    # Arrange
    activity = "Chess Club"
    activity_path = quote(activity, safe="")
    email = "testuser@example.com"

    # Act
    resp = client.post(f"/activities/{activity_path}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    body = resp.json()
    assert "Signed up" in body.get("message", "")

    # Verify participant is listed
    activities = client.get("/activities").json()
    assert email in activities[activity]["participants"]


def test_duplicate_signup_rejected(client):
    # Arrange
    activity = "Tennis Club"
    activity_path = quote(activity, safe="")
    email = "duplicate@example.com"

    # Act - first signup should succeed
    first = client.post(f"/activities/{activity_path}/signup", params={"email": email})
    assert first.status_code == 200

    # Act - second signup should be rejected
    second = client.post(f"/activities/{activity_path}/signup", params={"email": email})

    # Assert
    assert second.status_code == 400


def test_unregister_success_and_not_found(client):
    # Arrange - sign up a test user then remove them
    activity = "Drama Club"
    activity_path = quote(activity, safe="")
    email = "remove_me@example.com"

    signup = client.post(f"/activities/{activity_path}/signup", params={"email": email})
    assert signup.status_code == 200

    # Act - unregister
    delete = client.delete(f"/activities/{activity_path}/signup", params={"email": email})

    # Assert - successful removal
    assert delete.status_code == 200
    assert "Removed" in delete.json().get("message", "")

    # Act - attempt to remove again
    delete_again = client.delete(f"/activities/{activity_path}/signup", params={"email": email})

    # Assert - now not found
    assert delete_again.status_code == 404
