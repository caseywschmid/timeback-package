from timeback.services.oneroster.gradebook.endpoints.create_result import create_result
from timeback.models.request import (
    TimebackCreateResultRequest,
    TimebackCreateResultBody,
)
from timeback.models.response import TimebackCreateResultResponse
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus, TimebackScoreStatus


class MockHttp:
    def post(self, path, json=None):
        assert path == "/ims/oneroster/gradebook/v1p2/results"
        # Simulate 201 response body with sourcedIdPairs
        return {
            "sourcedIdPairs": {
                "suppliedSourcedId": json["result"].get("sourcedId", "temp-id"),
                "allocatedSourcedId": "allocated-result-123",
            }
        }


def test_create_result_success():
    """Test successful result creation."""
    body = TimebackCreateResultBody(
        sourcedId="result-created",
        lineItem=TimebackSourcedIdReference(sourcedId="line-item-1"),
        student=TimebackSourcedIdReference(sourcedId="student-1"),
        scoreStatus=TimebackScoreStatus.FULLY_GRADED,
        scoreDate="2024-01-15T10:00:00Z",
        score=95.5,
    )
    req = TimebackCreateResultRequest(result=body)
    resp = create_result(MockHttp(), req)
    assert isinstance(resp, TimebackCreateResultResponse)
    assert resp.sourcedIdPairs.allocatedSourcedId == "allocated-result-123"
    assert resp.sourcedIdPairs.suppliedSourcedId == "result-created"


def test_create_result_with_all_fields():
    """Test result creation with all optional fields."""
    body = TimebackCreateResultBody(
        sourcedId="result-full",
        lineItem=TimebackSourcedIdReference(sourcedId="line-item-1"),
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
    req = TimebackCreateResultRequest(result=body)
    resp = create_result(MockHttp(), req)
    assert isinstance(resp, TimebackCreateResultResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "result-full"

