"""Unit tests for get_assessment_test endpoint.

Tests the get_assessment_test function that retrieves a single QTI assessment test.
"""

from typing import Any, Dict
import pytest

from timeback.services.qti.endpoints.get_assessment_test import get_assessment_test
from timeback.models.response import TimebackGetAssessmentTestResponse


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


def create_mock_assessment_test_data(
    identifier: str = "test-001",
    title: str = "Test Assessment"
) -> Dict[str, Any]:
    """Create mock assessment test data for testing."""
    return {
        "identifier": identifier,
        "title": title,
        "qtiVersion": "3.0",
        "qti-test-part": [
            {
                "identifier": "part-1",
                "navigationMode": "linear",
                "submissionMode": "individual",
                "qti-assessment-section": [
                    {
                        "identifier": "section-1",
                        "title": "Section 1",
                        "visible": True
                    }
                ]
            }
        ],
        "qti-outcome-declaration": [
            {
                "identifier": "SCORE",
                "cardinality": "single",
                "baseType": "float"
            }
        ],
        "timeLimit": 3600,
        "maxAttempts": 3,
        "metadata": {"subject": "Math"},
        "rawXml": '<?xml version="1.0"?><qti-assessment-test></qti-assessment-test>',
        "createdAt": "2024-01-01T00:00:00Z",
        "updatedAt": "2024-01-01T00:00:00Z"
    }


class TestGetAssessmentTest:
    """Tests for get_assessment_test endpoint."""

    def test_get_assessment_test_success(self) -> None:
        """Test successful retrieval of an assessment test."""
        mock_data = create_mock_assessment_test_data()
        mock_http = MockHttpClient(mock_data)
        
        result = get_assessment_test(mock_http, "test-001")
        
        assert isinstance(result, TimebackGetAssessmentTestResponse)
        assert result.identifier == "test-001"
        assert result.title == "Test Assessment"
        assert mock_http.last_path == "/assessment-tests/test-001"

    def test_get_assessment_test_with_different_identifier(self) -> None:
        """Test that the identifier is correctly placed in the path."""
        mock_data = create_mock_assessment_test_data(identifier="math-final-42")
        mock_http = MockHttpClient(mock_data)
        
        result = get_assessment_test(mock_http, "math-final-42")
        
        assert result.identifier == "math-final-42"
        assert mock_http.last_path == "/assessment-tests/math-final-42"

    def test_get_assessment_test_validates_test_parts(self) -> None:
        """Test that test parts are correctly parsed."""
        mock_data = create_mock_assessment_test_data()
        mock_http = MockHttpClient(mock_data)
        
        result = get_assessment_test(mock_http, "test-001")
        
        assert result.qti_test_part is not None
        assert len(result.qti_test_part) == 1
        assert result.qti_test_part[0].identifier == "part-1"

    def test_get_assessment_test_validates_outcome_declarations(self) -> None:
        """Test that outcome declarations are correctly parsed."""
        mock_data = create_mock_assessment_test_data()
        mock_http = MockHttpClient(mock_data)
        
        result = get_assessment_test(mock_http, "test-001")
        
        assert result.qti_outcome_declaration is not None
        assert len(result.qti_outcome_declaration) == 1
        assert result.qti_outcome_declaration[0].identifier == "SCORE"

    def test_get_assessment_test_validates_time_limit(self) -> None:
        """Test that time limit is correctly parsed."""
        mock_data = create_mock_assessment_test_data()
        mock_http = MockHttpClient(mock_data)
        
        result = get_assessment_test(mock_http, "test-001")
        
        assert result.time_limit == 3600

    def test_get_assessment_test_validates_metadata(self) -> None:
        """Test that metadata is correctly parsed."""
        mock_data = create_mock_assessment_test_data()
        mock_http = MockHttpClient(mock_data)
        
        result = get_assessment_test(mock_http, "test-001")
        
        assert result.metadata is not None
        assert result.metadata["subject"] == "Math"

    def test_get_assessment_test_validates_raw_xml(self) -> None:
        """Test that rawXml is correctly parsed."""
        mock_data = create_mock_assessment_test_data()
        mock_http = MockHttpClient(mock_data)
        
        result = get_assessment_test(mock_http, "test-001")
        
        assert result.raw_xml is not None
        assert "qti-assessment-test" in result.raw_xml

