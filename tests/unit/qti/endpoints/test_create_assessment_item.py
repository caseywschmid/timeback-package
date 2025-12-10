"""Unit tests for create_assessment_item endpoint.

Tests the create_assessment_item function that creates a new QTI assessment item.
"""

from typing import Any, Dict
import pytest

from timeback.services.qti.endpoints.create_assessment_item import create_assessment_item
from timeback.models.request import TimebackCreateAssessmentItemRequest
from timeback.models.response import TimebackCreateAssessmentItemResponse


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
                "correctResponse": {"value": ["B"]}
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


SAMPLE_QTI_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<qti-assessment-item
  xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
  identifier="sample-item-1"
  title="Sample Question"
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


class TestCreateAssessmentItem:
    """Tests for create_assessment_item endpoint."""

    def test_create_assessment_item_with_xml(self) -> None:
        """Test successful creation of an assessment item using XML."""
        mock_data = create_mock_assessment_item_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateAssessmentItemRequest(
            format="xml",
            xml=SAMPLE_QTI_XML
        )
        result = create_assessment_item(mock_http, request)
        
        assert isinstance(result, TimebackCreateAssessmentItemResponse)
        assert result.identifier == "item-001"
        assert mock_http.last_path == "/assessment-items"
        assert mock_http.last_body["format"] == "xml"
        assert "qti-assessment-item" in mock_http.last_body["xml"]

    def test_create_assessment_item_with_metadata(self) -> None:
        """Test creation with metadata."""
        mock_data = create_mock_assessment_item_data()
        mock_data["metadata"] = {"subject": "Math", "grade": "5"}
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateAssessmentItemRequest(
            format="xml",
            xml=SAMPLE_QTI_XML,
            metadata={"subject": "Math", "grade": "5"}
        )
        result = create_assessment_item(mock_http, request)
        
        assert result.metadata is not None
        assert mock_http.last_body["metadata"] == {"subject": "Math", "grade": "5"}

    def test_create_assessment_item_format_defaults_to_xml(self) -> None:
        """Test that format defaults to xml."""
        mock_data = create_mock_assessment_item_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateAssessmentItemRequest(xml=SAMPLE_QTI_XML)
        result = create_assessment_item(mock_http, request)
        
        assert mock_http.last_body["format"] == "xml"

    def test_create_assessment_item_excludes_none_values(self) -> None:
        """Test that None values are excluded from the request body."""
        mock_data = create_mock_assessment_item_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateAssessmentItemRequest(
            format="xml",
            xml=SAMPLE_QTI_XML
            # metadata is None by default
        )
        result = create_assessment_item(mock_http, request)
        
        assert "metadata" not in mock_http.last_body

    def test_create_assessment_item_validates_response(self) -> None:
        """Test that response is validated correctly."""
        mock_data = create_mock_assessment_item_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateAssessmentItemRequest(
            format="xml",
            xml=SAMPLE_QTI_XML
        )
        result = create_assessment_item(mock_http, request)
        
        assert result.identifier == "item-001"
        assert result.title == "Test Assessment Item"
        assert result.type == "choice"
        assert result.qtiVersion == "3.0"
        assert result.timeDependent == False
        assert result.adaptive == False

    def test_create_assessment_item_with_difficulty_metadata(self) -> None:
        """Test creation with difficulty in metadata."""
        mock_data = create_mock_assessment_item_data()
        mock_data["metadata"] = {"difficulty": "hard"}
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateAssessmentItemRequest(
            format="xml",
            xml=SAMPLE_QTI_XML,
            metadata={"difficulty": "hard"}
        )
        result = create_assessment_item(mock_http, request)
        
        assert result.metadata["difficulty"] == "hard"

    def test_create_assessment_item_with_learning_objectives(self) -> None:
        """Test creation with learning objective set in metadata."""
        mock_data = create_mock_assessment_item_data()
        mock_data["metadata"] = {
            "learningObjectiveSet": [
                {"source": "CASE", "learningObjectiveIds": ["D1.5.6-8"]}
            ]
        }
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateAssessmentItemRequest(
            format="xml",
            xml=SAMPLE_QTI_XML,
            metadata={
                "learningObjectiveSet": [
                    {"source": "CASE", "learningObjectiveIds": ["D1.5.6-8"]}
                ]
            }
        )
        result = create_assessment_item(mock_http, request)
        
        assert "learningObjectiveSet" in result.metadata

