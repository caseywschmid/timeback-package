"""Unit tests for update_test_part endpoint.

Tests the update_test_part function that updates an existing test part.
"""

from typing import Any, Dict
import pytest

from timeback.services.qti.endpoints.update_test_part import update_test_part
from timeback.models.request import TimebackUpdateTestPartRequest
from timeback.models.response import TimebackUpdateTestPartResponse
from timeback.models.timeback_qti_section import TimebackQTISection
from timeback.enums import TimebackQTINavigationMode, TimebackQTISubmissionMode


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data: Dict[str, Any]):
        """Initialize with the response data to return."""
        self.response_data = response_data
        self.last_path: str = ""
        self.last_body: Dict[str, Any] = {}

    def put(self, path: str, json: Dict[str, Any] = None) -> Dict[str, Any]:
        """Mock PUT request."""
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
                "title": "Updated Section",
                "visible": True
            }
        ],
        "rawXml": '<?xml version="1.0"?><qti-test-part></qti-test-part>',
        "content": {}
    }


class TestUpdateTestPart:
    """Tests for update_test_part endpoint."""

    def test_update_test_part_success(self) -> None:
        """Test successful test part update."""
        mock_data = create_mock_test_part_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateTestPartRequest(
            identifier="part-001",
            navigation_mode=TimebackQTINavigationMode.LINEAR,
            submission_mode=TimebackQTISubmissionMode.INDIVIDUAL,
            qti_assessment_section=[
                TimebackQTISection(identifier="section-001", title="Updated Section")
            ]
        )
        result = update_test_part(mock_http, "test-001", "part-001", request)
        
        assert isinstance(result, TimebackUpdateTestPartResponse)
        assert result.identifier == "part-001"
        assert mock_http.last_path == "/assessment-tests/test-001/test-parts/part-001"

    def test_update_test_part_path_includes_both_identifiers(self) -> None:
        """Test that the path includes both test and part identifiers."""
        mock_data = create_mock_test_part_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateTestPartRequest(
            identifier="my-part",
            navigation_mode=TimebackQTINavigationMode.LINEAR,
            submission_mode=TimebackQTISubmissionMode.INDIVIDUAL,
            qti_assessment_section=[
                TimebackQTISection(identifier="section-001", title="Section")
            ]
        )
        update_test_part(mock_http, "my-test", "my-part", request)
        
        assert mock_http.last_path == "/assessment-tests/my-test/test-parts/my-part"

    def test_update_test_part_body_uses_aliases(self) -> None:
        """Test that the request body uses API aliases."""
        mock_data = create_mock_test_part_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateTestPartRequest(
            identifier="part-001",
            navigation_mode=TimebackQTINavigationMode.NONLINEAR,
            submission_mode=TimebackQTISubmissionMode.SIMULTANEOUS,
            qti_assessment_section=[
                TimebackQTISection(identifier="section-001", title="Section")
            ]
        )
        update_test_part(mock_http, "test-001", "part-001", request)
        
        assert mock_http.last_body["navigationMode"] == "nonlinear"
        assert mock_http.last_body["submissionMode"] == "simultaneous"
        assert "qti-assessment-section" in mock_http.last_body

    def test_update_test_part_changes_navigation_mode(self) -> None:
        """Test updating navigation mode."""
        mock_data = create_mock_test_part_response(navigation_mode="nonlinear")
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateTestPartRequest(
            identifier="part-001",
            navigation_mode=TimebackQTINavigationMode.NONLINEAR,
            submission_mode=TimebackQTISubmissionMode.INDIVIDUAL,
            qti_assessment_section=[
                TimebackQTISection(identifier="section-001", title="Section")
            ]
        )
        result = update_test_part(mock_http, "test-001", "part-001", request)
        
        assert result.navigation_mode == TimebackQTINavigationMode.NONLINEAR

    def test_update_test_part_changes_submission_mode(self) -> None:
        """Test updating submission mode."""
        mock_data = create_mock_test_part_response(submission_mode="simultaneous")
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateTestPartRequest(
            identifier="part-001",
            navigation_mode=TimebackQTINavigationMode.LINEAR,
            submission_mode=TimebackQTISubmissionMode.SIMULTANEOUS,
            qti_assessment_section=[
                TimebackQTISection(identifier="section-001", title="Section")
            ]
        )
        result = update_test_part(mock_http, "test-001", "part-001", request)
        
        assert result.submission_mode == TimebackQTISubmissionMode.SIMULTANEOUS

    def test_update_test_part_with_multiple_sections(self) -> None:
        """Test updating with multiple sections."""
        mock_data = create_mock_test_part_response()
        mock_data["qti-assessment-section"] = [
            {"identifier": "section-001", "title": "Section 1", "visible": True},
            {"identifier": "section-002", "title": "Section 2", "visible": True},
        ]
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateTestPartRequest(
            identifier="part-001",
            navigation_mode=TimebackQTINavigationMode.LINEAR,
            submission_mode=TimebackQTISubmissionMode.INDIVIDUAL,
            qti_assessment_section=[
                TimebackQTISection(identifier="section-001", title="Section 1"),
                TimebackQTISection(identifier="section-002", title="Section 2"),
            ]
        )
        result = update_test_part(mock_http, "test-001", "part-001", request)
        
        assert len(result.qti_assessment_section) == 2

