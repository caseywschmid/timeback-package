import pytest

from timeback.services.oneroster.rostering.endpoints.list_users import list_users
from timeback.models.response import TimebackListUsersResponse


class MockHttpClient:
    def __init__(self, response_data):
        self.response_data = response_data
        self.last_params = None

    def get(self, path, params=None):
        self.last_params = params
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


def test_list_users_success():
    mock_http = MockHttpClient(
        {
            "users": [minimal_user("1"), minimal_user("2")],
            "totalCount": 2,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }
    )

    resp = list_users(mock_http)

    assert isinstance(resp, TimebackListUsersResponse)
    assert len(resp.users) == 2
    assert resp.totalCount == 2


def test_list_users_passes_query_params():
    mock_http = MockHttpClient(
        {
            "users": [minimal_user("9")],
            "totalCount": 1,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 1,
        }
    )

    resp = list_users(
        mock_http,
        fields=["sourcedId", "username"],
        limit=1,
        offset=0,
        sort="givenName",
        order_by="asc",
        filter="status='active'",
        search="john",
    )

    assert isinstance(resp, TimebackListUsersResponse)
    assert mock_http.last_params == {
        "fields": "sourcedId,username",
        "limit": 1,
        "offset": 0,
        "sort": "givenName",
        "orderBy": "asc",
        "filter": "status='active'",
        "search": "john",
    }


