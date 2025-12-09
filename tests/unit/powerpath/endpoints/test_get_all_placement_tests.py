"""Unit tests for get_all_placement_tests endpoint."""

import pytest

from timeback.services.powerpath.endpoints.get_all_placement_tests import get_all_placement_tests
from timeback.models.response import TimebackGetAllPlacementTestsResponse
from timeback.models.request import TimebackGetAllPlacementTestsRequest
from timeback.enums import TimebackSubject


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data):
        self.response_data = response_data
        self.last_path = None
        self.last_params = None

    def get(self, path, params=None):
        self.last_path = path
        self.last_params = params
        return self.response_data


def minimal_placement_test(idx: str):
    """Create a minimal placement test object for testing."""
    return {
        "component_resources": {
            "sourcedId": f"cr{idx}",
            "title": f"Placement Test {idx}",
        },
        "resources": {
            "sourcedId": f"r{idx}",
            "title": f"Resource {idx}",
        },
        "resources_metadata": {
            "lessonType": "placement",
        },
        "assessment_line_items": {
            "sourcedId": f"ali{idx}",
        },
        "assessment_results": [
            {"sourcedId": f"ar{idx}", "score": 85.0}
        ],
    }


def test_get_all_placement_tests_success():
    """Test successful retrieval of all placement tests."""
    mock_http = MockHttpClient(
        {
            "placementTests": [minimal_placement_test("1"), minimal_placement_test("2")],
        }
    )

    request = TimebackGetAllPlacementTestsRequest(
        student="student-123",
        subject=TimebackSubject.READING,
    )
    resp = get_all_placement_tests(mock_http, request)

    assert isinstance(resp, TimebackGetAllPlacementTestsResponse)
    assert len(resp.placementTests) == 2
    assert resp.placementTests[0].component_resources["sourcedId"] == "cr1"
    assert resp.placementTests[1].component_resources["sourcedId"] == "cr2"


def test_get_all_placement_tests_passes_query_params():
    """Test that student and subject are passed as query params."""
    mock_http = MockHttpClient(
        {
            "placementTests": [minimal_placement_test("1")],
        }
    )

    request = TimebackGetAllPlacementTestsRequest(
        student="student-456",
        subject=TimebackSubject.MATH,
    )
    resp = get_all_placement_tests(mock_http, request)

    assert isinstance(resp, TimebackGetAllPlacementTestsResponse)
    assert mock_http.last_path == "/powerpath/placement/getAllPlacementTests"
    assert mock_http.last_params == {
        "student": "student-456",
        "subject": "Math",
    }


def test_get_all_placement_tests_empty_results():
    """Test handling of empty placement tests list."""
    mock_http = MockHttpClient(
        {
            "placementTests": [],
        }
    )

    request = TimebackGetAllPlacementTestsRequest(
        student="student-789",
        subject=TimebackSubject.SCIENCE,
    )
    resp = get_all_placement_tests(mock_http, request)

    assert isinstance(resp, TimebackGetAllPlacementTestsResponse)
    assert len(resp.placementTests) == 0


def test_get_all_placement_tests_with_null_assessment_data():
    """Test handling of placement tests with null assessment data."""
    mock_http = MockHttpClient(
        {
            "placementTests": [
                {
                    "component_resources": {"sourcedId": "cr1"},
                    "resources": {"sourcedId": "r1"},
                    "resources_metadata": {"lessonType": "placement"},
                    "assessment_line_items": None,
                    "assessment_results": None,
                }
            ],
        }
    )

    request = TimebackGetAllPlacementTestsRequest(
        student="student-000",
        subject=TimebackSubject.LANGUAGE,
    )
    resp = get_all_placement_tests(mock_http, request)

    assert isinstance(resp, TimebackGetAllPlacementTestsResponse)
    assert len(resp.placementTests) == 1
    assert resp.placementTests[0].assessment_line_items is None
    assert resp.placementTests[0].assessment_results is None

