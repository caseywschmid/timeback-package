from timeback.services.oneroster.gradebook.endpoints.put_result import (
    put_result,
)
from timeback.models.request import (
    TimebackPutResultRequest,
    TimebackPutResultBody,
)
from timeback.models.response import TimebackPutResultResponse
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus, TimebackScoreStatus


class MockHttp:
    def put(self, path, json=None):
        assert path.startswith("/ims/oneroster/gradebook/v1p2/results/")
        assert json is not None
        assert "result" in json
        # Extract sourcedId from path
        sourced_id = path.split("/")[-1]
        # Simulate 201 response body
        return {
            "result": {
                "sourcedId": sourced_id,
                "status": "active",
                "dateLastModified": "2024-01-01T00:00:00Z",
                "metadata": json.get("result", {}).get("metadata", {}),
                "lineItem": {"sourcedId": "line-item-1"},
                "student": {"sourcedId": "student-1"},
                "scoreStatus": "fully graded",
                "scoreDate": "2024-01-15T10:00:00Z",
                "score": 95.5,
                "textScore": "A",
                "comment": "Excellent work",
                "class": {"sourcedId": "class-1"},
                "scoreScale": {"sourcedId": "scale-1"},
            }
        }


def test_put_result_success():
    """Test successful result update/create."""
    body = TimebackPutResultBody(
        sourcedId="result-123",
        lineItem=TimebackSourcedIdReference(sourcedId="line-item-1"),
        student=TimebackSourcedIdReference(sourcedId="student-1"),
        scoreStatus=TimebackScoreStatus.FULLY_GRADED,
        scoreDate="2024-01-15T10:00:00Z",
        score=95.5,
        textScore="A",
        comment="Excellent work",
        class_=TimebackSourcedIdReference(sourcedId="class-1"),
        scoreScale=TimebackSourcedIdReference(sourcedId="scale-1"),
    )
    request = TimebackPutResultRequest(
        sourced_id="result-123", result=body
    )
    resp = put_result(MockHttp(), request)
    
    assert isinstance(resp, TimebackPutResultResponse)
    assert resp.result.sourcedId == "result-123"
    assert resp.result.score == 95.5
    assert resp.result.textScore == "A"
    assert resp.result.comment == "Excellent work"


def test_put_result_with_all_fields():
    """Test result update/create with all optional fields."""
    body = TimebackPutResultBody(
        sourcedId="result-456",
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
        metadata={"key": "value"},
    )
    request = TimebackPutResultRequest(
        sourced_id="result-456", result=body
    )
    resp = put_result(MockHttp(), request)
    
    assert isinstance(resp, TimebackPutResultResponse)
    assert resp.result.sourcedId == "result-456"  # Mock returns sourcedId from path

