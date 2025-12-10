"""Unit tests for get_stimulus endpoint.

Tests the get_stimulus function that retrieves a specific QTI stimulus by identifier.
"""

from typing import Any, Dict
import pytest

from timeback.services.qti.endpoints.get_stimulus import get_stimulus
from timeback.models.response import TimebackGetStimulusResponse


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


def create_mock_stimulus_data(
    identifier: str = "stimulus-001",
    title: str = "Test Stimulus"
) -> Dict[str, Any]:
    """Create mock stimulus data for testing."""
    return {
        "identifier": identifier,
        "title": title,
        "catalogInfo": [
            {
                "id": "catalog-1",
                "support": "spoken",
                "content": "<p>Read aloud text</p>"
            }
        ],
        "label": "Test Label",
        "language": "en",
        "stylesheet": {
            "href": "styles.css",
            "type": "text/css"
        },
        "toolName": "QTI Editor",
        "toolVersion": "1.0.0",
        "metadata": {
            "subject": "Science",
            "grade": "7"
        },
        "rawXml": f'<?xml version="1.0"?><qti-assessment-stimulus identifier="{identifier}" title="{title}"></qti-assessment-stimulus>',
        "content": {
            "qti-assessment-stimulus": {
                "_attributes": {
                    "identifier": identifier,
                    "title": title
                }
            }
        },
        "createdAt": "2024-01-15T10:30:00.000Z",
        "updatedAt": "2024-01-15T10:30:00.000Z"
    }


class TestGetStimulus:
    """Tests for get_stimulus endpoint."""

    def test_get_stimulus_success(self) -> None:
        """Test successful retrieval of a stimulus."""
        mock_data = create_mock_stimulus_data()
        mock_http = MockHttpClient(mock_data)
        
        result = get_stimulus(mock_http, "stimulus-001")
        
        assert isinstance(result, TimebackGetStimulusResponse)
        assert result.identifier == "stimulus-001"
        assert result.title == "Test Stimulus"
        assert result.language == "en"
        assert result.raw_xml is not None
        assert result.created_at is not None
        assert result.updated_at is not None
        
        # Verify request path
        assert mock_http.last_path == "/stimuli/stimulus-001"

    def test_get_stimulus_validates_all_fields(self) -> None:
        """Test that all stimulus fields are correctly parsed."""
        mock_data = create_mock_stimulus_data(
            identifier="stimulus-full",
            title="Complete Stimulus"
        )
        mock_http = MockHttpClient(mock_data)
        
        result = get_stimulus(mock_http, "stimulus-full")
        
        # Verify all fields
        assert result.identifier == "stimulus-full"
        assert result.title == "Complete Stimulus"
        assert result.label == "Test Label"
        assert result.language == "en"
        assert result.tool_name == "QTI Editor"
        assert result.tool_version == "1.0.0"
        
        # Verify catalog info
        assert len(result.catalog_info) == 1
        assert result.catalog_info[0].id == "catalog-1"
        assert result.catalog_info[0].support == "spoken"
        
        # Verify stylesheet
        assert result.stylesheet is not None
        assert result.stylesheet.href == "styles.css"
        assert result.stylesheet.type == "text/css"
        
        # Verify metadata
        assert result.metadata is not None
        assert result.metadata["subject"] == "Science"
        assert result.metadata["grade"] == "7"

    def test_get_stimulus_minimal_fields(self) -> None:
        """Test retrieval with minimal required fields."""
        minimal_data = {
            "identifier": "min-stimulus",
            "title": "Minimal Stimulus",
            "catalogInfo": [],
            "rawXml": "<qti-assessment-stimulus></qti-assessment-stimulus>",
            "createdAt": "2024-01-15T10:30:00.000Z",
            "updatedAt": "2024-01-15T10:30:00.000Z"
        }
        mock_http = MockHttpClient(minimal_data)
        
        result = get_stimulus(mock_http, "min-stimulus")
        
        assert result.identifier == "min-stimulus"
        assert result.title == "Minimal Stimulus"
        assert len(result.catalog_info) == 0
        assert result.stylesheet is None
        assert result.metadata is None
        assert result.label is None

    def test_get_stimulus_with_special_characters(self) -> None:
        """Test retrieval with special characters in identifier."""
        mock_data = create_mock_stimulus_data(
            identifier="stimulus-with-special_chars.123",
            title="Special Stimulus"
        )
        mock_http = MockHttpClient(mock_data)
        
        result = get_stimulus(mock_http, "stimulus-with-special_chars.123")
        
        assert result.identifier == "stimulus-with-special_chars.123"
        assert mock_http.last_path == "/stimuli/stimulus-with-special_chars.123"

    def test_get_stimulus_raw_xml_content(self) -> None:
        """Test that rawXml content is properly returned."""
        xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<qti-assessment-stimulus
    xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
    identifier="rich-stimulus"
    title="Rich Content">
    <qti-stimulus-body>
        <div class="content">
            <h2>Heading</h2>
            <p>Paragraph with <strong>bold</strong> text.</p>
        </div>
    </qti-stimulus-body>
</qti-assessment-stimulus>'''
        
        mock_data = create_mock_stimulus_data()
        mock_data["rawXml"] = xml_content
        mock_http = MockHttpClient(mock_data)
        
        result = get_stimulus(mock_http, "stimulus-001")
        
        assert result.raw_xml == xml_content
        assert "<qti-assessment-stimulus" in result.raw_xml
        assert "<qti-stimulus-body>" in result.raw_xml

    def test_get_stimulus_with_complex_metadata(self) -> None:
        """Test retrieval with complex nested metadata."""
        mock_data = create_mock_stimulus_data()
        mock_data["metadata"] = {
            "subject": "Science",
            "grade": "7",
            "standards": ["NGSS.MS-LS2-1", "NGSS.MS-LS2-2"],
            "difficulty": {
                "level": "medium",
                "score": 0.65
            },
            "tags": ["ecosystem", "biodiversity", "reading"]
        }
        mock_http = MockHttpClient(mock_data)
        
        result = get_stimulus(mock_http, "stimulus-001")
        
        assert result.metadata is not None
        assert result.metadata["subject"] == "Science"
        assert result.metadata["standards"] == ["NGSS.MS-LS2-1", "NGSS.MS-LS2-2"]
        assert result.metadata["difficulty"]["level"] == "medium"
        assert "ecosystem" in result.metadata["tags"]

