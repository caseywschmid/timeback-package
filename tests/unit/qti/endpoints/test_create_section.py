"""Unit tests for create_section endpoint.

Tests the create_section function that creates a new section
within a test part.
"""

from typing import Any, Dict
import pytest

from timeback.services.qti.endpoints.create_section import create_section
from timeback.models.request import TimebackCreateSectionRequest
from timeback.models.response import TimebackCreateSectionResponse
from timeback.models.timeback_qti_item_ref import TimebackQTIItemRef


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


def create_mock_section_response(
    identifier: str = "section-001",
    title: str = "Test Section"
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


class TestCreateSection:
    """Tests for create_section endpoint."""

    def test_create_section_success(self) -> None:
        """Test successful section creation."""
        mock_data = create_mock_section_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateSectionRequest(
            identifier="section-001",
            title="Test Section"
        )
        result = create_section(mock_http, "test-001", "part-001", request)
        
        assert isinstance(result, TimebackCreateSectionResponse)
        assert result.identifier == "section-001"
        assert mock_http.last_path == "/assessment-tests/test-001/test-parts/part-001/sections"

    def test_create_section_path_includes_all_identifiers(self) -> None:
        """Test that the path includes test and part identifiers."""
        mock_data = create_mock_section_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateSectionRequest(
            identifier="section-001",
            title="Test Section"
        )
        create_section(mock_http, "my-test", "my-part", request)
        
        assert mock_http.last_path == "/assessment-tests/my-test/test-parts/my-part/sections"

    def test_create_section_body_contains_required_fields(self) -> None:
        """Test that request body contains required fields."""
        mock_data = create_mock_section_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateSectionRequest(
            identifier="section-001",
            title="My Section",
            visible=False
        )
        create_section(mock_http, "test-001", "part-001", request)
        
        assert mock_http.last_body["identifier"] == "section-001"
        assert mock_http.last_body["title"] == "My Section"
        assert mock_http.last_body["visible"] is False

    def test_create_section_with_item_refs(self) -> None:
        """Test creating section with item references."""
        mock_data = create_mock_section_response()
        mock_data["qti-assessment-item-ref"] = [
            {"identifier": "item-001", "href": "/assessment-items/item-001"}
        ]
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateSectionRequest(
            identifier="section-001",
            title="Test Section",
            qti_assessment_item_ref=[
                TimebackQTIItemRef(identifier="item-001", href="/assessment-items/item-001")
            ]
        )
        result = create_section(mock_http, "test-001", "part-001", request)
        
        assert result.qti_assessment_item_ref is not None
        assert len(result.qti_assessment_item_ref) == 1

    def test_create_section_excludes_none_values(self) -> None:
        """Test that None values are excluded from request body."""
        mock_data = create_mock_section_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateSectionRequest(
            identifier="section-001",
            title="Test Section"
            # required, fixed, sequence are None
        )
        create_section(mock_http, "test-001", "part-001", request)
        
        assert "required" not in mock_http.last_body or mock_http.last_body.get("required") is None
        assert "sequence" not in mock_http.last_body

    def test_create_section_validates_response(self) -> None:
        """Test that response is validated correctly."""
        mock_data = create_mock_section_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackCreateSectionRequest(
            identifier="section-001",
            title="Test Section"
        )
        result = create_section(mock_http, "test-001", "part-001", request)
        
        assert result.identifier == "section-001"
        assert result.title == "Test Section"
        assert result.visible is True

