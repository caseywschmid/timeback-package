from timeback.services.oneroster.gradebook.endpoints.get_line_item import (
    get_line_item,
)
from timeback.models.request import (
    TimebackGetLineItemRequest,
    TimebackQueryParams,
)
from timeback.models.response import TimebackGetLineItemResponse
from timeback.enums import TimebackStatus


class MockHttp:
    def get(self, path, params=None):
        assert path == "/ims/oneroster/gradebook/v1p2/lineItems/line-item-123"
        # Simulate 200 response body
        return {
            "lineItem": {
                "sourcedId": "line-item-123",
                "status": "active",
                "dateLastModified": "2024-01-01T00:00:00Z",
                "metadata": {},
                "title": "Math Quiz 1",
                "description": "First quiz of the semester",
                "assignDate": "2024-01-15T00:00:00Z",
                "dueDate": "2024-01-20T23:59:59Z",
                "class": {"sourcedId": "class-1"},
                "school": {"sourcedId": "school-1"},
                "category": {"sourcedId": "category-1"},
                "scoreScale": {"sourcedId": "scale-1"},
                "resultValueMin": 0.0,
                "resultValueMax": 100.0,
            }
        }


def test_get_line_item_success():
    request = TimebackGetLineItemRequest(sourced_id="line-item-123")
    resp = get_line_item(MockHttp(), request)
    assert isinstance(resp, TimebackGetLineItemResponse)
    assert resp.line_item.sourcedId == "line-item-123"
    assert resp.line_item.title == "Math Quiz 1"
    assert resp.line_item.description == "First quiz of the semester"
    assert resp.line_item.class_.sourcedId == "class-1"
    assert resp.line_item.school.sourcedId == "school-1"
    assert resp.line_item.category.sourcedId == "category-1"


def test_get_line_item_with_fields():
    query_params = TimebackQueryParams(fields="sourcedId,title,assignDate,dueDate")
    request = TimebackGetLineItemRequest(
        sourced_id="line-item-123", query_params=query_params
    )
    resp = get_line_item(MockHttp(), request)
    assert isinstance(resp, TimebackGetLineItemResponse)
    assert resp.line_item.sourcedId == "line-item-123"

