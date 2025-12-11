"""Unit tests for get_section endpoint.

Tests the get_section function that retrieves a specific section.
"""

from typing import Any, Dict
import pytest

from timeback.services.qti.endpoints.get_section import get_section
from timeback.models.response import TimebackGetSectionResponse


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


def create_mock_section_data(
    identifier: str = "section-001",
    title: str = "Test Section"
) -> Dict[str, Any]:
    """Create mock section data for testing."""
    return {
        "identifier": identifier,
        "title": title,
        "visible": True,
        "required": True,
        "fixed": False,
        "qti-assessment-item-ref": [
            {"identifier": "item-001", "href": "/assessment-items/item-001"},
            {"identifier": "item-002", "href": "/assessment-items/item-002"},
        ]
    }


class TestGetSection:
    """Tests for get_section endpoint."""

    def test_get_section_success(self) -> None:
        """Test successful retrieval of a section."""
        mock_data = create_mock_section_data()
        mock_http = MockHttpClient(mock_data)
        
        result = get_section(mock_http, "test-001", "part-001", "section-001")
        
        assert isinstance(result, TimebackGetSectionResponse)
        assert result.identifier == "section-001"
        assert result.title == "Test Section"

    def test_get_section_path_includes_all_identifiers(self) -> None:
        """Test that the path includes all identifiers."""
        mock_data = create_mock_section_data()
        mock_http = MockHttpClient(mock_data)
        
        get_section(mock_http, "my-test", "my-part", "my-section")
        
        expected_path = "/assessment-tests/my-test/test-parts/my-part/sections/my-section"
        assert mock_http.last_path == expected_path

    def test_get_section_includes_item_refs(self) -> None:
        """Test that item references are included."""
        mock_data = create_mock_section_data()
        mock_http = MockHttpClient(mock_data)
        
        result = get_section(mock_http, "test-001", "part-001", "section-001")
        
        assert result.qti_assessment_item_ref is not None
        assert len(result.qti_assessment_item_ref) == 2
        assert result.qti_assessment_item_ref[0].identifier == "item-001"

    def test_get_section_validates_response(self) -> None:
        """Test that response is validated correctly."""
        mock_data = create_mock_section_data()
        mock_http = MockHttpClient(mock_data)
        
        result = get_section(mock_http, "test-001", "part-001", "section-001")
        
        assert result.visible is True
        assert result.required is True
        assert result.fixed is False

