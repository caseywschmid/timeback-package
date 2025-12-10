"""Unit tests for search_assessment_items endpoint.

Tests the search_assessment_items function that retrieves a paginated list of QTI assessment items.
"""

from typing import Any, Dict, List
import pytest

from timeback.services.qti.endpoints.search_assessment_items import search_assessment_items
from timeback.models.request import TimebackSearchAssessmentItemsRequest
from timeback.models.response import TimebackSearchAssessmentItemsResponse
from timeback.enums import TimebackQTIAssessmentItemSortField, TimebackSortOrder


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


def create_mock_assessment_item_data(
    identifier: str = "item-001",
    title: str = "Test Assessment Item",
    item_type: str = "choice"
) -> Dict[str, Any]:
    """Create mock assessment item data for testing."""
    return {
        "identifier": identifier,
        "title": title,
        "type": item_type,
        "qtiVersion": "3.0",
        "timeDependent": False,
        "adaptive": False,
        "responseDeclarations": [
            {
                "identifier": "RESPONSE",
                "cardinality": "single",
                "baseType": "identifier",
                "correctResponse": {"value": ["A"]}
            }
        ],
        "outcomeDeclarations": [
            {
                "identifier": "SCORE",
                "cardinality": "single",
                "baseType": "float"
            }
        ],
        "responseProcessing": {
            "templateType": "match_correct",
            "responseDeclarationIdentifier": "RESPONSE",
            "outcomeIdentifier": "SCORE",
            "correctResponseIdentifier": "correct",
            "incorrectResponseIdentifier": "incorrect"
        },
        "metadata": {
            "subject": "Math",
            "grade": "7",
            "difficulty": "medium"
        },
        "rawXml": '<?xml version="1.0"?><qti-assessment-item></qti-assessment-item>'
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
        items = [create_mock_assessment_item_data()]
    
    return {
        "items": items,
        "total": total,
        "page": page,
        "pages": pages,
        "limit": limit,
        "sort": sort,
        "order": order
    }


class TestSearchAssessmentItems:
    """Tests for search_assessment_items endpoint."""

    def test_search_assessment_items_success_default_params(self) -> None:
        """Test successful search with default parameters."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        result = search_assessment_items(mock_http)
        
        assert isinstance(result, TimebackSearchAssessmentItemsResponse)
        assert len(result.items) == 1
        assert result.total == 1
        assert result.page == 1
        assert result.pages == 1
        assert result.limit == 10
        assert result.order == TimebackSortOrder.DESC
        
        # Verify request was made with default params
        assert mock_http.last_path == "/assessment-items"
        assert mock_http.last_params["page"] == "1"
        assert mock_http.last_params["limit"] == "10"
        assert mock_http.last_params["order"] == "desc"

    def test_search_assessment_items_with_query(self) -> None:
        """Test search with a query parameter."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchAssessmentItemsRequest(query="math multiplication")
        result = search_assessment_items(mock_http, request)
        
        assert isinstance(result, TimebackSearchAssessmentItemsResponse)
        assert mock_http.last_params["query"] == "math multiplication"

    def test_search_assessment_items_with_filter(self) -> None:
        """Test search with a filter parameter."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchAssessmentItemsRequest(filter="type='choice'")
        result = search_assessment_items(mock_http, request)
        
        assert mock_http.last_params["filter"] == "type='choice'"

    def test_search_assessment_items_with_pagination(self) -> None:
        """Test search with custom pagination parameters."""
        mock_data = create_mock_response(
            total=50,
            page=3,
            pages=5,
            limit=10
        )
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchAssessmentItemsRequest(page=3, limit=10)
        result = search_assessment_items(mock_http, request)
        
        assert result.page == 3
        assert result.pages == 5
        assert result.total == 50
        assert mock_http.last_params["page"] == "3"
        assert mock_http.last_params["limit"] == "10"

    def test_search_assessment_items_with_sorting(self) -> None:
        """Test search with sorting parameters."""
        mock_data = create_mock_response(sort="type", order="asc")
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchAssessmentItemsRequest(
            sort=TimebackQTIAssessmentItemSortField.TYPE,
            order=TimebackSortOrder.ASC
        )
        result = search_assessment_items(mock_http, request)
        
        assert result.sort == "type"
        assert result.order == TimebackSortOrder.ASC
        assert mock_http.last_params["sort"] == "type"
        assert mock_http.last_params["order"] == "asc"

    def test_search_assessment_items_multiple_items(self) -> None:
        """Test search returning multiple items."""
        items = [
            create_mock_assessment_item_data("item-001", "Math Question", "choice"),
            create_mock_assessment_item_data("item-002", "Science Question", "text-entry"),
            create_mock_assessment_item_data("item-003", "English Question", "extended-text"),
        ]
        mock_data = create_mock_response(items=items, total=3)
        mock_http = MockHttpClient(mock_data)
        
        result = search_assessment_items(mock_http)
        
        assert len(result.items) == 3
        assert result.total == 3
        assert result.items[0].identifier == "item-001"
        assert result.items[0].type == "choice"
        assert result.items[1].type == "text-entry"
        assert result.items[2].type == "extended-text"

    def test_search_assessment_items_empty_results(self) -> None:
        """Test search returning no results."""
        mock_data = create_mock_response(items=[], total=0, pages=0)
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchAssessmentItemsRequest(query="nonexistent")
        result = search_assessment_items(mock_http, request)
        
        assert len(result.items) == 0
        assert result.total == 0
        assert result.pages == 0

    def test_search_assessment_items_validates_item_fields(self) -> None:
        """Test that assessment item fields are correctly parsed."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        result = search_assessment_items(mock_http)
        
        item = result.items[0]
        assert item.identifier == "item-001"
        assert item.title == "Test Assessment Item"
        assert item.type == "choice"
        assert item.qtiVersion == "3.0"
        assert item.timeDependent == False
        assert item.adaptive == False
        assert item.rawXml is not None
        
        # Verify response declarations
        assert item.responseDeclarations is not None
        assert len(item.responseDeclarations) == 1
        assert item.responseDeclarations[0].identifier == "RESPONSE"
        
        # Verify outcome declarations
        assert item.outcomeDeclarations is not None
        assert len(item.outcomeDeclarations) == 1
        
        # Verify metadata
        assert item.metadata is not None
        assert item.metadata["subject"] == "Math"
        assert item.metadata["difficulty"] == "medium"

    def test_search_assessment_items_all_parameters(self) -> None:
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
        
        request = TimebackSearchAssessmentItemsRequest(
            query="algebra",
            page=5,
            limit=10,
            sort=TimebackQTIAssessmentItemSortField.TITLE,
            order=TimebackSortOrder.ASC,
            filter="type='choice' AND metadata.difficulty='hard'"
        )
        result = search_assessment_items(mock_http, request)
        
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
        assert mock_http.last_params["filter"] == "type='choice' AND metadata.difficulty='hard'"

