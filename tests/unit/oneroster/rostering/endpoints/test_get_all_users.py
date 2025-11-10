import pytest

from timeback.services.oneroster.rostering.endpoints.get_all_users import get_all_users
from timeback.models.response import TimebackGetAllUsersResponse
from timeback.models.request import TimebackGetAllUsersRequest, TimebackQueryParams


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
        "dateLastModified": "2024-01-01T00:00:00Z",
    }


def test_get_all_users_success():
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

    request = TimebackGetAllUsersRequest()
    resp = get_all_users(mock_http, request)

    assert isinstance(resp, TimebackGetAllUsersResponse)
    assert len(resp.users) == 2
    assert resp.totalCount == 2


def test_get_all_users_passes_query_params():
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

    query_params = TimebackQueryParams(
        fields=["sourcedId", "username"],
        limit=1,
        offset=0,
        sort="givenName",
        order_by="asc",
        filter="status='active'",
        search="john",
    )
    request = TimebackGetAllUsersRequest(query_params=query_params)
    resp = get_all_users(mock_http, request)

    assert isinstance(resp, TimebackGetAllUsersResponse)
    assert mock_http.last_params == {
        "fields": "sourcedId,username",
        "limit": 1,
        "offset": 0,
        "sort": "givenName",
        "orderBy": "asc",
        "filter": "status='active'",
        "search": "john",
    }


