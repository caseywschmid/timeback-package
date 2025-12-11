"""Unit tests for search_sections endpoint.

Tests the search_sections function that searches for sections
within a test part.
"""

from typing import Any, Dict, List
import pytest

from timeback.services.qti.endpoints.search_sections import search_sections
from timeback.models.request import TimebackSearchSectionsRequest
from timeback.models.response import TimebackSearchSectionsResponse


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data: Dict[str, Any]):
        """Initialize with the response data to return."""
        self.response_data = response_data
        self.last_path: str = ""
        self.last_params: Dict[str, Any] = {}

    def get(self, path: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """Mock GET request."""
        self.last_path = path
        self.last_params = params or {}
        return self.response_data


def create_mock_section(
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
            {"identifier": "item-001", "href": "/assessment-items/item-001"}
        ]
    }


def create_mock_response(
    items: List[Dict[str, Any]] = None,
    total: int = None,
    page: int = 1,
    pages: int = 1,
    limit: int = 10,
    sort: str = "createdAt",
    order: str = "desc"
) -> Dict[str, Any]:
    """Create a mock search_sections response."""
    if items is None:
        items = [create_mock_section()]
    
    return {
        "items": items,
        "total": total if total is not None else len(items),
        "page": page,
        "pages": pages,
        "limit": limit,
        "sort": sort,
        "order": order
    }


class TestSearchSections:
    """Tests for search_sections endpoint."""

    def test_search_sections_success(self) -> None:
        """Test successful search with default parameters."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        result = search_sections(mock_http, "test-001", "part-001")
        
        assert isinstance(result, TimebackSearchSectionsResponse)
        assert len(result.items) == 1
        assert result.total == 1
        assert mock_http.last_path == "/assessment-tests/test-001/test-parts/part-001/sections"

    def test_search_sections_with_query(self) -> None:
        """Test search with query parameter."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchSectionsRequest(query="intro")
        result = search_sections(mock_http, "test-001", "part-001", request)
        
        assert mock_http.last_params["query"] == "intro"

    def test_search_sections_with_pagination(self) -> None:
        """Test search with pagination parameters."""
        mock_data = create_mock_response(page=2, pages=5, limit=20)
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchSectionsRequest(page=2, limit=20)
        result = search_sections(mock_http, "test-001", "part-001", request)
        
        assert mock_http.last_params["page"] == "2"
        assert mock_http.last_params["limit"] == "20"
        assert result.page == 2
        assert result.limit == 20

    def test_search_sections_multiple_results(self) -> None:
        """Test search returning multiple sections."""
        items = [
            create_mock_section("section-001", "Section 1"),
            create_mock_section("section-002", "Section 2"),
            create_mock_section("section-003", "Section 3"),
        ]
        mock_data = create_mock_response(items=items, total=3)
        mock_http = MockHttpClient(mock_data)
        
        result = search_sections(mock_http, "test-001", "part-001")
        
        assert len(result.items) == 3
        assert result.items[0].identifier == "section-001"
        assert result.items[1].identifier == "section-002"
        assert result.items[2].identifier == "section-003"

    def test_search_sections_empty_results(self) -> None:
        """Test search returning no results."""
        mock_data = create_mock_response(items=[], total=0)
        mock_http = MockHttpClient(mock_data)
        
        result = search_sections(mock_http, "test-001", "part-001")
        
        assert len(result.items) == 0
        assert result.total == 0

    def test_search_sections_path_includes_all_identifiers(self) -> None:
        """Test that the path includes test and part identifiers."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        search_sections(mock_http, "my-test", "my-part")
        
        assert mock_http.last_path == "/assessment-tests/my-test/test-parts/my-part/sections"

    def test_search_sections_validates_section_data(self) -> None:
        """Test that section data is correctly parsed."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        result = search_sections(mock_http, "test-001", "part-001")
        
        section = result.items[0]
        assert section.identifier == "section-001"
        assert section.title == "Test Section"
        assert section.visible is True

    def test_search_sections_includes_item_refs(self) -> None:
        """Test that item references are included."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        result = search_sections(mock_http, "test-001", "part-001")
        
        section = result.items[0]
        assert section.qti_assessment_item_ref is not None
        assert len(section.qti_assessment_item_ref) == 1
        assert section.qti_assessment_item_ref[0].identifier == "item-001"

