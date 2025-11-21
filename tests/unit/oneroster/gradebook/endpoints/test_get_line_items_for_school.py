from timeback.services.oneroster.gradebook.endpoints.get_line_items_for_school import (
    get_line_items_for_school,
)
from timeback.models.request import (
    TimebackGetLineItemsForSchoolRequest,
    TimebackQueryParams,
)
from timeback.models.response import TimebackGetAllLineItemsResponse
from timeback.enums import TimebackStatus


class MockHttp:
    def get(self, path, params=None):
        assert path.startswith("/ims/oneroster/gradebook/v1p2/schools/")
        assert path.endswith("/lineItems")
        # Simulate 200 response body
        return {
            "lineItems": [
                {
                    "sourcedId": "line-item-1",
                    "status": "active",
                    "dateLastModified": "2024-01-01T00:00:00Z",
                    "metadata": {},
                    "title": "Math Quiz 1",
                    "description": "First quiz of the semester",
                    "assignDate": "2024-01-15T00:00:00Z",
                    "dueDate": "2024-01-20T23:59:59Z",
                    "class": {"sourcedId": "class-1"},
                    "school": {"sourcedId": "school-123"},
                    "category": {"sourcedId": "category-1"},
                    "scoreScale": {"sourcedId": "scale-1"},
                    "resultValueMin": 0.0,
                    "resultValueMax": 100.0,
                }
            ],
            "totalCount": 1,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }


def test_get_line_items_for_school_success():
    """Test successful retrieval of line items for a school."""
    request = TimebackGetLineItemsForSchoolRequest(school_sourced_id="school-123")
    resp = get_line_items_for_school(MockHttp(), request)
    
    assert isinstance(resp, TimebackGetAllLineItemsResponse)
    assert len(resp.line_items) == 1
    assert resp.line_items[0].sourcedId == "line-item-1"
    assert resp.line_items[0].status == TimebackStatus.ACTIVE
    assert resp.line_items[0].title == "Math Quiz 1"
    assert resp.line_items[0].description == "First quiz of the semester"
    assert resp.line_items[0].class_.sourcedId == "class-1"
    assert resp.line_items[0].school.sourcedId == "school-123"
    assert resp.line_items[0].category.sourcedId == "category-1"
    assert resp.total_count == 1
    assert resp.limit == 100


def test_get_line_items_for_school_with_query_params():
    """Test retrieval with query parameters."""
    query_params = TimebackQueryParams(limit=50, offset=10, fields="sourcedId,title")
    request = TimebackGetLineItemsForSchoolRequest(
        school_sourced_id="school-123",
        query_params=query_params
    )
    resp = get_line_items_for_school(MockHttp(), request)
    
    assert isinstance(resp, TimebackGetAllLineItemsResponse)
    assert len(resp.line_items) == 1

