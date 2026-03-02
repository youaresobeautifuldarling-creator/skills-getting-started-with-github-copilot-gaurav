import copy
import pytest
from fastapi.testclient import TestClient

import src.app as app_module


# Initial activities snapshot copied from src/app.py to reset state between tests
INITIAL_ACTIVITIES = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"],
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"],
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"],
    },
    "Basketball Club": {
        "description": "Play competitive basketball and improve your game skills",
        "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": [],
    },
    "Tennis Club": {
        "description": "Learn tennis techniques and participate in friendly matches",
        "schedule": "Tuesdays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": [],
    },
    "Drama Club": {
        "description": "Perform in plays and develop acting and theatrical skills",
        "schedule": "Wednesdays, 3:30 PM - 5:30 PM",
        "max_participants": 25,
        "participants": [],
    },
    "Art Club": {
        "description": "Explore painting, drawing, sculpture and other visual arts",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": [],
    },
    "Debate Club": {
        "description": "Develop public speaking and argumentation skills through competitive debates",
        "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
        "max_participants": 16,
        "participants": [],
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts through hands-on projects",
        "schedule": "Wednesdays, 3:30 PM - 4:45 PM",
        "max_participants": 18,
        "participants": [],
    },
}


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory activities mapping before each test."""
    app_module.activities = copy.deepcopy(INITIAL_ACTIVITIES)
    yield


@pytest.fixture
def client():
    """Provide a TestClient for the FastAPI app."""
    client = TestClient(app_module.app)
    return client
