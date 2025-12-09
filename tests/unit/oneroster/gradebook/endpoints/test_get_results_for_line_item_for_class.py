from timeback.services.oneroster.gradebook.endpoints.get_results_for_line_item_for_class import (
    get_results_for_line_item_for_class,
)
from timeback.models.request import (
    TimebackGetResultsForLineItemForClassRequest,
    TimebackQueryParams,
)
from timeback.models.response import TimebackGetAllResultsResponse
from timeback.enums import TimebackStatus, TimebackScoreStatus


class MockHttp:
    def get(self, path, params=None):
        assert path.startswith("/ims/oneroster/gradebook/v1p2/classes/")
        assert "/lineItems/" in path
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
                    "student": {"sourcedId": "student-1"},
                    "class": {"sourcedId": "class-456"},
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


def test_get_results_for_line_item_for_class_success():
    """Test successful retrieval of results for a line item and class."""
    request = TimebackGetResultsForLineItemForClassRequest(
        class_sourced_id="class-456",
        line_item_sourced_id="line-item-123"
    )
    resp = get_results_for_line_item_for_class(MockHttp(), request)
    
    assert isinstance(resp, TimebackGetAllResultsResponse)
    assert len(resp.results) == 1
    assert resp.results[0].sourcedId == "result-1"
    assert resp.results[0].status == TimebackStatus.ACTIVE
    assert resp.results[0].scoreStatus == TimebackScoreStatus.FULLY_GRADED
    assert resp.results[0].score == 95.5
    assert resp.results[0].lineItem.sourcedId == "line-item-123"
    assert resp.results[0].student.sourcedId == "student-1"
    assert resp.results[0].class_.sourcedId == "class-456"
    assert resp.total_count == 1
    assert resp.limit == 100


def test_get_results_for_line_item_for_class_with_query_params():
    """Test retrieval with query parameters."""
    query_params = TimebackQueryParams(limit=50, offset=10, fields="sourcedId,scoreStatus")
    request = TimebackGetResultsForLineItemForClassRequest(
        class_sourced_id="class-456",
        line_item_sourced_id="line-item-123",
        query_params=query_params
    )
    resp = get_results_for_line_item_for_class(MockHttp(), request)
    
    assert isinstance(resp, TimebackGetAllResultsResponse)
    assert len(resp.results) == 1

