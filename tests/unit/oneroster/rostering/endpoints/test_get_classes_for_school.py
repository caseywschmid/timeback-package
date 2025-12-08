import pytest

from timeback.services.oneroster.rostering.endpoints.get_classes_for_school import get_classes_for_school
from timeback.models.response import TimebackGetAllClassesResponse
from timeback.models.request import TimebackGetClassesForSchoolRequest, TimebackQueryParams


class MockHttpClient:
    def __init__(self, response_data):
        self.response_data = response_data
        self.last_path = None
        self.last_params = None

    def get(self, path, params=None):
        self.last_path = path
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
        "org": {"sourcedId": "school1", "href": "/orgs/school1", "type": "org"},
        "terms": [
            {"sourcedId": "term1", "href": "/terms/term1", "type": "academicSession"}
        ],
        "dateLastModified": "2024-01-01T00:00:00Z",
    }


def test_get_classes_for_school_success():
    """Test successful retrieval of classes for a school."""
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

    request = TimebackGetClassesForSchoolRequest(school_sourced_id="school1")
    resp = get_classes_for_school(mock_http, request)

    assert isinstance(resp, TimebackGetAllClassesResponse)
    assert len(resp.classes) == 2
    assert resp.total_count == 2
    assert resp.classes[0].sourcedId == "class1"
    assert resp.classes[0].title == "Class 1"
    # Verify the correct path was called
    assert "/ims/oneroster/rostering/v1p2/schools/school1/classes" in mock_http.last_path


def test_get_classes_for_school_passes_query_params():
    """Test that query parameters are passed correctly."""
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
    request = TimebackGetClassesForSchoolRequest(
        school_sourced_id="school123",
        query_params=query_params
    )
    resp = get_classes_for_school(mock_http, request)

    assert isinstance(resp, TimebackGetAllClassesResponse)
    assert "/ims/oneroster/rostering/v1p2/schools/school123/classes" in mock_http.last_path
    assert mock_http.last_params == {
        "fields": "sourcedId,title",
        "limit": 1,
        "offset": 0,
        "sort": "title",
        "orderBy": "asc",
        "filter": "status='active'",
        "search": "math",
    }


def test_get_classes_for_school_empty_list():
    """Test retrieval when school has no classes."""
    mock_http = MockHttpClient(
        {
            "classes": [],
            "totalCount": 0,
            "pageCount": 0,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }
    )

    request = TimebackGetClassesForSchoolRequest(school_sourced_id="empty-school")
    resp = get_classes_for_school(mock_http, request)

    assert isinstance(resp, TimebackGetAllClassesResponse)
    assert len(resp.classes) == 0
    assert resp.total_count == 0

