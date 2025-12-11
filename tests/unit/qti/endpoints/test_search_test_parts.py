"""Unit tests for search_test_parts endpoint.

Tests the search_test_parts function that searches for test parts
within an assessment test.
"""

from typing import Any, Dict, List
import pytest

from timeback.services.qti.endpoints.search_test_parts import search_test_parts
from timeback.models.request import TimebackSearchTestPartsRequest
from timeback.models.response import TimebackSearchTestPartsResponse
from timeback.enums import TimebackQTINavigationMode, TimebackQTISubmissionMode


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


def create_mock_test_part(
    identifier: str = "part-001",
    navigation_mode: str = "linear",
    submission_mode: str = "individual"
) -> Dict[str, Any]:
    """Create mock test part data for testing."""
    return {
        "identifier": identifier,
        "navigationMode": navigation_mode,
        "submissionMode": submission_mode,
        "qti-assessment-section": [
            {
                "identifier": "section-001",
                "title": "Test Section",
                "visible": True,
                "required": True,
                "fixed": False
            }
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
    """Create a mock search_test_parts response."""
    if items is None:
        items = [create_mock_test_part()]
    
    return {
        "items": items,
        "total": total if total is not None else len(items),
        "page": page,
        "pages": pages,
        "limit": limit,
        "sort": sort,
        "order": order
    }


class TestSearchTestParts:
    """Tests for search_test_parts endpoint."""

    def test_search_test_parts_success(self) -> None:
        """Test successful search with default parameters."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        result = search_test_parts(mock_http, "test-001")
        
        assert isinstance(result, TimebackSearchTestPartsResponse)
        assert len(result.items) == 1
        assert result.total == 1
        assert mock_http.last_path == "/assessment-tests/test-001/test-parts"

    def test_search_test_parts_with_query(self) -> None:
        """Test search with query parameter."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchTestPartsRequest(query="part")
        result = search_test_parts(mock_http, "test-001", request)
        
        assert mock_http.last_params["query"] == "part"

    def test_search_test_parts_with_pagination(self) -> None:
        """Test search with pagination parameters."""
        mock_data = create_mock_response(page=2, pages=5, limit=20)
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchTestPartsRequest(page=2, limit=20)
        result = search_test_parts(mock_http, "test-001", request)
        
        assert mock_http.last_params["page"] == "2"
        assert mock_http.last_params["limit"] == "20"
        assert result.page == 2
        assert result.limit == 20

    def test_search_test_parts_with_navigation_mode_filter(self) -> None:
        """Test search with navigation mode filter."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchTestPartsRequest(
            navigation_mode=TimebackQTINavigationMode.LINEAR
        )
        result = search_test_parts(mock_http, "test-001", request)
        
        assert mock_http.last_params["navigationMode"] == "linear"

    def test_search_test_parts_with_submission_mode_filter(self) -> None:
        """Test search with submission mode filter."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchTestPartsRequest(
            submission_mode=TimebackQTISubmissionMode.SIMULTANEOUS
        )
        result = search_test_parts(mock_http, "test-001", request)
        
        assert mock_http.last_params["submissionMode"] == "simultaneous"

    def test_search_test_parts_multiple_results(self) -> None:
        """Test search returning multiple test parts."""
        items = [
            create_mock_test_part("part-001", "linear", "individual"),
            create_mock_test_part("part-002", "nonlinear", "simultaneous"),
        ]
        mock_data = create_mock_response(items=items, total=2)
        mock_http = MockHttpClient(mock_data)
        
        result = search_test_parts(mock_http, "test-001")
        
        assert len(result.items) == 2
        assert result.items[0].identifier == "part-001"
        assert result.items[1].identifier == "part-002"

    def test_search_test_parts_empty_results(self) -> None:
        """Test search returning no results."""
        mock_data = create_mock_response(items=[], total=0)
        mock_http = MockHttpClient(mock_data)
        
        result = search_test_parts(mock_http, "test-001")
        
        assert len(result.items) == 0
        assert result.total == 0

    def test_search_test_parts_validates_test_part_data(self) -> None:
        """Test that test part data is correctly parsed."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        result = search_test_parts(mock_http, "test-001")
        
        part = result.items[0]
        assert part.identifier == "part-001"
        assert part.navigation_mode == TimebackQTINavigationMode.LINEAR
        assert part.submission_mode == TimebackQTISubmissionMode.INDIVIDUAL

    def test_search_test_parts_path_includes_test_identifier(self) -> None:
        """Test that the path correctly includes the assessment test identifier."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        search_test_parts(mock_http, "my-custom-test-id")
        
        assert mock_http.last_path == "/assessment-tests/my-custom-test-id/test-parts"

