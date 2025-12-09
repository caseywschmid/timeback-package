from timeback.services.oneroster.gradebook.endpoints.create_line_item import create_line_item
from timeback.models.request import (
    TimebackCreateLineItemRequest,
    TimebackCreateLineItemBody,
)
from timeback.models.response import TimebackCreateLineItemResponse
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus


class MockHttp:
    def post(self, path, json=None):
        assert path == "/ims/oneroster/gradebook/v1p2/lineItems"
        # Simulate 201 response body with sourcedIdPairs
        return {
            "sourcedIdPairs": {
                "suppliedSourcedId": json["lineItem"].get("sourcedId", "temp-id"),
                "allocatedSourcedId": "allocated-line-item-123",
            }
        }


def test_create_line_item_success():
    """Test successful line item creation."""
    body = TimebackCreateLineItemBody(
        sourcedId="line-item-created",
        title="Math Quiz 1",
        assignDate="2024-01-15T00:00:00Z",
        dueDate="2024-01-20T23:59:59Z",
        class_=TimebackSourcedIdReference(sourcedId="class-1"),
        school=TimebackSourcedIdReference(sourcedId="school-1"),
        category=TimebackSourcedIdReference(sourcedId="category-1"),
        description="First quiz of the semester",
        resultValueMin=0.0,
        resultValueMax=100.0,
    )
    req = TimebackCreateLineItemRequest(lineItem=body)
    resp = create_line_item(MockHttp(), req)
    assert isinstance(resp, TimebackCreateLineItemResponse)
    assert resp.sourcedIdPairs.allocatedSourcedId == "allocated-line-item-123"
    assert resp.sourcedIdPairs.suppliedSourcedId == "line-item-created"


def test_create_line_item_with_all_fields():
    """Test line item creation with all optional fields."""
    body = TimebackCreateLineItemBody(
        sourcedId="line-item-full",
        title="Math Quiz 1",
        assignDate="2024-01-15T00:00:00Z",
        dueDate="2024-01-20T23:59:59Z",
        class_=TimebackSourcedIdReference(sourcedId="class-1"),
        school=TimebackSourcedIdReference(sourcedId="school-1"),
        category=TimebackSourcedIdReference(sourcedId="category-1"),
        status=TimebackStatus.ACTIVE,
        description="First quiz of the semester",
        scoreScale=TimebackSourcedIdReference(sourcedId="scale-1"),
        resultValueMin=0.0,
        resultValueMax=100.0,
        metadata={"key": "value"},
    )
    req = TimebackCreateLineItemRequest(lineItem=body)
    resp = create_line_item(MockHttp(), req)
    assert isinstance(resp, TimebackCreateLineItemResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "line-item-full"

