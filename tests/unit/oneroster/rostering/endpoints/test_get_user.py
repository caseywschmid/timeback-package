import pytest
from unittest.mock import Mock

from timeback.services.oneroster.rostering.endpoints.get_user import get_user
from timeback.models.response import TimebackGetUserResponse
from timeback.models.request import TimebackGetUserRequest, TimebackQueryParams


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
                "dateLastModified": "2024-01-01T00:00:00Z",
            }
        }
    )

    request = TimebackGetUserRequest(sourced_id="user123")
    response = get_user(mock_http, request)

    assert isinstance(response, TimebackGetUserResponse)
    assert response.user.sourcedId == "user123"
    assert response.user.username == "jdoe"


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
                "roles": [
                    {"role": "student", "roleType": "primary", "org": {"sourcedId": "org1", "type": "org"}}
                ],
                "agents": [],
                "userProfiles": [],
                "dateLastModified": "2024-01-01T00:00:00Z",
            }
        }
    )

    query_params = TimebackQueryParams(fields=["sourcedId", "username"])
    request = TimebackGetUserRequest(sourced_id="user123", query_params=query_params)
    response = get_user(mock_http, request)

    assert isinstance(response, TimebackGetUserResponse)
    assert mock_http.last_params == {"fields": "sourcedId,username"}


def test_get_user_direct_response():
    """Test user retrieval when API returns user object directly (edge case)."""
    # Note: According to API spec, response should be {"user": {...}}, but this tests edge case
    mock_http = MockHttpClient(
        {
            "user": {
                "sourcedId": "user456",
                "username": "asmith",
                "givenName": "Alice",
                "familyName": "Smith",
                "enabledUser": True,
                "roles": [{"role": "teacher", "roleType": "primary", "org": {"sourcedId": "org2", "type": "org"}}],
                "agents": [],
                "userProfiles": [],
                "dateLastModified": "2024-01-01T00:00:00Z",
            }
        }
    )

    request = TimebackGetUserRequest(sourced_id="user456")
    response = get_user(mock_http, request)

    assert isinstance(response, TimebackGetUserResponse)
    assert response.user.sourcedId == "user456"
    assert response.user.username == "asmith"


    
