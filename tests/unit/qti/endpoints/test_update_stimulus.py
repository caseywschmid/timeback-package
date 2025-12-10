"""Unit tests for update_stimulus endpoint.

Tests the update_stimulus function that updates an existing QTI stimulus.
"""

from typing import Any, Dict
import pytest

from timeback.services.qti.endpoints.update_stimulus import update_stimulus
from timeback.models.request import TimebackUpdateStimulusRequest
from timeback.models.response import TimebackUpdateStimulusResponse
from timeback.models.timeback_qti_stimulus import TimebackQTIStylesheet
from timeback.models.timeback_catalog_entry import TimebackCatalogEntry


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data: Dict[str, Any]):
        """Initialize with the response data to return."""
        self.response_data = response_data
        self.last_path: str = ""
        self.last_json: Dict[str, Any] = {}

    def put(self, path: str, json: Dict[str, Any] = None) -> Dict[str, Any]:
        """Mock PUT request."""
        self.last_path = path
        self.last_json = json or {}
        return self.response_data


def create_mock_stimulus_response(
    identifier: str = "stimulus-001",
    title: str = "Updated Stimulus"
) -> Dict[str, Any]:
    """Create mock stimulus response data."""
    return {
        "identifier": identifier,
        "title": title,
        "catalogInfo": [],
        "language": "en",
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
        "updatedAt": "2024-01-16T14:00:00.000Z"
    }


class TestUpdateStimulus:
    """Tests for update_stimulus endpoint."""

    def test_update_stimulus_success(self) -> None:
        """Test successful update of a stimulus."""
        mock_response = create_mock_stimulus_response()
        mock_http = MockHttpClient(mock_response)
        
        request = TimebackUpdateStimulusRequest(
            identifier="stimulus-001",
            title="Updated Stimulus",
            content="<div>Updated content</div>"
        )
        
        result = update_stimulus(mock_http, request)
        
        assert isinstance(result, TimebackUpdateStimulusResponse)
        assert result.identifier == "stimulus-001"
        assert result.title == "Updated Stimulus"
        
        # Verify request path and body
        assert mock_http.last_path == "/stimuli/stimulus-001"
        assert mock_http.last_json["identifier"] == "stimulus-001"
        assert mock_http.last_json["title"] == "Updated Stimulus"
        assert mock_http.last_json["content"] == "<div>Updated content</div>"

    def test_update_stimulus_with_metadata(self) -> None:
        """Test update with new metadata."""
        mock_response = create_mock_stimulus_response()
        mock_response["metadata"] = {"subject": "Math", "grade": "8"}
        mock_http = MockHttpClient(mock_response)
        
        request = TimebackUpdateStimulusRequest(
            identifier="stimulus-math",
            title="Math Stimulus",
            content="<div>Math content</div>",
            metadata={"subject": "Math", "grade": "8"}
        )
        
        result = update_stimulus(mock_http, request)
        
        assert result.metadata is not None
        assert result.metadata["subject"] == "Math"
        assert mock_http.last_json["metadata"] == {"subject": "Math", "grade": "8"}

    def test_update_stimulus_with_stylesheet(self) -> None:
        """Test update with stylesheet."""
        mock_response = create_mock_stimulus_response()
        mock_response["stylesheet"] = {"href": "new-styles.css", "type": "text/css"}
        mock_http = MockHttpClient(mock_response)
        
        stylesheet = TimebackQTIStylesheet(href="new-styles.css", type="text/css")
        request = TimebackUpdateStimulusRequest(
            identifier="stimulus-styled",
            title="Styled Stimulus",
            content="<div>Content</div>",
            stylesheet=stylesheet
        )
        
        result = update_stimulus(mock_http, request)
        
        assert result.stylesheet is not None
        assert result.stylesheet.href == "new-styles.css"
        assert mock_http.last_json["stylesheet"]["href"] == "new-styles.css"

    def test_update_stimulus_with_catalog_info(self) -> None:
        """Test update with catalog info."""
        mock_response = create_mock_stimulus_response()
        mock_response["catalogInfo"] = [
            {"id": "cat-updated", "support": "braille", "content": "<p>Braille version</p>"}
        ]
        mock_http = MockHttpClient(mock_response)
        
        catalog_entry = TimebackCatalogEntry(
            id="cat-updated",
            support="braille",
            content="<p>Braille version</p>"
        )
        request = TimebackUpdateStimulusRequest(
            identifier="stimulus-accessible",
            title="Accessible Stimulus",
            content="<div>Content</div>",
            catalog_info=[catalog_entry]
        )
        
        result = update_stimulus(mock_http, request)
        
        assert len(result.catalog_info) == 1
        assert result.catalog_info[0].support == "braille"
        assert "catalogInfo" in mock_http.last_json

    def test_update_stimulus_with_tool_info(self) -> None:
        """Test update with tool name and version."""
        mock_response = create_mock_stimulus_response()
        mock_response["toolName"] = "Updated Editor"
        mock_response["toolVersion"] = "3.0.0"
        mock_http = MockHttpClient(mock_response)
        
        request = TimebackUpdateStimulusRequest(
            identifier="stimulus-tool",
            title="Updated Stimulus",
            content="<div>Content</div>",
            tool_name="Updated Editor",
            tool_version="3.0.0"
        )
        
        result = update_stimulus(mock_http, request)
        
        assert result.tool_name == "Updated Editor"
        assert result.tool_version == "3.0.0"
        assert mock_http.last_json["toolName"] == "Updated Editor"
        assert mock_http.last_json["toolVersion"] == "3.0.0"

    def test_update_stimulus_changes_language(self) -> None:
        """Test update with different language."""
        mock_response = create_mock_stimulus_response()
        mock_response["language"] = "fr"
        mock_http = MockHttpClient(mock_response)
        
        request = TimebackUpdateStimulusRequest(
            identifier="stimulus-french",
            title="Stimulus Français",
            content="<div>Contenu en français</div>",
            language="fr"
        )
        
        result = update_stimulus(mock_http, request)
        
        assert result.language == "fr"
        assert mock_http.last_json["language"] == "fr"

    def test_update_stimulus_identifier_in_path(self) -> None:
        """Test that identifier is correctly placed in URL path."""
        mock_response = create_mock_stimulus_response(
            identifier="special-id-123"
        )
        mock_http = MockHttpClient(mock_response)
        
        request = TimebackUpdateStimulusRequest(
            identifier="special-id-123",
            title="Test",
            content="<div>Content</div>"
        )
        
        update_stimulus(mock_http, request)
        
        assert mock_http.last_path == "/stimuli/special-id-123"

    def test_update_stimulus_excludes_none_values(self) -> None:
        """Test that None values are excluded from request body."""
        mock_response = create_mock_stimulus_response()
        mock_http = MockHttpClient(mock_response)
        
        request = TimebackUpdateStimulusRequest(
            identifier="stimulus-minimal",
            title="Minimal Update",
            content="<div>Content</div>"
        )
        
        update_stimulus(mock_http, request)
        
        # Should have required fields
        assert "identifier" in mock_http.last_json
        assert "title" in mock_http.last_json
        assert "content" in mock_http.last_json
        # Should not have None fields
        assert "stylesheet" not in mock_http.last_json
        assert "catalogInfo" not in mock_http.last_json
        assert "metadata" not in mock_http.last_json

