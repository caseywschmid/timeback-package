"""Unit tests for update_assessment_test endpoint.

Tests the update_assessment_test function that updates an existing QTI assessment test.
"""

from typing import Any, Dict
import pytest

from timeback.services.qti.endpoints.update_assessment_test import update_assessment_test
from timeback.models.request import TimebackUpdateAssessmentTestRequest
from timeback.models.response import TimebackUpdateAssessmentTestResponse


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
    title: str = "Updated Test"
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
        "updatedAt": "2024-01-02T00:00:00Z"
    }


SAMPLE_UPDATED_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<qti-assessment-test
  xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
  identifier="sample-test-1"
  title="Updated Test">
  <qti-test-part identifier="part-1" navigation-mode="nonlinear" submission-mode="simultaneous">
    <qti-assessment-section identifier="section-1" title="Updated Section" visible="true">
      <qti-assessment-item-ref identifier="item-1" href="/assessment-items/item-1"/>
      <qti-assessment-item-ref identifier="item-2" href="/assessment-items/item-2"/>
    </qti-assessment-section>
  </qti-test-part>
</qti-assessment-test>'''


class TestUpdateAssessmentTest:
    """Tests for update_assessment_test endpoint."""

    def test_update_assessment_test_success(self) -> None:
        """Test successful update of an assessment test."""
        mock_data = create_mock_assessment_test_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentTestRequest(
            format="xml",
            xml=SAMPLE_UPDATED_XML
        )
        result = update_assessment_test(mock_http, "test-001", request)
        
        assert isinstance(result, TimebackUpdateAssessmentTestResponse)
        assert result.identifier == "test-001"
        assert mock_http.last_path == "/assessment-tests/test-001"
        assert mock_http.last_body["format"] == "xml"

    def test_update_assessment_test_with_different_identifier(self) -> None:
        """Test that the identifier is correctly placed in the path."""
        mock_data = create_mock_assessment_test_data(identifier="math-test-99")
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentTestRequest(
            format="xml",
            xml=SAMPLE_UPDATED_XML
        )
        result = update_assessment_test(mock_http, "math-test-99", request)
        
        assert result.identifier == "math-test-99"
        assert mock_http.last_path == "/assessment-tests/math-test-99"

    def test_update_assessment_test_with_metadata(self) -> None:
        """Test update with metadata changes."""
        mock_data = create_mock_assessment_test_data()
        mock_data["metadata"] = {"subject": "Science", "version": "2.0"}
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentTestRequest(
            format="xml",
            xml=SAMPLE_UPDATED_XML,
            metadata={"subject": "Science", "version": "2.0"}
        )
        result = update_assessment_test(mock_http, "test-001", request)
        
        assert result.metadata["subject"] == "Science"
        assert mock_http.last_body["metadata"] == {"subject": "Science", "version": "2.0"}

    def test_update_assessment_test_excludes_none_values(self) -> None:
        """Test that None values are excluded from the request body."""
        mock_data = create_mock_assessment_test_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentTestRequest(
            format="xml",
            xml=SAMPLE_UPDATED_XML
            # metadata is None by default
        )
        result = update_assessment_test(mock_http, "test-001", request)
        
        assert "metadata" not in mock_http.last_body

    def test_update_assessment_test_format_defaults_to_xml(self) -> None:
        """Test that format defaults to xml."""
        mock_data = create_mock_assessment_test_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentTestRequest(xml=SAMPLE_UPDATED_XML)
        result = update_assessment_test(mock_http, "test-001", request)
        
        assert mock_http.last_body["format"] == "xml"

    def test_update_assessment_test_validates_response(self) -> None:
        """Test that response is validated correctly."""
        mock_data = create_mock_assessment_test_data()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateAssessmentTestRequest(
            format="xml",
            xml=SAMPLE_UPDATED_XML
        )
        result = update_assessment_test(mock_http, "test-001", request)
        
        assert result.title == "Updated Test"
        assert result.qti_version == "3.0"
        assert result.raw_xml is not None

