def test_get_activities_returns_expected_structure(client):
    # Arrange
    expected_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert len(payload) > 0

    first_activity = next(iter(payload.values()))
    assert expected_keys.issubset(first_activity.keys())


def test_get_activities_includes_seed_data(client):
    # Arrange
    activity_name = "Chess Club"

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert activity_name in payload
    assert "michael@mergington.edu" in payload[activity_name]["participants"]
