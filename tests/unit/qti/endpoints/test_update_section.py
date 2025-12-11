"""Unit tests for update_section endpoint.

Tests the update_section function that updates an existing section.
"""

from typing import Any, Dict
import pytest

from timeback.services.qti.endpoints.update_section import update_section
from timeback.models.request import TimebackUpdateSectionRequest
from timeback.models.response import TimebackUpdateSectionResponse


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


def create_mock_section_response(
    identifier: str = "section-001",
    title: str = "Updated Section"
) -> Dict[str, Any]:
    """Create mock section response data for testing."""
    return {
        "identifier": identifier,
        "title": title,
        "visible": True,
        "required": True,
        "fixed": False,
        "qti-assessment-item-ref": []
    }


class TestUpdateSection:
    """Tests for update_section endpoint."""

    def test_update_section_success(self) -> None:
        """Test successful section update."""
        mock_data = create_mock_section_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateSectionRequest(
            identifier="section-001",
            title="Updated Section"
        )
        result = update_section(mock_http, "test-001", "part-001", "section-001", request)
        
        assert isinstance(result, TimebackUpdateSectionResponse)
        assert result.identifier == "section-001"
        assert result.title == "Updated Section"

    def test_update_section_path_includes_all_identifiers(self) -> None:
        """Test that the path includes all identifiers."""
        mock_data = create_mock_section_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateSectionRequest(
            identifier="my-section",
            title="Updated"
        )
        update_section(mock_http, "my-test", "my-part", "my-section", request)
        
        expected_path = "/assessment-tests/my-test/test-parts/my-part/sections/my-section"
        assert mock_http.last_path == expected_path

    def test_update_section_body_uses_aliases(self) -> None:
        """Test that request body uses API aliases."""
        mock_data = create_mock_section_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateSectionRequest(
            identifier="section-001",
            title="Updated",
            visible=False
        )
        update_section(mock_http, "test-001", "part-001", "section-001", request)
        
        assert mock_http.last_body["identifier"] == "section-001"
        assert mock_http.last_body["title"] == "Updated"
        assert mock_http.last_body["visible"] is False

    def test_update_section_changes_title(self) -> None:
        """Test updating the section title."""
        mock_data = create_mock_section_response(title="New Title")
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateSectionRequest(
            identifier="section-001",
            title="New Title"
        )
        result = update_section(mock_http, "test-001", "part-001", "section-001", request)
        
        assert result.title == "New Title"

    def test_update_section_changes_visibility(self) -> None:
        """Test updating section visibility."""
        mock_data = create_mock_section_response()
        mock_data["visible"] = False
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackUpdateSectionRequest(
            identifier="section-001",
            title="Section",
            visible=False
        )
        result = update_section(mock_http, "test-001", "part-001", "section-001", request)
        
        assert result.visible is False

