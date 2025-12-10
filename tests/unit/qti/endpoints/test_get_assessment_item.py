"""Unit tests for get_assessment_item endpoint.

Tests the get_assessment_item function that retrieves a single QTI assessment item.
"""

from typing import Any, Dict
import pytest

from timeback.services.qti.endpoints.get_assessment_item import get_assessment_item
from timeback.models.response import TimebackGetAssessmentItemResponse


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


def create_mock_assessment_item_data(
    identifier: str = "item-001",
    title: str = "Test Assessment Item",
    item_type: str = "choice"
) -> Dict[str, Any]:
    """Create mock assessment item data for testing."""
    return {
        "identifier": identifier,
        "title": title,
        "type": item_type,
        "qtiVersion": "3.0",
        "timeDependent": False,
        "adaptive": False,
        "responseDeclarations": [
            {
                "identifier": "RESPONSE",
                "cardinality": "single",
                "baseType": "identifier",
                "correctResponse": {"value": ["A"]}
            }
        ],
        "outcomeDeclarations": [
            {
                "identifier": "SCORE",
                "cardinality": "single",
                "baseType": "float"
            }
        ],
        "responseProcessing": {
            "templateType": "match_correct",
            "responseDeclarationIdentifier": "RESPONSE",
            "outcomeIdentifier": "SCORE",
            "correctResponseIdentifier": "correct",
            "incorrectResponseIdentifier": "incorrect"
        },
        "metadata": {
            "subject": "Math",
            "grade": "7",
            "difficulty": "medium"
        },
        "rawXml": '<?xml version="1.0"?><qti-assessment-item></qti-assessment-item>'
    }


class TestGetAssessmentItem:
    """Tests for get_assessment_item endpoint."""

    def test_get_assessment_item_success(self) -> None:
        """Test successful retrieval of an assessment item."""
        mock_data = create_mock_assessment_item_data()
        mock_http = MockHttpClient(mock_data)
        
        result = get_assessment_item(mock_http, "item-001")
        
        assert isinstance(result, TimebackGetAssessmentItemResponse)
        assert result.identifier == "item-001"
        assert result.title == "Test Assessment Item"
        assert result.type == "choice"
        assert mock_http.last_path == "/assessment-items/item-001"

    def test_get_assessment_item_with_different_identifier(self) -> None:
        """Test that the identifier is correctly placed in the path."""
        mock_data = create_mock_assessment_item_data(identifier="math-question-42")
        mock_http = MockHttpClient(mock_data)
        
        result = get_assessment_item(mock_http, "math-question-42")
        
        assert result.identifier == "math-question-42"
        assert mock_http.last_path == "/assessment-items/math-question-42"

    def test_get_assessment_item_validates_response_declarations(self) -> None:
        """Test that response declarations are correctly parsed."""
        mock_data = create_mock_assessment_item_data()
        mock_http = MockHttpClient(mock_data)
        
        result = get_assessment_item(mock_http, "item-001")
        
        assert result.responseDeclarations is not None
        assert len(result.responseDeclarations) == 1
        assert result.responseDeclarations[0].identifier == "RESPONSE"
        assert result.responseDeclarations[0].cardinality == "single"
        assert result.responseDeclarations[0].baseType == "identifier"

    def test_get_assessment_item_validates_outcome_declarations(self) -> None:
        """Test that outcome declarations are correctly parsed."""
        mock_data = create_mock_assessment_item_data()
        mock_http = MockHttpClient(mock_data)
        
        result = get_assessment_item(mock_http, "item-001")
        
        assert result.outcomeDeclarations is not None
        assert len(result.outcomeDeclarations) == 1
        assert result.outcomeDeclarations[0].identifier == "SCORE"

    def test_get_assessment_item_validates_metadata(self) -> None:
        """Test that metadata is correctly parsed."""
        mock_data = create_mock_assessment_item_data()
        mock_http = MockHttpClient(mock_data)
        
        result = get_assessment_item(mock_http, "item-001")
        
        assert result.metadata is not None
        assert result.metadata["subject"] == "Math"
        assert result.metadata["grade"] == "7"
        assert result.metadata["difficulty"] == "medium"

    def test_get_assessment_item_validates_raw_xml(self) -> None:
        """Test that rawXml is correctly parsed."""
        mock_data = create_mock_assessment_item_data()
        mock_http = MockHttpClient(mock_data)
        
        result = get_assessment_item(mock_http, "item-001")
        
        assert result.rawXml is not None
        assert "qti-assessment-item" in result.rawXml

