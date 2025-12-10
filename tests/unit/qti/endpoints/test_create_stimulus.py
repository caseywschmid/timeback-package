"""Unit tests for create_stimulus endpoint.

Tests the create_stimulus function that creates a new QTI stimulus.
"""

from typing import Any, Dict
from datetime import datetime
import pytest

from timeback.services.qti.endpoints.create_stimulus import create_stimulus
from timeback.models.request import TimebackCreateStimulusRequest
from timeback.models.response import TimebackCreateStimulusResponse
from timeback.models.timeback_qti_stimulus import TimebackQTIStylesheet
from timeback.models.timeback_catalog_entry import TimebackCatalogEntry


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data: Dict[str, Any]):
        """Initialize with the response data to return."""
        self.response_data = response_data
        self.last_path: str = ""
        self.last_json: Dict[str, Any] = {}

    def post(self, path: str, json: Dict[str, Any] = None) -> Dict[str, Any]:
        """Mock POST request."""
        self.last_path = path
        self.last_json = json or {}
        return self.response_data


def create_mock_stimulus_response(
    identifier: str = "stimulus-001",
    title: str = "Test Stimulus",
    content_html: str = "<div>Test content</div>"
) -> Dict[str, Any]:
    """Create mock stimulus response data."""
    return {
        "identifier": identifier,
        "title": title,
        "catalogInfo": [],
        "language": "en",
        "rawXml": f'<?xml version="1.0"?><qti-assessment-stimulus identifier="{identifier}" title="{title}"><qti-stimulus-body>{content_html}</qti-stimulus-body></qti-assessment-stimulus>',
        "content": {
            "qti-assessment-stimulus": {
                "_attributes": {
                    "identifier": identifier,
                    "title": title
                },
                "qti-stimulus-body": {}
            }
        },
        "createdAt": "2024-01-15T10:30:00.000Z",
        "updatedAt": "2024-01-15T10:30:00.000Z"
    }


class TestCreateStimulus:
    """Tests for create_stimulus endpoint."""

    def test_create_stimulus_success_minimal(self) -> None:
        """Test successful creation with minimal required fields."""
        mock_response = create_mock_stimulus_response()
        mock_http = MockHttpClient(mock_response)
        
        request = TimebackCreateStimulusRequest(
            identifier="stimulus-001",
            title="Test Stimulus",
            content="<div>Test content</div>"
        )
        
        result = create_stimulus(mock_http, request)
        
        assert isinstance(result, TimebackCreateStimulusResponse)
        assert result.identifier == "stimulus-001"
        assert result.title == "Test Stimulus"
        assert result.raw_xml is not None
        assert result.created_at is not None
        assert result.updated_at is not None
        
        # Verify request was made correctly
        assert mock_http.last_path == "/stimuli"
        assert mock_http.last_json["identifier"] == "stimulus-001"
        assert mock_http.last_json["title"] == "Test Stimulus"
        assert mock_http.last_json["content"] == "<div>Test content</div>"

    def test_create_stimulus_with_metadata(self) -> None:
        """Test creation with custom metadata."""
        mock_response = create_mock_stimulus_response()
        mock_response["metadata"] = {"subject": "Science", "grade": "7"}
        mock_http = MockHttpClient(mock_response)
        
        request = TimebackCreateStimulusRequest(
            identifier="stimulus-science",
            title="Science Stimulus",
            content="<div>Science content</div>",
            metadata={"subject": "Science", "grade": "7"}
        )
        
        result = create_stimulus(mock_http, request)
        
        assert result.metadata is not None
        assert result.metadata["subject"] == "Science"
        assert result.metadata["grade"] == "7"
        assert mock_http.last_json["metadata"] == {"subject": "Science", "grade": "7"}

    def test_create_stimulus_with_language(self) -> None:
        """Test creation with custom language."""
        mock_response = create_mock_stimulus_response()
        mock_response["language"] = "es"
        mock_http = MockHttpClient(mock_response)
        
        request = TimebackCreateStimulusRequest(
            identifier="stimulus-spanish",
            title="Spanish Stimulus",
            content="<div>Contenido en español</div>",
            language="es"
        )
        
        result = create_stimulus(mock_http, request)
        
        assert result.language == "es"
        assert mock_http.last_json["language"] == "es"

    def test_create_stimulus_with_label(self) -> None:
        """Test creation with a label."""
        mock_response = create_mock_stimulus_response()
        mock_response["label"] = "Test Label"
        mock_http = MockHttpClient(mock_response)
        
        request = TimebackCreateStimulusRequest(
            identifier="stimulus-labeled",
            title="Labeled Stimulus",
            content="<div>Content</div>",
            label="Test Label"
        )
        
        result = create_stimulus(mock_http, request)
        
        assert result.label == "Test Label"
        assert mock_http.last_json["label"] == "Test Label"

    def test_create_stimulus_with_stylesheet(self) -> None:
        """Test creation with stylesheet reference."""
        mock_response = create_mock_stimulus_response()
        mock_response["stylesheet"] = {"href": "styles.css", "type": "text/css"}
        mock_http = MockHttpClient(mock_response)
        
        stylesheet = TimebackQTIStylesheet(href="styles.css", type="text/css")
        request = TimebackCreateStimulusRequest(
            identifier="stimulus-styled",
            title="Styled Stimulus",
            content="<div>Styled content</div>",
            stylesheet=stylesheet
        )
        
        result = create_stimulus(mock_http, request)
        
        assert result.stylesheet is not None
        assert result.stylesheet.href == "styles.css"
        assert result.stylesheet.type == "text/css"
        assert mock_http.last_json["stylesheet"]["href"] == "styles.css"
        assert mock_http.last_json["stylesheet"]["type"] == "text/css"

    def test_create_stimulus_with_catalog_info(self) -> None:
        """Test creation with catalog info for accessibility."""
        mock_response = create_mock_stimulus_response()
        mock_response["catalogInfo"] = [
            {"id": "cat-1", "support": "spoken", "content": "<p>Audio description</p>"}
        ]
        mock_http = MockHttpClient(mock_response)
        
        catalog_entry = TimebackCatalogEntry(
            id="cat-1",
            support="spoken",
            content="<p>Audio description</p>"
        )
        request = TimebackCreateStimulusRequest(
            identifier="stimulus-accessible",
            title="Accessible Stimulus",
            content="<div>Accessible content</div>",
            catalog_info=[catalog_entry]
        )
        
        result = create_stimulus(mock_http, request)
        
        assert len(result.catalog_info) == 1
        assert result.catalog_info[0].id == "cat-1"
        assert result.catalog_info[0].support == "spoken"
        # Verify alias is used in the request
        assert "catalogInfo" in mock_http.last_json
        assert mock_http.last_json["catalogInfo"][0]["id"] == "cat-1"

    def test_create_stimulus_with_tool_info(self) -> None:
        """Test creation with tool name and version."""
        mock_response = create_mock_stimulus_response()
        mock_response["toolName"] = "QTI Editor"
        mock_response["toolVersion"] = "2.0.0"
        mock_http = MockHttpClient(mock_response)
        
        request = TimebackCreateStimulusRequest(
            identifier="stimulus-tool",
            title="Tool-created Stimulus",
            content="<div>Content</div>",
            tool_name="QTI Editor",
            tool_version="2.0.0"
        )
        
        result = create_stimulus(mock_http, request)
        
        assert result.tool_name == "QTI Editor"
        assert result.tool_version == "2.0.0"
        # Verify aliases are used in the request
        assert mock_http.last_json["toolName"] == "QTI Editor"
        assert mock_http.last_json["toolVersion"] == "2.0.0"

    def test_create_stimulus_with_all_fields(self) -> None:
        """Test creation with all optional fields."""
        mock_response = create_mock_stimulus_response(
            identifier="stimulus-full",
            title="Full Stimulus"
        )
        mock_response["label"] = "Complete Example"
        mock_response["language"] = "en-US"
        mock_response["stylesheet"] = {"href": "main.css", "type": "text/css"}
        mock_response["catalogInfo"] = [
            {"id": "cat-1", "support": "spoken", "content": "<p>Narration</p>"}
        ]
        mock_response["toolName"] = "Timeback SDK"
        mock_response["toolVersion"] = "1.0.0"
        mock_response["metadata"] = {"subject": "Math", "difficulty": "easy"}
        mock_http = MockHttpClient(mock_response)
        
        stylesheet = TimebackQTIStylesheet(href="main.css", type="text/css")
        catalog_entry = TimebackCatalogEntry(
            id="cat-1",
            support="spoken",
            content="<p>Narration</p>"
        )
        
        request = TimebackCreateStimulusRequest(
            identifier="stimulus-full",
            title="Full Stimulus",
            content="<div>Complete content</div>",
            format="json",
            label="Complete Example",
            language="en-US",
            stylesheet=stylesheet,
            catalog_info=[catalog_entry],
            tool_name="Timeback SDK",
            tool_version="1.0.0",
            metadata={"subject": "Math", "difficulty": "easy"}
        )
        
        result = create_stimulus(mock_http, request)
        
        assert result.identifier == "stimulus-full"
        assert result.title == "Full Stimulus"
        assert result.label == "Complete Example"
        assert result.language == "en-US"
        assert result.stylesheet is not None
        assert len(result.catalog_info) == 1
        assert result.tool_name == "Timeback SDK"
        assert result.tool_version == "1.0.0"
        assert result.metadata is not None

    def test_create_stimulus_excludes_none_values(self) -> None:
        """Test that None values are excluded from the request body."""
        mock_response = create_mock_stimulus_response()
        mock_http = MockHttpClient(mock_response)
        
        request = TimebackCreateStimulusRequest(
            identifier="stimulus-minimal",
            title="Minimal Stimulus",
            content="<div>Content</div>"
        )
        
        create_stimulus(mock_http, request)
        
        # Should only have required fields + defaults
        assert "identifier" in mock_http.last_json
        assert "title" in mock_http.last_json
        assert "content" in mock_http.last_json
        # Optional fields should not be present when None
        assert "xml" not in mock_http.last_json
        assert "stylesheet" not in mock_http.last_json
        assert "catalogInfo" not in mock_http.last_json
        assert "toolName" not in mock_http.last_json
        assert "toolVersion" not in mock_http.last_json
        assert "metadata" not in mock_http.last_json

    def test_create_stimulus_html_content_format(self) -> None:
        """Test that HTML content with special characters is preserved."""
        html_content = """<div class="stimulus">
            <h2>Test &amp; Verify</h2>
            <p>Content with <strong>formatting</strong></p>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
            </ul>
        </div>"""
        
        mock_response = create_mock_stimulus_response()
        mock_http = MockHttpClient(mock_response)
        
        request = TimebackCreateStimulusRequest(
            identifier="stimulus-html",
            title="HTML Stimulus",
            content=html_content
        )
        
        create_stimulus(mock_http, request)
        
        # HTML content should be preserved exactly
        assert mock_http.last_json["content"] == html_content

