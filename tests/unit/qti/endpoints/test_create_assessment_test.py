"""Unit tests for create_assessment_test endpoint.

Tests the create_assessment_test function that creates a new QTI assessment test.
"""

from typing import Any, Dict
import pytest

from timeback.services.qti.endpoints.create_assessment_test import create_assessment_test
from timeback.models.request import TimebackCreateAssessmentTestRequest
from timeback.models.response import TimebackCreateAssessmentTestResponse


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
        "rawXml": '<?xml version="1.0"?><qti-assessment-test></qti-assessment-test>',
        "createdAt": "2024-01-01T00:00:00Z",
        "updatedAt": "2024-01-01T00:00:00Z"
    }


SAMPLE_QTI_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<qti-assessment-test
  xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
  identifier="sample-test-1"
  title="Sample Test">
  <qti-test-part identifier="part-1" navigation-mode="linear" submission-mode="individual">
    <qti-assessment-section identifier="section-1" title="Section 1" visible="true">
      <qti-assessment-item-ref identifier="item-1" href="/assessment-items/item-1"/>
    </qti-assessment-section>
  </qti-test-part>
</qti-assessment-test>'''


class TestCreateAssessmentTest:
    """Tests for create_assessment_test endpoint."""

    def test_create_assessment_test_with_xml(self) -> None:
        """Test successful creation of an assessment test using XML."""
        mock_data = create_mock_assessment_test_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateAssessmentTestRequest(
            format="xml",
            xml=SAMPLE_QTI_XML
        )
        result = create_assessment_test(mock_http, request)
        
        assert isinstance(result, TimebackCreateAssessmentTestResponse)
        assert result.identifier == "test-001"
        assert mock_http.last_path == "/assessment-tests"
        assert mock_http.last_body["format"] == "xml"
        assert "qti-assessment-test" in mock_http.last_body["xml"]

    def test_create_assessment_test_with_metadata(self) -> None:
        """Test creation with metadata."""
        mock_data = create_mock_assessment_test_data()
        mock_data["metadata"] = {"subject": "Math", "grade": "5"}
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateAssessmentTestRequest(
            format="xml",
            xml=SAMPLE_QTI_XML,
            metadata={"subject": "Math", "grade": "5"}
        )
        result = create_assessment_test(mock_http, request)
        
        assert result.metadata is not None
        assert mock_http.last_body["metadata"] == {"subject": "Math", "grade": "5"}

    def test_create_assessment_test_format_defaults_to_xml(self) -> None:
        """Test that format defaults to xml."""
        mock_data = create_mock_assessment_test_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateAssessmentTestRequest(xml=SAMPLE_QTI_XML)
        result = create_assessment_test(mock_http, request)
        
        assert mock_http.last_body["format"] == "xml"

    def test_create_assessment_test_excludes_none_values(self) -> None:
        """Test that None values are excluded from the request body."""
        mock_data = create_mock_assessment_test_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateAssessmentTestRequest(
            format="xml",
            xml=SAMPLE_QTI_XML
            # metadata is None by default
        )
        result = create_assessment_test(mock_http, request)
        
        assert "metadata" not in mock_http.last_body

    def test_create_assessment_test_validates_response(self) -> None:
        """Test that response is validated correctly."""
        mock_data = create_mock_assessment_test_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateAssessmentTestRequest(
            format="xml",
            xml=SAMPLE_QTI_XML
        )
        result = create_assessment_test(mock_http, request)
        
        assert result.identifier == "test-001"
        assert result.title == "Test Assessment"
        assert result.qti_version == "3.0"
        assert result.raw_xml is not None

