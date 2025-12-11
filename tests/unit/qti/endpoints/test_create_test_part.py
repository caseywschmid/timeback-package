"""Unit tests for create_test_part endpoint.

Tests the create_test_part function that creates a new test part
within an assessment test.
"""

from typing import Any, Dict
import pytest

from timeback.services.qti.endpoints.create_test_part import create_test_part
from timeback.models.request import TimebackCreateTestPartRequest
from timeback.models.response import TimebackCreateTestPartResponse
from timeback.models.timeback_qti_section import TimebackQTISection
from timeback.enums import TimebackQTINavigationMode, TimebackQTISubmissionMode


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data: Dict[str, Any]):
        """Initialize with the response data to return."""
        self.response_data = response_data
        self.last_path: str = ""
        self.last_body: Dict[str, Any] = {}

    def post(self, path: str, json: Dict[str, Any] = None) -> Dict[str, Any]:
        """Mock POST request."""
        self.last_path = path
        self.last_body = json or {}
        return self.response_data


def create_mock_test_part_response(
    identifier: str = "part-001",
    navigation_mode: str = "linear",
    submission_mode: str = "individual"
) -> Dict[str, Any]:
    """Create mock test part response data for testing."""
    return {
        "identifier": identifier,
        "navigationMode": navigation_mode,
        "submissionMode": submission_mode,
        "qti-assessment-section": [
            {
                "identifier": "section-001",
                "title": "Test Section",
                "visible": True
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


class TestCreateTestPart:
    """Tests for create_test_part endpoint."""

    def test_create_test_part_success(self) -> None:
        """Test successful test part creation."""
        mock_data = create_mock_test_part_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateTestPartRequest(
            identifier="part-001",
            navigation_mode=TimebackQTINavigationMode.LINEAR,
            submission_mode=TimebackQTISubmissionMode.INDIVIDUAL,
            qti_assessment_section=[
                TimebackQTISection(identifier="section-001", title="Section 1")
            ]
        )
        result = create_test_part(mock_http, "test-001", request)
        
        assert isinstance(result, TimebackCreateTestPartResponse)
        assert result.identifier == "part-001"
        assert mock_http.last_path == "/assessment-tests/test-001/test-parts"

    def test_create_test_part_path_includes_test_identifier(self) -> None:
        """Test that the path includes the assessment test identifier."""
        mock_data = create_mock_test_part_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateTestPartRequest(
            identifier="part-001",
            navigation_mode=TimebackQTINavigationMode.LINEAR,
            submission_mode=TimebackQTISubmissionMode.INDIVIDUAL,
            qti_assessment_section=[
                TimebackQTISection(identifier="section-001", title="Section 1")
            ]
        )
        create_test_part(mock_http, "my-custom-test", request)
        
        assert mock_http.last_path == "/assessment-tests/my-custom-test/test-parts"

    def test_create_test_part_body_uses_aliases(self) -> None:
        """Test that the request body uses API aliases."""
        mock_data = create_mock_test_part_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateTestPartRequest(
            identifier="part-001",
            navigation_mode=TimebackQTINavigationMode.NONLINEAR,
            submission_mode=TimebackQTISubmissionMode.SIMULTANEOUS,
            qti_assessment_section=[
                TimebackQTISection(identifier="section-001", title="Section 1")
            ]
        )
        create_test_part(mock_http, "test-001", request)
        
        assert mock_http.last_body["navigationMode"] == "nonlinear"
        assert mock_http.last_body["submissionMode"] == "simultaneous"
        assert "qti-assessment-section" in mock_http.last_body

    def test_create_test_part_with_nonlinear_navigation(self) -> None:
        """Test creating a test part with nonlinear navigation."""
        mock_data = create_mock_test_part_response(navigation_mode="nonlinear")
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateTestPartRequest(
            identifier="part-002",
            navigation_mode=TimebackQTINavigationMode.NONLINEAR,
            submission_mode=TimebackQTISubmissionMode.INDIVIDUAL,
            qti_assessment_section=[
                TimebackQTISection(identifier="section-001", title="Section 1")
            ]
        )
        result = create_test_part(mock_http, "test-001", request)
        
        assert result.navigation_mode == TimebackQTINavigationMode.NONLINEAR

    def test_create_test_part_with_simultaneous_submission(self) -> None:
        """Test creating a test part with simultaneous submission."""
        mock_data = create_mock_test_part_response(submission_mode="simultaneous")
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateTestPartRequest(
            identifier="part-003",
            navigation_mode=TimebackQTINavigationMode.LINEAR,
            submission_mode=TimebackQTISubmissionMode.SIMULTANEOUS,
            qti_assessment_section=[
                TimebackQTISection(identifier="section-001", title="Section 1")
            ]
        )
        result = create_test_part(mock_http, "test-001", request)
        
        assert result.submission_mode == TimebackQTISubmissionMode.SIMULTANEOUS

    def test_create_test_part_with_multiple_sections(self) -> None:
        """Test creating a test part with multiple sections."""
        mock_data = create_mock_test_part_response()
        mock_data["qti-assessment-section"] = [
            {"identifier": "section-001", "title": "Section 1", "visible": True},
            {"identifier": "section-002", "title": "Section 2", "visible": True},
        ]
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateTestPartRequest(
            identifier="part-001",
            navigation_mode=TimebackQTINavigationMode.LINEAR,
            submission_mode=TimebackQTISubmissionMode.INDIVIDUAL,
            qti_assessment_section=[
                TimebackQTISection(identifier="section-001", title="Section 1"),
                TimebackQTISection(identifier="section-002", title="Section 2"),
            ]
        )
        result = create_test_part(mock_http, "test-001", request)
        
        assert len(result.qti_assessment_section) == 2

    def test_create_test_part_response_includes_raw_xml(self) -> None:
        """Test that response includes raw XML."""
        mock_data = create_mock_test_part_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateTestPartRequest(
            identifier="part-001",
            navigation_mode=TimebackQTINavigationMode.LINEAR,
            submission_mode=TimebackQTISubmissionMode.INDIVIDUAL,
            qti_assessment_section=[
                TimebackQTISection(identifier="section-001", title="Section 1")
            ]
        )
        result = create_test_part(mock_http, "test-001", request)
        
        assert result.raw_xml is not None
        assert "qti-test-part" in result.raw_xml

