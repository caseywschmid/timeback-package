import pytest

from timeback.services.oneroster.rostering.endpoints.get_agent_for import get_agent_for
from timeback.models.response import TimebackGetAgentForResponse


class MockHttpClient:
    def __init__(self, response_data):
        self.response_data = response_data
        self.last_path = None

    def get(self, path, params=None):
        self.last_path = path
        return self.response_data


def minimal_user(idx: str):
    return {
        "sourcedId": f"u{idx}",
        "enabledUser": True,
        "givenName": "A",
        "familyName": "B",
        "roles": [
            {"role": "student", "roleType": "primary", "org": {"sourcedId": "org1", "type": "org"}}
        ],
        "agents": [],
        "userProfiles": [],
        "email": f"u{idx}@example.com",
        "status": "active",
    }


def test_get_agent_for_success():
    mock_http = MockHttpClient(
        {
            "users": [minimal_user("1"), minimal_user("2")],
        }
    )

    resp = get_agent_for(mock_http, "parent-user-id")

    assert isinstance(resp, TimebackGetAgentForResponse)
    assert len(resp.users) == 2
    assert resp.users[0].sourcedId == "u1"
    assert resp.users[1].sourcedId == "u2"
    assert mock_http.last_path == "/ims/oneroster/rostering/v1p2/users/parent-user-id/agentFor"


def test_get_agent_for_empty_list():
    mock_http = MockHttpClient(
        {
            "users": [],
        }
    )

    resp = get_agent_for(mock_http, "user-with-no-agents")

    assert isinstance(resp, TimebackGetAgentForResponse)
    assert len(resp.users) == 0

