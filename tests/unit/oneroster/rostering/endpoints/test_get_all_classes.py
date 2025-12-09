import pytest

from timeback.services.oneroster.rostering.endpoints.get_all_classes import get_all_classes
from timeback.models.response import TimebackGetAllClassesResponse
from timeback.models.request import TimebackGetAllClassesRequest, TimebackQueryParams


class MockHttpClient:
    def __init__(self, response_data):
        self.response_data = response_data
        self.last_params = None

    def get(self, path, params=None):
        self.last_params = params
        return self.response_data


def minimal_class(idx: str):
    return {
        "sourcedId": f"class{idx}",
        "status": "active",
        "title": f"Class {idx}",
        "classCode": f"CODE{idx}",
        "classType": "scheduled",
        "location": f"Room {idx}",
        "course": {"sourcedId": f"course{idx}", "href": f"/courses/course{idx}", "type": "course"},
        "org": {"sourcedId": "org1", "href": "/orgs/org1", "type": "org"},
        "terms": [
            {"sourcedId": "term1", "href": "/terms/term1", "type": "academicSession"}
        ],
        "dateLastModified": "2024-01-01T00:00:00Z",
    }


def test_get_all_classes_success():
    mock_http = MockHttpClient(
        {
            "classes": [minimal_class("1"), minimal_class("2")],
            "totalCount": 2,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }
    )

    request = TimebackGetAllClassesRequest()
    resp = get_all_classes(mock_http, request)

    assert isinstance(resp, TimebackGetAllClassesResponse)
    assert len(resp.classes) == 2
    assert resp.total_count == 2
    assert resp.classes[0].sourcedId == "class1"
    assert resp.classes[0].title == "Class 1"
    assert resp.classes[0].status.value == "active"


def test_get_all_classes_passes_query_params():
    mock_http = MockHttpClient(
        {
            "classes": [minimal_class("9")],
            "totalCount": 1,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 1,
        }
    )

    query_params = TimebackQueryParams(
        fields=["sourcedId", "title"],
        limit=1,
        offset=0,
        sort="title",
        order_by="asc",
        filter="status='active'",
        search="math",
    )
    request = TimebackGetAllClassesRequest(query_params=query_params)
    resp = get_all_classes(mock_http, request)

    assert isinstance(resp, TimebackGetAllClassesResponse)
    assert mock_http.last_params == {
        "fields": "sourcedId,title",
        "limit": 1,
        "offset": 0,
        "sort": "title",
        "orderBy": "asc",
        "filter": "status='active'",
        "search": "math",
    }

