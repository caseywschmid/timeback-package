import pytest
from unittest.mock import Mock

from timeback.services.oneroster.rostering.endpoints.get_school import get_school
from timeback.models.response import TimebackGetSchoolResponse
from timeback.models.request import TimebackGetSchoolRequest, TimebackQueryParams
from timeback.enums import TimebackOrgType, TimebackStatus


class MockHttpClient:
    def __init__(self, response_data):
        self.response_data = response_data
        self.last_params = None

    def get(self, path, params=None):
        self.last_params = params
        return self.response_data


def test_get_school_success():
    """Test successful school retrieval."""
    mock_http = MockHttpClient(
        {
            "org": {
                "sourcedId": "school123",
                "name": "Lincoln Elementary School",
                "type": "school",
                "status": "active",
                "dateLastModified": "2024-01-01T00:00:00Z",
            }
        }
    )

    request = TimebackGetSchoolRequest(sourced_id="school123")
    response = get_school(mock_http, request)

    assert isinstance(response, TimebackGetSchoolResponse)
    assert response.org.sourcedId == "school123"
    assert response.org.name == "Lincoln Elementary School"
    assert response.org.type == TimebackOrgType.SCHOOL


def test_get_school_with_fields_param():
    """Test that fields query param is passed as comma-separated string."""
    mock_http = MockHttpClient(
        {
            "org": {
                "sourcedId": "school123",
                "name": "Lincoln Elementary School",
                "type": "school",
                "status": "active",
                "dateLastModified": "2024-01-01T00:00:00Z",
            }
        }
    )

    query_params = TimebackQueryParams(fields=["sourcedId", "name"])
    request = TimebackGetSchoolRequest(sourced_id="school123", query_params=query_params)
    response = get_school(mock_http, request)

    assert isinstance(response, TimebackGetSchoolResponse)
    assert mock_http.last_params == {"fields": "sourcedId,name"}


def test_get_school_with_parent():
    """Test school retrieval with parent organization."""
    mock_http = MockHttpClient(
        {
            "org": {
                "sourcedId": "school456",
                "name": "Washington High School",
                "type": "school",
                "status": "active",
                "parent": {"sourcedId": "district1", "type": "org"},
                "dateLastModified": "2024-01-01T00:00:00Z",
            }
        }
    )

    request = TimebackGetSchoolRequest(sourced_id="school456")
    response = get_school(mock_http, request)

    assert isinstance(response, TimebackGetSchoolResponse)
    assert response.org.sourcedId == "school456"
    assert response.org.parent is not None
    assert response.org.parent.sourcedId == "district1"

