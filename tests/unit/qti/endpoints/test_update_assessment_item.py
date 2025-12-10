"""Unit tests for update_assessment_item endpoint.

Tests the update_assessment_item function that updates an existing QTI assessment item.
"""

from typing import Any, Dict
import pytest

from timeback.services.qti.endpoints.update_assessment_item import update_assessment_item
from timeback.models.request import TimebackUpdateAssessmentItemRequest
from timeback.models.response import TimebackUpdateAssessmentItemResponse


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


def create_mock_assessment_item_data(
    identifier: str = "item-001",
    title: str = "Updated Assessment Item",
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
                "correctResponse": {"value": ["C"]}
            }
        ],
        "outcomeDeclarations": [
            {
                "identifier": "SCORE",
                "cardinality": "single",
                "baseType": "float"
            }
        ],
        "rawXml": '<?xml version="1.0"?><qti-assessment-item></qti-assessment-item>'
    }


SAMPLE_UPDATED_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<qti-assessment-item
  xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
  identifier="sample-item-1"
  title="Updated Question"
  adaptive="false"
  time-dependent="false">
  <qti-response-declaration identifier="RESPONSE" cardinality="single" base-type="identifier">
    <qti-correct-response>
      <qti-value>C</qti-value>
    </qti-correct-response>
  </qti-response-declaration>
  <qti-item-body>
    <qti-choice-interaction response-identifier="RESPONSE" max-choices="1">
      <qti-prompt>What is 3 + 3?</qti-prompt>
      <qti-simple-choice identifier="A">5</qti-simple-choice>
      <qti-simple-choice identifier="B">7</qti-simple-choice>
      <qti-simple-choice identifier="C">6</qti-simple-choice>
    </qti-choice-interaction>
  </qti-item-body>
</qti-assessment-item>'''


class TestUpdateAssessmentItem:
    """Tests for update_assessment_item endpoint."""

    def test_update_assessment_item_success(self) -> None:
        """Test successful update of an assessment item."""
        mock_data = create_mock_assessment_item_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentItemRequest(
            format="xml",
            xml=SAMPLE_UPDATED_XML
        )
        result = update_assessment_item(mock_http, "item-001", request)
        
        assert isinstance(result, TimebackUpdateAssessmentItemResponse)
        assert result.identifier == "item-001"
        assert mock_http.last_path == "/assessment-items/item-001"
        assert mock_http.last_body["format"] == "xml"

    def test_update_assessment_item_with_different_identifier(self) -> None:
        """Test that the identifier is correctly placed in the path."""
        mock_data = create_mock_assessment_item_data(identifier="math-q-99")
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentItemRequest(
            format="xml",
            xml=SAMPLE_UPDATED_XML
        )
        result = update_assessment_item(mock_http, "math-q-99", request)
        
        assert result.identifier == "math-q-99"
        assert mock_http.last_path == "/assessment-items/math-q-99"

    def test_update_assessment_item_with_metadata(self) -> None:
        """Test update with metadata changes."""
        mock_data = create_mock_assessment_item_data()
        mock_data["metadata"] = {"difficulty": "hard", "subject": "Science"}
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentItemRequest(
            format="xml",
            xml=SAMPLE_UPDATED_XML,
            metadata={"difficulty": "hard", "subject": "Science"}
        )
        result = update_assessment_item(mock_http, "item-001", request)
        
        assert result.metadata["difficulty"] == "hard"
        assert mock_http.last_body["metadata"] == {"difficulty": "hard", "subject": "Science"}

    def test_update_assessment_item_excludes_none_values(self) -> None:
        """Test that None values are excluded from the request body."""
        mock_data = create_mock_assessment_item_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentItemRequest(
            format="xml",
            xml=SAMPLE_UPDATED_XML
            # metadata is None by default
        )
        result = update_assessment_item(mock_http, "item-001", request)
        
        assert "metadata" not in mock_http.last_body

    def test_update_assessment_item_format_defaults_to_xml(self) -> None:
        """Test that format defaults to xml."""
        mock_data = create_mock_assessment_item_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentItemRequest(xml=SAMPLE_UPDATED_XML)
        result = update_assessment_item(mock_http, "item-001", request)
        
        assert mock_http.last_body["format"] == "xml"

    def test_update_assessment_item_validates_response(self) -> None:
        """Test that response is validated correctly."""
        mock_data = create_mock_assessment_item_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentItemRequest(
            format="xml",
            xml=SAMPLE_UPDATED_XML
        )
        result = update_assessment_item(mock_http, "item-001", request)
        
        assert result.title == "Updated Assessment Item"
        assert result.qtiVersion == "3.0"
        assert result.responseDeclarations is not None
        assert result.rawXml is not None

