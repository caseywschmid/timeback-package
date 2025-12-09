from timeback.services.oneroster.gradebook.endpoints.put_line_item import (
    put_line_item,
)
from timeback.models.request import (
    TimebackPutLineItemRequest,
    TimebackPutLineItemBody,
)
from timeback.models.response import TimebackPutLineItemResponse
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus


class MockHttp:
    def put(self, path, json=None):
        assert path.startswith("/ims/oneroster/gradebook/v1p2/lineItems/")
        assert json is not None
        assert "lineItem" in json
        # Extract sourcedId from path
        sourced_id = path.split("/")[-1]
        # Simulate 201 response body
        return {
            "lineItem": {
                "sourcedId": sourced_id,
                "status": "active",
                "dateLastModified": "2024-01-01T00:00:00Z",
                "metadata": json.get("lineItem", {}).get("metadata", {}),
                "title": json["lineItem"]["title"],
                "description": json["lineItem"].get("description"),
                "assignDate": json["lineItem"]["assignDate"],
                "dueDate": json["lineItem"]["dueDate"],
                "class": {"sourcedId": "class-1"},
                "school": {"sourcedId": "school-1"},
                "category": {"sourcedId": "category-1"},
                "scoreScale": json["lineItem"].get("scoreScale"),
                "resultValueMin": json["lineItem"].get("resultValueMin"),
                "resultValueMax": json["lineItem"].get("resultValueMax"),
            }
        }


def test_put_line_item_success():
    """Test successful line item update/create."""
    body = TimebackPutLineItemBody(
        sourcedId="line-item-123",
        title="Math Quiz 1 - Updated",
        assignDate="2024-01-15T00:00:00Z",
        dueDate="2024-01-20T23:59:59Z",
        class_=TimebackSourcedIdReference(sourcedId="class-1"),
        school=TimebackSourcedIdReference(sourcedId="school-1"),
        category=TimebackSourcedIdReference(sourcedId="category-1"),
        description="Updated description",
        resultValueMin=0.0,
        resultValueMax=100.0,
    )
    request = TimebackPutLineItemRequest(
        sourced_id="line-item-123", lineItem=body
    )
    resp = put_line_item(MockHttp(), request)
    
    assert isinstance(resp, TimebackPutLineItemResponse)
    assert resp.line_item.sourcedId == "line-item-123"
    assert resp.line_item.title == "Math Quiz 1 - Updated"
    assert resp.line_item.description == "Updated description"


def test_put_line_item_with_all_fields():
    """Test line item update/create with all optional fields."""
    body = TimebackPutLineItemBody(
        sourcedId="line-item-456",
        title="Math Quiz 2",
        assignDate="2024-01-22T00:00:00Z",
        dueDate="2024-01-27T23:59:59Z",
        class_=TimebackSourcedIdReference(sourcedId="class-1"),
        school=TimebackSourcedIdReference(sourcedId="school-1"),
        category=TimebackSourcedIdReference(sourcedId="category-1"),
        status=TimebackStatus.ACTIVE,
        description="Second quiz",
        scoreScale=TimebackSourcedIdReference(sourcedId="scale-1"),
        resultValueMin=0.0,
        resultValueMax=100.0,
        metadata={"key": "value"},
    )
    request = TimebackPutLineItemRequest(
        sourced_id="line-item-456", lineItem=body
    )
    resp = put_line_item(MockHttp(), request)
    
    assert isinstance(resp, TimebackPutLineItemResponse)
    assert resp.line_item.sourcedId == "line-item-456"  # Mock returns sourcedId from path

