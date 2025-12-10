"""Unit tests for search_assessment_tests endpoint.

Tests the search_assessment_tests function that retrieves a paginated list of QTI assessment tests.
"""

from typing import Any, Dict, List
import pytest

from timeback.services.qti.endpoints.search_assessment_tests import search_assessment_tests
from timeback.models.request import TimebackSearchAssessmentTestsRequest
from timeback.models.response import TimebackSearchAssessmentTestsResponse
from timeback.enums import (
    TimebackQTIAssessmentTestSortField,
    TimebackSortOrder,
    TimebackQTINavigationMode,
    TimebackQTISubmissionMode,
)


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


def create_mock_assessment_test_data(
    identifier: str = "test-001",
    title: str = "Test Assessment"
) -> Dict[str, Any]:
    """Create mock assessment test data for testing."""
    return {
        "identifier": identifier,
        "title": title,
        "qtiVersion": "3.0",
        "qti-test-part": [
            {
                "identifier": "part-1",
                "navigationMode": "linear",
                "submissionMode": "individual",
                "qti-assessment-section": [
                    {
                        "identifier": "section-1",
                        "title": "Section 1",
                        "visible": True,
                        "qti-assessment-item-ref": [
                            {"identifier": "item-1", "href": "/assessment-items/item-1"}
                        ]
                    }
                ]
            }
        ],
        "qti-outcome-declaration": [
            {
                "identifier": "SCORE",
                "cardinality": "single",
                "baseType": "float"
            }
        ],
        "rawXml": '<?xml version="1.0"?><qti-assessment-test></qti-assessment-test>',
        "createdAt": "2024-01-01T00:00:00Z",
        "updatedAt": "2024-01-01T00:00:00Z"
    }


def create_mock_response(
    items: List[Dict[str, Any]] = None,
    total: int = 1,
    page: int = 1,
    pages: int = 1,
    limit: int = 10,
    sort: str = "createdAt",
    order: str = "desc"
) -> Dict[str, Any]:
    """Create a mock search response."""
    if items is None:
        items = [create_mock_assessment_test_data()]
    
    return {
        "items": items,
        "total": total,
        "page": page,
        "pages": pages,
        "limit": limit,
        "sort": sort,
        "order": order
    }


class TestSearchAssessmentTests:
    """Tests for search_assessment_tests endpoint."""

    def test_search_assessment_tests_success_default_params(self) -> None:
        """Test successful search with default parameters."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        result = search_assessment_tests(mock_http)
        
        assert isinstance(result, TimebackSearchAssessmentTestsResponse)
        assert len(result.items) == 1
        assert result.total == 1
        assert result.page == 1
        assert result.pages == 1
        assert result.limit == 10
        assert result.order == TimebackSortOrder.DESC
        
        # Verify request was made with default params
        assert mock_http.last_path == "/assessment-tests"
        assert mock_http.last_params["page"] == "1"
        assert mock_http.last_params["limit"] == "10"
        assert mock_http.last_params["order"] == "desc"

    def test_search_assessment_tests_with_query(self) -> None:
        """Test search with a query parameter."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchAssessmentTestsRequest(query="math test")
        result = search_assessment_tests(mock_http, request)
        
        assert isinstance(result, TimebackSearchAssessmentTestsResponse)
        assert mock_http.last_params["query"] == "math test"

    def test_search_assessment_tests_with_navigation_mode(self) -> None:
        """Test search filtered by navigation mode."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchAssessmentTestsRequest(
            navigation_mode=TimebackQTINavigationMode.LINEAR
        )
        result = search_assessment_tests(mock_http, request)
        
        assert mock_http.last_params["navigationMode"] == "linear"

    def test_search_assessment_tests_with_submission_mode(self) -> None:
        """Test search filtered by submission mode."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchAssessmentTestsRequest(
            submission_mode=TimebackQTISubmissionMode.SIMULTANEOUS
        )
        result = search_assessment_tests(mock_http, request)
        
        assert mock_http.last_params["submissionMode"] == "simultaneous"

    def test_search_assessment_tests_with_pagination(self) -> None:
        """Test search with custom pagination parameters."""
        mock_data = create_mock_response(
            total=50,
            page=3,
            pages=5,
            limit=10
        )
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchAssessmentTestsRequest(page=3, limit=10)
        result = search_assessment_tests(mock_http, request)
        
        assert result.page == 3
        assert result.pages == 5
        assert result.total == 50
        assert mock_http.last_params["page"] == "3"
        assert mock_http.last_params["limit"] == "10"

    def test_search_assessment_tests_with_sorting(self) -> None:
        """Test search with sorting parameters."""
        mock_data = create_mock_response(sort="title", order="asc")
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchAssessmentTestsRequest(
            sort=TimebackQTIAssessmentTestSortField.TITLE,
            order=TimebackSortOrder.ASC
        )
        result = search_assessment_tests(mock_http, request)
        
        assert result.sort == "title"
        assert result.order == TimebackSortOrder.ASC
        assert mock_http.last_params["sort"] == "title"
        assert mock_http.last_params["order"] == "asc"

    def test_search_assessment_tests_multiple_tests(self) -> None:
        """Test search returning multiple tests."""
        items = [
            create_mock_assessment_test_data("test-001", "Math Test"),
            create_mock_assessment_test_data("test-002", "Science Test"),
            create_mock_assessment_test_data("test-003", "English Test"),
        ]
        mock_data = create_mock_response(items=items, total=3)
        mock_http = MockHttpClient(mock_data)
        
        result = search_assessment_tests(mock_http)
        
        assert len(result.items) == 3
        assert result.total == 3
        assert result.items[0].identifier == "test-001"
        assert result.items[0].title == "Math Test"
        assert result.items[1].identifier == "test-002"
        assert result.items[2].identifier == "test-003"

    def test_search_assessment_tests_empty_results(self) -> None:
        """Test search returning no results."""
        mock_data = create_mock_response(items=[], total=0, pages=0)
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchAssessmentTestsRequest(query="nonexistent")
        result = search_assessment_tests(mock_http, request)
        
        assert len(result.items) == 0
        assert result.total == 0
        assert result.pages == 0

    def test_search_assessment_tests_validates_test_fields(self) -> None:
        """Test that assessment test fields are correctly parsed."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        result = search_assessment_tests(mock_http)
        
        test = result.items[0]
        assert test.identifier == "test-001"
        assert test.title == "Test Assessment"
        assert test.qti_version == "3.0"
        assert test.raw_xml is not None
        
        # Verify test parts
        assert test.qti_test_part is not None
        assert len(test.qti_test_part) == 1
        assert test.qti_test_part[0].identifier == "part-1"
        
        # Verify outcome declarations
        assert test.qti_outcome_declaration is not None
        assert len(test.qti_outcome_declaration) == 1

    def test_search_assessment_tests_all_parameters(self) -> None:
        """Test search with all parameters set."""
        mock_data = create_mock_response(
            total=100,
            page=5,
            pages=10,
            limit=10,
            sort="title",
            order="asc"
        )
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchAssessmentTestsRequest(
            query="algebra",
            page=5,
            limit=10,
            sort=TimebackQTIAssessmentTestSortField.TITLE,
            order=TimebackSortOrder.ASC,
            navigation_mode=TimebackQTINavigationMode.LINEAR,
            submission_mode=TimebackQTISubmissionMode.INDIVIDUAL,
            filter="type='practice'"
        )
        result = search_assessment_tests(mock_http, request)
        
        assert result.page == 5
        assert result.pages == 10
        assert result.total == 100
        assert result.sort == "title"
        assert result.order == TimebackSortOrder.ASC
        
        # Verify all params were sent
        assert mock_http.last_params["query"] == "algebra"
        assert mock_http.last_params["page"] == "5"
        assert mock_http.last_params["limit"] == "10"
        assert mock_http.last_params["sort"] == "title"
        assert mock_http.last_params["order"] == "asc"
        assert mock_http.last_params["navigationMode"] == "linear"
        assert mock_http.last_params["submissionMode"] == "individual"
        assert mock_http.last_params["filter"] == "type='practice'"

