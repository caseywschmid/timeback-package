from timeback.services.oneroster.gradebook.endpoints.get_results_for_student_for_class import (
    get_results_for_student_for_class,
)
from timeback.models.request import (
    TimebackGetResultsForStudentForClassRequest,
    TimebackQueryParams,
)
from timeback.models.response import TimebackGetAllResultsResponse
from timeback.enums import TimebackStatus, TimebackScoreStatus


class MockHttp:
    def get(self, path, params=None):
        assert path.startswith("/ims/oneroster/gradebook/v1p2/classes/")
        assert "/students/" in path
        assert path.endswith("/results")
        # Simulate 200 response body
        return {
            "results": [
                {
                    "sourcedId": "result-1",
                    "status": "active",
                    "dateLastModified": "2024-01-01T00:00:00Z",
                    "metadata": {},
                    "lineItem": {"sourcedId": "line-item-123"},
                    "student": {"sourcedId": "student-456"},
                    "class": {"sourcedId": "class-789"},
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


def test_get_results_for_student_for_class_success():
    """Test successful retrieval of results for a student and class."""
    request = TimebackGetResultsForStudentForClassRequest(
        class_sourced_id="class-789",
        student_sourced_id="student-456"
    )
    resp = get_results_for_student_for_class(MockHttp(), request)
    
    assert isinstance(resp, TimebackGetAllResultsResponse)
    assert len(resp.results) == 1
    assert resp.results[0].sourcedId == "result-1"
    assert resp.results[0].status == TimebackStatus.ACTIVE
    assert resp.results[0].scoreStatus == TimebackScoreStatus.FULLY_GRADED
    assert resp.results[0].score == 95.5
    assert resp.results[0].lineItem.sourcedId == "line-item-123"
    assert resp.results[0].student.sourcedId == "student-456"
    assert resp.results[0].class_.sourcedId == "class-789"
    assert resp.total_count == 1
    assert resp.limit == 100


def test_get_results_for_student_for_class_with_query_params():
    """Test retrieval with query parameters."""
    query_params = TimebackQueryParams(limit=50, offset=10, fields="sourcedId,scoreStatus")
    request = TimebackGetResultsForStudentForClassRequest(
        class_sourced_id="class-789",
        student_sourced_id="student-456",
        query_params=query_params
    )
    resp = get_results_for_student_for_class(MockHttp(), request)
    
    assert isinstance(resp, TimebackGetAllResultsResponse)
    assert len(resp.results) == 1

