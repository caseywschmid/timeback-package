from timeback.services.oneroster.gradebook.endpoints.post_line_items_for_class import (
    post_line_items_for_class,
)
from timeback.models.request import (
    TimebackPostLineItemsForClassRequest,
    TimebackCreateLineItemBody,
)
from timeback.models.response import TimebackPostLineItemsForClassResponse
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus


class MockHttp:
    def post(self, path, json=None):
        assert path.startswith("/ims/oneroster/gradebook/v1p2/classes/")
        assert path.endswith("/lineItems")
        assert json is not None
        assert "lineItems" in json
        assert isinstance(json["lineItems"], list)
        # Simulate 201 response body with sourcedIdPairs
        # Use the first line item's sourcedId if available
        first_line_item_sourced_id = json["lineItems"][0].get("sourcedId", "temp-id") if json["lineItems"] else "temp-id"
        return {
            "sourcedIdPairs": {
                "suppliedSourcedId": first_line_item_sourced_id,
                "allocatedSourcedId": "allocated-line-item-123",
            }
        }


def test_post_line_items_for_class_success():
    """Test successful line item creation for a class."""
    class_sourced_id = "class-123"
    line_item1 = TimebackCreateLineItemBody(
        sourcedId="line-item-1",
        title="Math Quiz 1",
        assignDate="2024-01-15T00:00:00Z",
        dueDate="2024-01-20T23:59:59Z",
        class_=TimebackSourcedIdReference(sourcedId=class_sourced_id),
        school=TimebackSourcedIdReference(sourcedId="school-1"),
        category=TimebackSourcedIdReference(sourcedId="category-1"),
    )
    request = TimebackPostLineItemsForClassRequest(
        class_sourced_id=class_sourced_id,
        lineItems=[line_item1]
    )
    resp = post_line_items_for_class(MockHttp(), request)
    
    assert isinstance(resp, TimebackPostLineItemsForClassResponse)
    assert resp.sourcedIdPairs.allocatedSourcedId == "allocated-line-item-123"
    assert resp.sourcedIdPairs.suppliedSourcedId == "line-item-1"


def test_post_line_items_for_class_multiple_items():
    """Test creating multiple line items for a class."""
    class_sourced_id = "class-456"
    line_item1 = TimebackCreateLineItemBody(
        sourcedId="line-item-1",
        title="Math Quiz 1",
        assignDate="2024-01-15T00:00:00Z",
        dueDate="2024-01-20T23:59:59Z",
        class_=TimebackSourcedIdReference(sourcedId=class_sourced_id),
        school=TimebackSourcedIdReference(sourcedId="school-1"),
        category=TimebackSourcedIdReference(sourcedId="category-1"),
    )
    line_item2 = TimebackCreateLineItemBody(
        sourcedId="line-item-2",
        title="Math Quiz 2",
        assignDate="2024-01-22T00:00:00Z",
        dueDate="2024-01-27T23:59:59Z",
        class_=TimebackSourcedIdReference(sourcedId=class_sourced_id),
        school=TimebackSourcedIdReference(sourcedId="school-1"),
        category=TimebackSourcedIdReference(sourcedId="category-1"),
    )
    request = TimebackPostLineItemsForClassRequest(
        class_sourced_id=class_sourced_id,
        lineItems=[line_item1, line_item2]
    )
    resp = post_line_items_for_class(MockHttp(), request)
    
    assert isinstance(resp, TimebackPostLineItemsForClassResponse)
    assert resp.sourcedIdPairs.allocatedSourcedId == "allocated-line-item-123"
    assert resp.sourcedIdPairs.suppliedSourcedId == "line-item-1"  # First line item's sourcedId


def test_post_line_items_for_class_with_all_fields():
    """Test line item creation with all optional fields."""
    class_sourced_id = "class-789"
    line_item = TimebackCreateLineItemBody(
        sourcedId="line-item-full",
        title="Math Quiz Full",
        assignDate="2024-01-15T00:00:00Z",
        dueDate="2024-01-20T23:59:59Z",
        class_=TimebackSourcedIdReference(sourcedId=class_sourced_id),
        school=TimebackSourcedIdReference(sourcedId="school-1"),
        category=TimebackSourcedIdReference(sourcedId="category-1"),
        status=TimebackStatus.ACTIVE,
        description="Full quiz description",
        scoreScale=TimebackSourcedIdReference(sourcedId="scale-1"),
        resultValueMin=0.0,
        resultValueMax=100.0,
    )
    request = TimebackPostLineItemsForClassRequest(
        class_sourced_id=class_sourced_id,
        lineItems=[line_item]
    )
    resp = post_line_items_for_class(MockHttp(), request)
    
    assert isinstance(resp, TimebackPostLineItemsForClassResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "line-item-full"

