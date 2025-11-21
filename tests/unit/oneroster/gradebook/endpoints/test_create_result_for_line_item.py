from timeback.services.oneroster.gradebook.endpoints.create_result_for_line_item import (
    create_result_for_line_item,
)
from timeback.models.request import (
    TimebackCreateResultForLineItemRequest,
    TimebackCreateResultBody,
)
from timeback.models.response import TimebackCreateResultForLineItemResponse
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus, TimebackScoreStatus


class MockHttp:
    def post(self, path, json=None):
        assert path.startswith("/ims/oneroster/gradebook/v1p2/lineItems/")
        assert path.endswith("/results")
        assert json is not None
        assert "results" in json
        assert isinstance(json["results"], list)
        # Simulate 201 response body with sourcedIdPairs
        # Use the first result's sourcedId if available
        first_result_sourced_id = json["results"][0].get("sourcedId", "temp-id") if json["results"] else "temp-id"
        return {
            "sourcedIdPairs": {
                "suppliedSourcedId": first_result_sourced_id,
                "allocatedSourcedId": "allocated-result-123",
            }
        }


def test_create_result_for_line_item_success():
    """Test successful result creation for a line item."""
    line_item_sourced_id = "line-item-123"
    result1 = TimebackCreateResultBody(
        sourcedId="result-1",
        lineItem=TimebackSourcedIdReference(sourcedId=line_item_sourced_id),
        student=TimebackSourcedIdReference(sourcedId="student-1"),
        scoreStatus=TimebackScoreStatus.FULLY_GRADED,
        scoreDate="2024-01-15T10:00:00Z",
        score=95.5,
    )
    request = TimebackCreateResultForLineItemRequest(
        line_item_sourced_id=line_item_sourced_id,
        results=[result1]
    )
    resp = create_result_for_line_item(MockHttp(), request)
    
    assert isinstance(resp, TimebackCreateResultForLineItemResponse)
    assert resp.sourcedIdPairs.allocatedSourcedId == "allocated-result-123"
    assert resp.sourcedIdPairs.suppliedSourcedId == "result-1"


def test_create_result_for_line_item_multiple_results():
    """Test creating multiple results for a line item."""
    line_item_sourced_id = "line-item-456"
    result1 = TimebackCreateResultBody(
        sourcedId="result-1",
        lineItem=TimebackSourcedIdReference(sourcedId=line_item_sourced_id),
        student=TimebackSourcedIdReference(sourcedId="student-1"),
        scoreStatus=TimebackScoreStatus.FULLY_GRADED,
        scoreDate="2024-01-15T10:00:00Z",
        score=95.5,
    )
    result2 = TimebackCreateResultBody(
        sourcedId="result-2",
        lineItem=TimebackSourcedIdReference(sourcedId=line_item_sourced_id),
        student=TimebackSourcedIdReference(sourcedId="student-2"),
        scoreStatus=TimebackScoreStatus.SUBMITTED,
        scoreDate="2024-01-16T10:00:00Z",
        score=88.0,
    )
    request = TimebackCreateResultForLineItemRequest(
        line_item_sourced_id=line_item_sourced_id,
        results=[result1, result2]
    )
    resp = create_result_for_line_item(MockHttp(), request)
    
    assert isinstance(resp, TimebackCreateResultForLineItemResponse)
    assert resp.sourcedIdPairs.allocatedSourcedId == "allocated-result-123"
    assert resp.sourcedIdPairs.suppliedSourcedId == "result-1"  # First result's sourcedId


def test_create_result_for_line_item_with_all_fields():
    """Test result creation with all optional fields."""
    line_item_sourced_id = "line-item-789"
    result = TimebackCreateResultBody(
        sourcedId="result-full",
        lineItem=TimebackSourcedIdReference(sourcedId=line_item_sourced_id),
        student=TimebackSourcedIdReference(sourcedId="student-1"),
        scoreStatus=TimebackScoreStatus.FULLY_GRADED,
        scoreDate="2024-01-15T10:00:00Z",
        status=TimebackStatus.ACTIVE,
        score=95.5,
        textScore="A",
        comment="Excellent work",
        class_=TimebackSourcedIdReference(sourcedId="class-1"),
        scoreScale=TimebackSourcedIdReference(sourcedId="scale-1"),
    )
    request = TimebackCreateResultForLineItemRequest(
        line_item_sourced_id=line_item_sourced_id,
        results=[result]
    )
    resp = create_result_for_line_item(MockHttp(), request)
    
    assert isinstance(resp, TimebackCreateResultForLineItemResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "result-full"

