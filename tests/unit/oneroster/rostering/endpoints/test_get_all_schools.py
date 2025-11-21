import pytest

from timeback.services.oneroster.rostering.endpoints.get_all_schools import get_all_schools
from timeback.models.response import TimebackGetAllSchoolsResponse
from timeback.models.request import TimebackGetAllSchoolsRequest, TimebackQueryParams


class MockHttpClient:
    def __init__(self, response_data):
        self.response_data = response_data
        self.last_params = None

    def get(self, path, params=None):
        self.last_params = params
        return self.response_data


def minimal_org(idx: str):
    return {
        "sourcedId": f"org{idx}",
        "status": "active",
        "name": f"School {idx}",
        "type": "school",
        "identifier": f"ID{idx}",
        "children": [],
        "dateLastModified": "2024-01-01T00:00:00Z",
    }


def test_get_all_schools_success():
    mock_http = MockHttpClient(
        {
            "orgs": [minimal_org("1"), minimal_org("2")],
            "totalCount": 2,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }
    )

    request = TimebackGetAllSchoolsRequest()
    resp = get_all_schools(mock_http, request)

    assert isinstance(resp, TimebackGetAllSchoolsResponse)
    assert len(resp.orgs) == 2
    assert resp.total_count == 2


def test_get_all_schools_passes_query_params():
    mock_http = MockHttpClient(
        {
            "orgs": [minimal_org("9")],
            "totalCount": 1,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 1,
        }
    )

    query_params = TimebackQueryParams(
        fields=["sourcedId", "name"],
        limit=1,
        offset=0,
        sort="name",
        order_by="asc",
        filter="status='active'",
        search="school",
    )
    request = TimebackGetAllSchoolsRequest(query_params=query_params)
    resp = get_all_schools(mock_http, request)

    assert isinstance(resp, TimebackGetAllSchoolsResponse)
    assert mock_http.last_params == {
        "fields": "sourcedId,name",
        "limit": 1,
        "offset": 0,
        "sort": "name",
        "orderBy": "asc",
        "filter": "status='active'",
        "search": "school",
    }

