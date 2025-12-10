"""Unit tests for update_metadata endpoint.

Tests the update_metadata function that updates metadata for assessment items.
"""

from typing import Any, Dict
import pytest

from timeback.services.qti.endpoints.update_metadata import update_metadata
from timeback.models.request import TimebackUpdateAssessmentItemMetadataRequest
from timeback.models.response import TimebackUpdateAssessmentItemMetadataResponse


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


def create_mock_assessment_item_data(
    identifier: str = "item-001",
    title: str = "Test Assessment Item"
) -> Dict[str, Any]:
    """Create mock assessment item data for testing."""
    return {
        "identifier": identifier,
        "title": title,
        "type": "choice",
        "qtiVersion": "3.0",
        "timeDependent": False,
        "adaptive": False,
        "responseDeclarations": [
            {
                "identifier": "RESPONSE",
                "cardinality": "single",
                "baseType": "identifier",
                "correctResponse": {"value": ["B"]}
            }
        ],
        "metadata": {
            "subject": "Math",
            "grade": "5",
            "difficulty": "medium"
        },
        "rawXml": '<?xml version="1.0"?><qti-assessment-item></qti-assessment-item>'
    }


SAMPLE_QTI_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<qti-assessment-item
  xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
  identifier="item-001"
  title="Test Item"
  adaptive="false"
  time-dependent="false">
  <qti-response-declaration identifier="RESPONSE" cardinality="single" base-type="identifier">
    <qti-correct-response>
      <qti-value>B</qti-value>
    </qti-correct-response>
  </qti-response-declaration>
  <qti-item-body>
    <qti-choice-interaction response-identifier="RESPONSE" max-choices="1">
      <qti-prompt>What is 2 + 2?</qti-prompt>
      <qti-simple-choice identifier="A">3</qti-simple-choice>
      <qti-simple-choice identifier="B">4</qti-simple-choice>
    </qti-choice-interaction>
  </qti-item-body>
</qti-assessment-item>'''


class TestUpdateMetadata:
    """Tests for update_metadata endpoint."""

    def test_update_metadata_success(self) -> None:
        """Test successful metadata update."""
        mock_data = create_mock_assessment_item_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentItemMetadataRequest(
            format="xml",
            xml=SAMPLE_QTI_XML,
            metadata={"subject": "Math", "difficulty": "hard"}
        )
        result = update_metadata(mock_http, request)
        
        assert isinstance(result, TimebackUpdateAssessmentItemMetadataResponse)
        assert result.identifier == "item-001"
        assert mock_http.last_path == "/assessment-items/metadata"
        assert mock_http.last_body["format"] == "xml"

    def test_update_metadata_with_metadata_only(self) -> None:
        """Test metadata update with metadata field."""
        mock_data = create_mock_assessment_item_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentItemMetadataRequest(
            format="xml",
            xml=SAMPLE_QTI_XML,
            metadata={"difficulty": "easy", "grade": "6"}
        )
        result = update_metadata(mock_http, request)
        
        assert mock_http.last_body["metadata"] == {"difficulty": "easy", "grade": "6"}

    def test_update_metadata_format_defaults_to_xml(self) -> None:
        """Test that format defaults to xml."""
        mock_data = create_mock_assessment_item_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentItemMetadataRequest(xml=SAMPLE_QTI_XML)
        result = update_metadata(mock_http, request)
        
        assert mock_http.last_body["format"] == "xml"

    def test_update_metadata_excludes_none_values(self) -> None:
        """Test that None values are excluded from the request body."""
        mock_data = create_mock_assessment_item_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentItemMetadataRequest(
            format="xml",
            xml=SAMPLE_QTI_XML
            # metadata is None by default
        )
        result = update_metadata(mock_http, request)
        
        assert "metadata" not in mock_http.last_body

    def test_update_metadata_validates_response(self) -> None:
        """Test that response is validated correctly."""
        mock_data = create_mock_assessment_item_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentItemMetadataRequest(
            format="xml",
            xml=SAMPLE_QTI_XML,
            metadata={"subject": "Math"}
        )
        result = update_metadata(mock_http, request)
        
        assert result.identifier == "item-001"
        assert result.title == "Test Assessment Item"
        assert result.type == "choice"
        assert result.metadata["subject"] == "Math"

    def test_update_metadata_path_is_correct(self) -> None:
        """Test that the path is correctly set."""
        mock_data = create_mock_assessment_item_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentItemMetadataRequest(
            format="xml",
            xml=SAMPLE_QTI_XML
        )
        update_metadata(mock_http, request)
        
        assert mock_http.last_path == "/assessment-items/metadata"

