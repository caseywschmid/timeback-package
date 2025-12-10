"""Unit tests for search_stimuli endpoint.

Tests the search_stimuli function that retrieves a paginated list of QTI stimuli.
"""

from typing import Any, Dict, List
from datetime import datetime
import pytest

from timeback.services.qti.endpoints.search_stimuli import search_stimuli
from timeback.models.request import TimebackSearchStimuliRequest
from timeback.models.response import TimebackSearchStimuliResponse
from timeback.models.timeback_qti_stimulus import TimebackQTIStimulus
from timeback.enums import TimebackQTISortField, TimebackSortOrder


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
        "rawXml": '<?xml version="1.0"?><qti-assessment-stimulus></qti-assessment-stimulus>',
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
        items = [create_mock_stimulus_data()]
    
    return {
        "items": items,
        "total": total,
        "page": page,
        "pages": pages,
        "limit": limit,
        "sort": sort,
        "order": order
    }


class TestSearchStimuli:
    """Tests for search_stimuli endpoint."""

    def test_search_stimuli_success_default_params(self) -> None:
        """Test successful search with default parameters."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        result = search_stimuli(mock_http)
        
        assert isinstance(result, TimebackSearchStimuliResponse)
        assert len(result.items) == 1
        assert result.total == 1
        assert result.page == 1
        assert result.pages == 1
        assert result.limit == 10
        assert result.order == TimebackSortOrder.DESC
        
        # Verify request was made with default params
        assert mock_http.last_path == "/stimuli"
        assert mock_http.last_params["page"] == "1"
        assert mock_http.last_params["limit"] == "10"
        assert mock_http.last_params["order"] == "desc"

    def test_search_stimuli_with_query(self) -> None:
        """Test search with a query parameter."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchStimuliRequest(query="forest ecosystem")
        result = search_stimuli(mock_http, request)
        
        assert isinstance(result, TimebackSearchStimuliResponse)
        assert mock_http.last_params["query"] == "forest ecosystem"

    def test_search_stimuli_with_pagination(self) -> None:
        """Test search with custom pagination parameters."""
        mock_data = create_mock_response(
            total=50,
            page=3,
            pages=5,
            limit=10
        )
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchStimuliRequest(page=3, limit=10)
        result = search_stimuli(mock_http, request)
        
        assert result.page == 3
        assert result.pages == 5
        assert result.total == 50
        assert mock_http.last_params["page"] == "3"
        assert mock_http.last_params["limit"] == "10"

    def test_search_stimuli_with_sorting(self) -> None:
        """Test search with sorting parameters."""
        mock_data = create_mock_response(sort="title", order="asc")
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchStimuliRequest(
            sort=TimebackQTISortField.TITLE,
            order=TimebackSortOrder.ASC
        )
        result = search_stimuli(mock_http, request)
        
        assert result.sort == "title"
        assert result.order == TimebackSortOrder.ASC
        assert mock_http.last_params["sort"] == "title"
        assert mock_http.last_params["order"] == "asc"

    def test_search_stimuli_multiple_items(self) -> None:
        """Test search returning multiple items."""
        items = [
            create_mock_stimulus_data("stim-001", "First Stimulus"),
            create_mock_stimulus_data("stim-002", "Second Stimulus"),
            create_mock_stimulus_data("stim-003", "Third Stimulus"),
        ]
        mock_data = create_mock_response(items=items, total=3)
        mock_http = MockHttpClient(mock_data)
        
        result = search_stimuli(mock_http)
        
        assert len(result.items) == 3
        assert result.total == 3
        assert result.items[0].identifier == "stim-001"
        assert result.items[1].identifier == "stim-002"
        assert result.items[2].identifier == "stim-003"

    def test_search_stimuli_empty_results(self) -> None:
        """Test search returning no results."""
        mock_data = create_mock_response(items=[], total=0, pages=0)
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchStimuliRequest(query="nonexistent")
        result = search_stimuli(mock_http, request)
        
        assert len(result.items) == 0
        assert result.total == 0
        assert result.pages == 0

    def test_search_stimuli_validates_stimulus_fields(self) -> None:
        """Test that stimulus fields are correctly parsed."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        result = search_stimuli(mock_http)
        
        stimulus = result.items[0]
        assert isinstance(stimulus, TimebackQTIStimulus)
        assert stimulus.identifier == "stimulus-001"
        assert stimulus.title == "Test Stimulus"
        assert stimulus.language == "en"
        assert stimulus.label == "Test Label"
        assert stimulus.tool_name == "QTI Editor"
        assert stimulus.tool_version == "1.0.0"
        assert stimulus.raw_xml is not None
        assert stimulus.content is not None
        assert stimulus.created_at is not None
        assert stimulus.updated_at is not None
        
        # Verify catalog info
        assert len(stimulus.catalog_info) == 1
        assert stimulus.catalog_info[0].id == "catalog-1"
        assert stimulus.catalog_info[0].support == "spoken"
        
        # Verify stylesheet
        assert stimulus.stylesheet is not None
        assert stimulus.stylesheet.href == "styles.css"
        assert stimulus.stylesheet.type == "text/css"
        
        # Verify metadata
        assert stimulus.metadata is not None
        assert stimulus.metadata["subject"] == "Science"

    def test_search_stimuli_all_parameters(self) -> None:
        """Test search with all parameters set."""
        mock_data = create_mock_response(
            total=100,
            page=5,
            pages=10,
            limit=10,
            sort="updatedAt",
            order="desc"
        )
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackSearchStimuliRequest(
            query="ecosystem",
            page=5,
            limit=10,
            sort=TimebackQTISortField.UPDATED_AT,
            order=TimebackSortOrder.DESC
        )
        result = search_stimuli(mock_http, request)
        
        assert result.page == 5
        assert result.pages == 10
        assert result.total == 100
        assert result.sort == "updatedAt"
        assert result.order == TimebackSortOrder.DESC
        
        # Verify all params were sent
        assert mock_http.last_params["query"] == "ecosystem"
        assert mock_http.last_params["page"] == "5"
        assert mock_http.last_params["limit"] == "10"
        assert mock_http.last_params["sort"] == "updatedAt"
        assert mock_http.last_params["order"] == "desc"

    def test_search_stimuli_minimal_stimulus_data(self) -> None:
        """Test with minimal required stimulus fields."""
        minimal_stimulus = {
            "identifier": "min-stimulus",
            "title": "Minimal Stimulus",
            "catalogInfo": [],
            "rawXml": "<qti-assessment-stimulus></qti-assessment-stimulus>",
            "createdAt": "2024-01-15T10:30:00.000Z",
            "updatedAt": "2024-01-15T10:30:00.000Z"
        }
        mock_data = create_mock_response(items=[minimal_stimulus])
        mock_http = MockHttpClient(mock_data)
        
        result = search_stimuli(mock_http)
        
        stimulus = result.items[0]
        assert stimulus.identifier == "min-stimulus"
        assert stimulus.title == "Minimal Stimulus"
        assert len(stimulus.catalog_info) == 0
        assert stimulus.stylesheet is None
        assert stimulus.metadata is None

