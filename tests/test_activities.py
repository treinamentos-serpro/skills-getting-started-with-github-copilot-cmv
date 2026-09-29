def test_get_activities_returns_seed_data(client):
    # Arrange
    # (no setup needed, activities are seeded by the reset_activities fixture)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    chess_club = data["Chess Club"]
    assert chess_club["description"] == "Learn strategies and compete in chess tournaments"
    assert chess_club["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
    assert chess_club["max_participants"] == 12
    assert "michael@mergington.edu" in chess_club["participants"]
