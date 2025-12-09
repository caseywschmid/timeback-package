"""Unit tests for get_screening_results endpoint."""

import pytest

from timeback.services.powerpath.endpoints.get_screening_results import get_screening_results
from timeback.models.response import TimebackGetScreeningResultsResponse


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


def test_get_screening_results_success():
    """Test successful retrieval of screening results."""
    mock_http = MockHttpClient(
        {
            "Reading": {
                "grade": "5",
                "ritScore": 210.5,
                "testName": "Reading Screening Test",
                "completedAt": "2024-01-15T10:30:00Z",
            },
            "Math": {
                "grade": "6",
                "ritScore": 225.0,
                "testName": "Math Screening Test",
                "completedAt": "2024-01-16T14:00:00Z",
            },
        }
    )

    resp = get_screening_results(mock_http, "student-123")

    assert isinstance(resp, TimebackGetScreeningResultsResponse)
    assert "Reading" in resp.root
    assert "Math" in resp.root
    assert resp.root["Reading"].grade == "5"
    assert resp.root["Reading"].ritScore == 210.5
    assert resp.root["Math"].grade == "6"


def test_get_screening_results_path():
    """Test that the correct path is called."""
    mock_http = MockHttpClient({})

    resp = get_screening_results(mock_http, "user-456")

    assert mock_http.last_path == "/powerpath/screening/results/user-456"


def test_get_screening_results_with_null_values():
    """Test handling of null results for some subjects."""
    mock_http = MockHttpClient(
        {
            "Reading": {
                "grade": "4",
                "ritScore": 195.0,
                "testName": "Reading Screening",
                "completedAt": "2024-01-10T09:00:00Z",
            },
            "Math": None,
            "Language": None,
        }
    )

    resp = get_screening_results(mock_http, "student-789")

    assert isinstance(resp, TimebackGetScreeningResultsResponse)
    assert resp.root["Reading"] is not None
    assert resp.root["Reading"].grade == "4"
    assert resp.root["Math"] is None
    assert resp.root["Language"] is None


def test_get_screening_results_empty():
    """Test handling of empty results (no subjects)."""
    mock_http = MockHttpClient({})

    resp = get_screening_results(mock_http, "new-student")

    assert isinstance(resp, TimebackGetScreeningResultsResponse)
    assert len(resp.root) == 0


def test_get_screening_results_all_null():
    """Test when all subjects have null results."""
    mock_http = MockHttpClient(
        {
            "Reading": None,
            "Math": None,
            "Language": None,
            "Science": None,
        }
    )

    resp = get_screening_results(mock_http, "student-no-tests")

    assert isinstance(resp, TimebackGetScreeningResultsResponse)
    assert resp.root["Reading"] is None
    assert resp.root["Math"] is None
    assert resp.root["Language"] is None
    assert resp.root["Science"] is None

