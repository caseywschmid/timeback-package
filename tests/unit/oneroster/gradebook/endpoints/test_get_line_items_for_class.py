from timeback.services.oneroster.gradebook.endpoints.get_line_items_for_class import (
    get_line_items_for_class,
)
from timeback.models.request import (
    TimebackGetLineItemsForClassRequest,
    TimebackQueryParams,
)
from timeback.models.response import TimebackGetAllLineItemsResponse
from timeback.enums import TimebackStatus


class MockHttp:
    def get(self, path, params=None):
        assert path.startswith("/ims/oneroster/gradebook/v1p2/classes/")
        assert path.endswith("/lineItems")
        # Simulate 200 response body
        return {
            "lineItems": [
                {
                    "sourcedId": "line-item-1",
                    "status": "active",
                    "dateLastModified": "2024-01-01T00:00:00Z",
                    "metadata": {},
                    "title": "Homework Assignment 1",
                    "description": "First homework assignment",
                    "assignDate": "2024-01-01T00:00:00Z",
                    "dueDate": "2024-01-15T00:00:00Z",
                    "class": {"sourcedId": "class-123"},
                    "school": {"sourcedId": "school-456"},
                    "category": {"sourcedId": "category-789"},
                    "gradingPeriod": {"sourcedId": "grading-period-1"},
                    "academicSession": {"sourcedId": "session-1"},
                    "scoreScale": {"sourcedId": "scale-1"},
                    "resultValueMin": 0.0,
                    "resultValueMax": 100.0,
                },
                {
                    "sourcedId": "line-item-2",
                    "status": "active",
                    "dateLastModified": "2024-01-02T00:00:00Z",
                    "title": "Midterm Exam",
                    "assignDate": "2024-02-01T00:00:00Z",
                    "dueDate": "2024-02-01T00:00:00Z",
                    "class": {"sourcedId": "class-123"},
                    "school": {"sourcedId": "school-456"},
                    "category": {"sourcedId": "category-789"},
                }
            ],
            "totalCount": 2,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }


def test_get_line_items_for_class_success():
    """Test successful retrieval of line items for a class."""
    request = TimebackGetLineItemsForClassRequest(
        class_sourced_id="class-123"
    )
    resp = get_line_items_for_class(MockHttp(), request)
    
    assert isinstance(resp, TimebackGetAllLineItemsResponse)
    assert len(resp.line_items) == 2
    assert resp.line_items[0].sourcedId == "line-item-1"
    assert resp.line_items[0].status == TimebackStatus.ACTIVE
    assert resp.line_items[0].title == "Homework Assignment 1"
    assert resp.line_items[0].class_.sourcedId == "class-123"
    assert resp.line_items[0].school.sourcedId == "school-456"
    assert resp.line_items[0].category.sourcedId == "category-789"
    assert resp.line_items[1].sourcedId == "line-item-2"
    assert resp.line_items[1].title == "Midterm Exam"
    assert resp.total_count == 2
    assert resp.limit == 100


def test_get_line_items_for_class_with_query_params():
    """Test retrieval with query parameters."""
    query_params = TimebackQueryParams(limit=50, offset=10, fields="sourcedId,title")
    request = TimebackGetLineItemsForClassRequest(
        class_sourced_id="class-123",
        query_params=query_params
    )
    resp = get_line_items_for_class(MockHttp(), request)
    
    assert isinstance(resp, TimebackGetAllLineItemsResponse)
    assert len(resp.line_items) == 2

