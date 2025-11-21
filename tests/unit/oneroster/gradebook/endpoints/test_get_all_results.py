from timeback.services.oneroster.gradebook.endpoints.get_all_results import (
    get_all_results,
)
from timeback.models.request import (
    TimebackGetAllResultsRequest,
    TimebackQueryParams,
)
from timeback.models.response import TimebackGetAllResultsResponse
from timeback.enums import TimebackStatus, TimebackScoreStatus


class MockHttp:
    def get(self, path, params=None):
        assert path == "/ims/oneroster/gradebook/v1p2/results"
        # Simulate 200 response body
        return {
            "results": [
                {
                    "sourcedId": "result-1",
                    "status": "active",
                    "dateLastModified": "2024-01-01T00:00:00Z",
                    "metadata": {},
                    "lineItem": {"sourcedId": "line-item-1"},
                    "student": {"sourcedId": "student-1"},
                    "class": {"sourcedId": "class-1"},
                    "scoreScale": {"sourcedId": "scale-1"},
                    "scoreStatus": "fully graded",
                    "score": 95.5,
                    "textScore": "A",
                    "scoreDate": "2024-01-15T10:00:00Z",
                    "comment": "Excellent work",
                }
            ],
            "totalCount": 1,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }


def test_get_all_results_success():
    request = TimebackGetAllResultsRequest()
    resp = get_all_results(MockHttp(), request)
    assert isinstance(resp, TimebackGetAllResultsResponse)
    assert len(resp.results) == 1
    assert resp.results[0].sourcedId == "result-1"
    assert resp.results[0].status == TimebackStatus.ACTIVE
    assert resp.results[0].scoreStatus == TimebackScoreStatus.FULLY_GRADED
    assert resp.results[0].score == 95.5
    assert resp.results[0].lineItem.sourcedId == "line-item-1"
    assert resp.results[0].student.sourcedId == "student-1"
    assert resp.total_count == 1
    assert resp.limit == 100


def test_get_all_results_with_query_params():
    query_params = TimebackQueryParams(limit=50, offset=10, fields="sourcedId,scoreStatus")
    request = TimebackGetAllResultsRequest(query_params=query_params)
    resp = get_all_results(MockHttp(), request)
    assert isinstance(resp, TimebackGetAllResultsResponse)
    assert len(resp.results) == 1

