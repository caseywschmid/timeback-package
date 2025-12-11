"""Unit tests for update_assessment_test_metadata endpoint.

Tests the update_assessment_test_metadata function that updates only the
metadata fields of an assessment test.
"""

from typing import Any, Dict
import pytest

from timeback.services.qti.endpoints.update_assessment_test_metadata import update_assessment_test_metadata
from timeback.models.request import TimebackUpdateAssessmentTestMetadataRequest
from timeback.models.response import TimebackUpdateAssessmentTestMetadataResponse


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


def create_mock_assessment_test_data(
    identifier: str = "test-001",
    title: str = "Test Assessment"
) -> Dict[str, Any]:
    """Create mock assessment test data for testing."""
    return {
        "identifier": identifier,
        "title": title,
        "qtiVersion": "3.0",
        "qti-test-part": [],
        "qti-outcome-declaration": [],
        "metadata": {
            "subject": "Math",
            "grade": "5",
            "description": "Updated description"
        },
        "rawXml": '<?xml version="1.0"?><qti-assessment-test></qti-assessment-test>',
        "createdAt": "2024-01-01T00:00:00Z",
        "updatedAt": "2024-01-02T00:00:00Z"
    }


class TestUpdateAssessmentTestMetadata:
    """Tests for update_assessment_test_metadata endpoint."""

    def test_update_assessment_test_metadata_success(self) -> None:
        """Test successful metadata update."""
        mock_data = create_mock_assessment_test_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentTestMetadataRequest(
            metadata={"subject": "Math", "description": "Updated"}
        )
        result = update_assessment_test_metadata(mock_http, "test-001", request)
        
        assert isinstance(result, TimebackUpdateAssessmentTestMetadataResponse)
        assert result.identifier == "test-001"
        assert mock_http.last_path == "/assessment-tests/test-001/metadata"

    def test_update_assessment_test_metadata_with_different_identifier(self) -> None:
        """Test that the identifier is correctly placed in the path."""
        mock_data = create_mock_assessment_test_data(identifier="math-test-99")
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentTestMetadataRequest(
            metadata={"subject": "Science"}
        )
        result = update_assessment_test_metadata(mock_http, "math-test-99", request)
        
        assert result.identifier == "math-test-99"
        assert mock_http.last_path == "/assessment-tests/math-test-99/metadata"

    def test_update_assessment_test_metadata_body_contains_metadata(self) -> None:
        """Test that the request body contains the metadata."""
        mock_data = create_mock_assessment_test_data()
        mock_http = MockHttpClient(mock_data)
        
        metadata = {"subject": "Math", "grade": "6", "description": "New description"}
        request = TimebackUpdateAssessmentTestMetadataRequest(metadata=metadata)
        result = update_assessment_test_metadata(mock_http, "test-001", request)
        
        assert mock_http.last_body["metadata"] == metadata

    def test_update_assessment_test_metadata_validates_response(self) -> None:
        """Test that response is validated correctly."""
        mock_data = create_mock_assessment_test_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentTestMetadataRequest(
            metadata={"subject": "Math"}
        )
        result = update_assessment_test_metadata(mock_http, "test-001", request)
        
        assert result.identifier == "test-001"
        assert result.title == "Test Assessment"
        assert result.qti_version == "3.0"
        assert result.metadata["subject"] == "Math"

    def test_update_assessment_test_metadata_complex_metadata(self) -> None:
        """Test with complex metadata including nested objects."""
        mock_data = create_mock_assessment_test_data()
        mock_data["metadata"] = {
            "subject": "Math",
            "learningObjectives": ["LO1", "LO2"],
            "settings": {"timeLimit": 3600, "allowReview": True}
        }
        mock_http = MockHttpClient(mock_data)
        
        metadata = {
            "subject": "Math",
            "learningObjectives": ["LO1", "LO2"],
            "settings": {"timeLimit": 3600, "allowReview": True}
        }
        request = TimebackUpdateAssessmentTestMetadataRequest(metadata=metadata)
        result = update_assessment_test_metadata(mock_http, "test-001", request)
        
        assert result.metadata["learningObjectives"] == ["LO1", "LO2"]
        assert result.metadata["settings"]["timeLimit"] == 3600

