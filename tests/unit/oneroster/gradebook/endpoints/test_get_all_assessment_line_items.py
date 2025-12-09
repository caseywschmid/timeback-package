from timeback.services.oneroster.gradebook.endpoints.get_all_assessment_line_items import (
    get_all_assessment_line_items,
)
from timeback.models.request import (
    TimebackGetAllAssessmentLineItemsRequest,
    TimebackQueryParams,
)
from timeback.models.response import TimebackGetAllAssessmentLineItemsResponse


class MockHttp:
    def __init__(self):
        self.last_path = None
        self.last_params = None

    def get(self, path, params=None):
        self.last_path = path
        self.last_params = params
        return {
            "assessmentLineItems": [
                {
                    "sourcedId": "ali-001",
                    "status": "active",
                    "title": "Quiz 1",
                    "class": {"sourcedId": "class-001"},
                    "school": {"sourcedId": "school-001"},
                    "category": {"sourcedId": "cat-001"},
                    "assignDate": "2024-01-01",
                    "dueDate": "2024-01-15",
                },
                {
                    "sourcedId": "ali-002",
                    "status": "active",
                    "title": "Homework 1",
                    "class": {"sourcedId": "class-001"},
                    "school": {"sourcedId": "school-001"},
                    "category": {"sourcedId": "cat-002"},
                    "assignDate": "2024-01-02",
                    "dueDate": "2024-01-16",
                },
            ],
            "totalCount": 2,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }


def test_get_all_assessment_line_items_success():
    """Test successful assessment line items retrieval."""
    mock_http = MockHttp()
    request = TimebackGetAllAssessmentLineItemsRequest()
    resp = get_all_assessment_line_items(mock_http, request)

    assert isinstance(resp, TimebackGetAllAssessmentLineItemsResponse)
    assert len(resp.assessmentLineItems) == 2
    assert resp.assessmentLineItems[0].sourcedId == "ali-001"
    assert resp.assessmentLineItems[0].title == "Quiz 1"
    assert resp.total_count == 2
    assert "/ims/oneroster/gradebook/v1p2/assessmentLineItems" in mock_http.last_path


def test_get_all_assessment_line_items_with_query_params():
    """Test assessment line items retrieval with query parameters."""
    mock_http = MockHttp()
    query_params = TimebackQueryParams(
        limit=50,
        offset=10,
        sort="title",
        order_by="asc",
    )
    request = TimebackGetAllAssessmentLineItemsRequest(query_params=query_params)
    resp = get_all_assessment_line_items(mock_http, request)

    assert isinstance(resp, TimebackGetAllAssessmentLineItemsResponse)
    assert mock_http.last_params == {
        "limit": 50,
        "offset": 10,
        "sort": "title",
        "orderBy": "asc",
    }


def test_get_all_assessment_line_items_empty_list():
    """Test assessment line items retrieval with empty list."""
    class MockHttpEmpty:
        def get(self, path, params=None):
            return {
                "assessmentLineItems": [],
                "totalCount": 0,
                "pageCount": 0,
                "pageNumber": 0,
                "offset": 0,
                "limit": 100,
            }

    request = TimebackGetAllAssessmentLineItemsRequest()
    resp = get_all_assessment_line_items(MockHttpEmpty(), request)

    assert isinstance(resp, TimebackGetAllAssessmentLineItemsResponse)
    assert len(resp.assessmentLineItems) == 0
    assert resp.total_count == 0

