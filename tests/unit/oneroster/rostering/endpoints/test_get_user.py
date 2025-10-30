import pytest
from unittest.mock import Mock

from timeback.services.oneroster.rostering.endpoints.get_user import get_user
from timeback.services.oneroster.rostering.utils.parse_user_response import (
    parse_user_response,
)
from timeback.models.timeback_user import TimebackUser
from timeback.errors import ParseError


class MockHttpClient:
    def __init__(self, response_data):
        self.response_data = response_data
        self.last_params = None

    def get(self, path, params=None):
        self.last_params = params
        return self.response_data


def test_get_user_success():
    """Test successful user retrieval."""
    mock_http = MockHttpClient(
        {
            "user": {
                "sourcedId": "user123",
                "username": "jdoe",
                "givenName": "John",
                "familyName": "Doe",
                "enabledUser": True,
                "roles": [
                    {"role": "student", "roleType": "primary", "org": {"sourcedId": "org1", "type": "org"}}
                ],
                "agents": [],
                "userProfiles": [],
            }
        }
    )

    user = get_user(mock_http, "user123")

    assert isinstance(user, TimebackUser)
    assert user.sourcedId == "user123"
    assert user.username == "jdoe"


def test_get_user_with_fields_param():
    """Test that fields query param is passed as comma-separated string."""
    mock_http = MockHttpClient(
        {
            "user": {
                "sourcedId": "user123",
                "username": "jdoe",
                "givenName": "John",
                "familyName": "Doe",
                "enabledUser": True,
                "roles": [],
                "agents": [],
                "userProfiles": [],
            }
        }
    )

    user = get_user(mock_http, "user123", fields=["sourcedId", "username"]) 

    assert isinstance(user, TimebackUser)
    assert mock_http.last_params == {"fields": "sourcedId,username"}


def test_get_user_direct_response():
    """Test user retrieval when API returns user object directly."""
    mock_http = MockHttpClient(
        {
            "sourcedId": "user456",
            "username": "asmith",
            "givenName": "Alice",
            "familyName": "Smith",
            "enabledUser": True,
            "roles": [{"role": "teacher", "roleType": "primary", "org": {"sourcedId": "org2", "type": "org"}}],
            "agents": [],
            "userProfiles": [],
        }
    )

    user = get_user(mock_http, "user456")

    assert isinstance(user, TimebackUser)
    assert user.sourcedId == "user456"
    assert user.username == "asmith"


def test_parse_user_response_with_user_wrapper():
    """Test parsing response with user wrapper."""
    data = {
        "user": {
            "sourcedId": "user789",
            "username": "bwilson",
            "givenName": "Bob",
            "familyName": "Wilson",
            "enabledUser": True,
            "roles": [{"role": "student", "roleType": "primary", "org": {"sourcedId": "org3", "type": "org"}}],
            "agents": [],
            "userProfiles": [],
        }
    }

    user = parse_user_response(data)

    assert isinstance(user, TimebackUser)
    assert user.sourcedId == "user789"
    assert user.username == "bwilson"


def test_parse_user_response_direct():
    """Test parsing response without user wrapper."""
    data = {
        "sourcedId": "user999",
        "username": "cjohnson",
        "givenName": "Carl",
        "familyName": "Johnson",
        "enabledUser": True,
        "roles": [{"role": "teacher", "roleType": "primary", "org": {"sourcedId": "org4", "type": "org"}}],
        "agents": [],
        "userProfiles": [],
    }

    user = parse_user_response(data)

    assert isinstance(user, TimebackUser)
    assert user.sourcedId == "user999"
    assert user.username == "cjohnson"


def test_parse_user_response_invalid_data():
    """Test parsing fails with invalid data."""
    data = {"invalid": "data"}

    with pytest.raises(ParseError, match="Failed to parse User response"):
        parse_user_response(data)


    
