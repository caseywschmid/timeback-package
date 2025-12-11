"""Unit tests for get_test_part endpoint.

Tests the get_test_part function that retrieves a specific test part
by identifier.
"""

from typing import Any, Dict
import pytest

from timeback.services.qti.endpoints.get_test_part import get_test_part
from timeback.models.response import TimebackGetTestPartResponse
from timeback.enums import TimebackQTINavigationMode, TimebackQTISubmissionMode


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data: Dict[str, Any]):
        """Initialize with the response data to return."""
        self.response_data = response_data
        self.last_path: str = ""

    def get(self, path: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """Mock GET request."""
        self.last_path = path
        return self.response_data


def create_mock_test_part_data(
    identifier: str = "part-001",
    navigation_mode: str = "linear",
    submission_mode: str = "individual"
) -> Dict[str, Any]:
    """Create mock test part data for testing."""
    return {
        "identifier": identifier,
        "navigationMode": navigation_mode,
        "submissionMode": submission_mode,
        "qti-assessment-section": [
            {
                "identifier": "section-001",
                "title": "Test Section",
                "visible": True,
                "required": True,
                "fixed": False
            }
        ],
        "rawXml": '<?xml version="1.0"?><qti-test-part></qti-test-part>',
        "content": {
            "qti-test-part": {
                "_attributes": {
                    "identifier": identifier,
                    "navigation-mode": navigation_mode,
                    "submission-mode": submission_mode
                }
            }
        }
    }


class TestGetTestPart:
    """Tests for get_test_part endpoint."""

    def test_get_test_part_success(self) -> None:
        """Test successful retrieval of a test part."""
        mock_data = create_mock_test_part_data()
        mock_http = MockHttpClient(mock_data)
        
        result = get_test_part(mock_http, "test-001", "part-001")
        
        assert isinstance(result, TimebackGetTestPartResponse)
        assert result.identifier == "part-001"
        assert mock_http.last_path == "/assessment-tests/test-001/test-parts/part-001"

    def test_get_test_part_path_includes_both_identifiers(self) -> None:
        """Test that the path includes both test and part identifiers."""
        mock_data = create_mock_test_part_data()
        mock_http = MockHttpClient(mock_data)
        
        get_test_part(mock_http, "my-test-id", "my-part-id")
        
        assert mock_http.last_path == "/assessment-tests/my-test-id/test-parts/my-part-id"

    def test_get_test_part_validates_navigation_mode(self) -> None:
        """Test that navigation mode is correctly parsed."""
        mock_data = create_mock_test_part_data(navigation_mode="nonlinear")
        mock_http = MockHttpClient(mock_data)
        
        result = get_test_part(mock_http, "test-001", "part-001")
        
        assert result.navigation_mode == TimebackQTINavigationMode.NONLINEAR

    def test_get_test_part_validates_submission_mode(self) -> None:
        """Test that submission mode is correctly parsed."""
        mock_data = create_mock_test_part_data(submission_mode="simultaneous")
        mock_http = MockHttpClient(mock_data)
        
        result = get_test_part(mock_http, "test-001", "part-001")
        
        assert result.submission_mode == TimebackQTISubmissionMode.SIMULTANEOUS

    def test_get_test_part_includes_sections(self) -> None:
        """Test that sections are included in the response."""
        mock_data = create_mock_test_part_data()
        mock_data["qti-assessment-section"] = [
            {"identifier": "section-001", "title": "Section 1", "visible": True},
            {"identifier": "section-002", "title": "Section 2", "visible": True},
        ]
        mock_http = MockHttpClient(mock_data)
        
        result = get_test_part(mock_http, "test-001", "part-001")
        
        assert result.qti_assessment_section is not None
        assert len(result.qti_assessment_section) == 2

    def test_get_test_part_includes_raw_xml(self) -> None:
        """Test that raw XML is included in the response."""
        mock_data = create_mock_test_part_data()
        mock_http = MockHttpClient(mock_data)
        
        result = get_test_part(mock_http, "test-001", "part-001")
        
        assert result.raw_xml is not None
        assert "qti-test-part" in result.raw_xml

    def test_get_test_part_includes_content(self) -> None:
        """Test that parsed content is included in the response."""
        mock_data = create_mock_test_part_data()
        mock_http = MockHttpClient(mock_data)
        
        result = get_test_part(mock_http, "test-001", "part-001")
        
        assert result.content is not None
        assert "qti-test-part" in result.content

