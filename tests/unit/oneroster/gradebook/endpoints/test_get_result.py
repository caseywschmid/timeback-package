from timeback.services.oneroster.gradebook.endpoints.get_result import (
    get_result,
)
from timeback.models.request import (
    TimebackGetResultRequest,
    TimebackQueryParams,
)
from timeback.models.response import TimebackGetResultResponse
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus, TimebackScoreStatus


class MockHttp:
    def get(self, path, params=None):
        assert path == "/ims/oneroster/gradebook/v1p2/results/result-123"
        # Simulate 200 response body
        return {
            "result": {
                "sourcedId": "result-123",
                "status": "active",
                "dateLastModified": "2024-01-01T00:00:00Z",
                "metadata": {},
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


def test_get_result_success():
    request = TimebackGetResultRequest(sourced_id="result-123")
    resp = get_result(MockHttp(), request)
    assert isinstance(resp, TimebackGetResultResponse)
    assert resp.result.sourcedId == "result-123"
    assert resp.result.score == 95.5
    assert resp.result.textScore == "A"
    assert resp.result.comment == "Excellent work"


def test_get_result_with_fields():
    query_params = TimebackQueryParams(fields="sourcedId,score,textScore")
    request = TimebackGetResultRequest(
        sourced_id="result-123", query_params=query_params
    )
    resp = get_result(MockHttp(), request)
    assert isinstance(resp, TimebackGetResultResponse)
    assert resp.result.sourcedId == "result-123"

