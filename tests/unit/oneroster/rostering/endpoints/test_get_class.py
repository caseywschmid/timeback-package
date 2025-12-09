import pytest
from unittest.mock import Mock

from timeback.services.oneroster.rostering.endpoints.get_class import get_class
from timeback.models.response import TimebackGetClassResponse
from timeback.models.request import TimebackGetClassRequest, TimebackQueryParams
from timeback.enums import TimebackStatus, TimebackClassType


class MockHttpClient:
    def __init__(self, response_data):
        self.response_data = response_data
        self.last_params = None

    def get(self, path, params=None):
        self.last_params = params
        return self.response_data


def test_get_class_success():
    """Test successful class retrieval."""
    mock_http = MockHttpClient(
        {
            "class": {
                "sourcedId": "class123",
                "title": "Math 101 - Section A",
                "status": "active",
                "dateLastModified": "2024-01-01T00:00:00Z",
                "classType": "scheduled",
                "course": {"sourcedId": "course123"},
                "org": {"sourcedId": "school123", "type": "org"},
                "terms": [{"sourcedId": "term123"}],
            }
        }
    )

    request = TimebackGetClassRequest(sourced_id="class123")
    response = get_class(mock_http, request)

    assert isinstance(response, TimebackGetClassResponse)
    assert response.class_.sourcedId == "class123"
    assert response.class_.title == "Math 101 - Section A"
    assert response.class_.classType == TimebackClassType.SCHEDULED


def test_get_class_with_fields_param():
    """Test that fields query param is passed as comma-separated string."""
    mock_http = MockHttpClient(
        {
            "class": {
                "sourcedId": "class123",
                "title": "Math 101 - Section A",
                "status": "active",
                "dateLastModified": "2024-01-01T00:00:00Z",
                "course": {"sourcedId": "course123"},
                "org": {"sourcedId": "school123", "type": "org"},
                "terms": [{"sourcedId": "term123"}],
            }
        }
    )

    query_params = TimebackQueryParams(fields=["sourcedId", "title"])
    request = TimebackGetClassRequest(sourced_id="class123", query_params=query_params)
    response = get_class(mock_http, request)

    assert isinstance(response, TimebackGetClassResponse)
    assert mock_http.last_params == {"fields": "sourcedId,title"}


def test_get_class_with_all_fields():
    """Test class retrieval with all optional fields populated."""
    mock_http = MockHttpClient(
        {
            "class": {
                "sourcedId": "class456",
                "title": "English Literature - Period 2",
                "status": "active",
                "dateLastModified": "2024-01-01T00:00:00Z",
                "classType": "homeroom",
                "classCode": "ENG-LIT-P2",
                "location": "Room 204",
                "grades": ["9", "10"],
                "subjects": ["Language"],
                "subjectCodes": ["ELA"],
                "periods": ["2"],
                "course": {"sourcedId": "course456"},
                "org": {"sourcedId": "school456", "type": "org"},
                "terms": [{"sourcedId": "term456"}, {"sourcedId": "term457"}],
                "resources": [{"sourcedId": "resource123"}],
                "metadata": {"customField": "customValue"},
            }
        }
    )

    request = TimebackGetClassRequest(sourced_id="class456")
    response = get_class(mock_http, request)

    assert isinstance(response, TimebackGetClassResponse)
    assert response.class_.sourcedId == "class456"
    assert response.class_.title == "English Literature - Period 2"
    assert response.class_.classType == TimebackClassType.HOMEROOM
    assert response.class_.classCode == "ENG-LIT-P2"
    assert response.class_.location == "Room 204"
    assert response.class_.grades == ["9", "10"]
    assert response.class_.subjects == ["Language"]
    assert len(response.class_.terms) == 2
    assert response.class_.resources is not None
    assert len(response.class_.resources) == 1
    assert response.class_.metadata == {"customField": "customValue"}


def test_get_class_minimal_response():
    """Test class retrieval with only required fields."""
    mock_http = MockHttpClient(
        {
            "class": {
                "sourcedId": "class789",
                "title": "Science 101",
                "status": "active",
                "dateLastModified": "2024-01-01T00:00:00Z",
                "course": {"sourcedId": "course789"},
                "org": {"sourcedId": "school789", "type": "org"},
                "terms": [{"sourcedId": "term789"}],
            }
        }
    )

    request = TimebackGetClassRequest(sourced_id="class789")
    response = get_class(mock_http, request)

    assert isinstance(response, TimebackGetClassResponse)
    assert response.class_.sourcedId == "class789"
    assert response.class_.title == "Science 101"
    assert response.class_.course.sourcedId == "course789"
    assert response.class_.org.sourcedId == "school789"
    assert len(response.class_.terms) == 1
    # Optional fields should be None
    assert response.class_.classCode is None
    assert response.class_.location is None
    assert response.class_.grades is None

