from timeback.services.oneroster.gradebook.endpoints.get_all_assessment_results import (
    get_all_assessment_results,
)
from timeback.models.request import (
    TimebackGetAllAssessmentResultsRequest,
    TimebackQueryParams,
)
from timeback.models.response import TimebackGetAllAssessmentResultsResponse


class MockHttp:
    def __init__(self):
        self.last_path = None
        self.last_params = None

    def get(self, path, params=None):
        self.last_path = path
        self.last_params = params
        return {
            "assessmentResults": [
                {
                    "sourcedId": "ar-001",
                    "status": "active",
                    "assessmentLineItem": {"sourcedId": "ali-001"},
                    "student": {"sourcedId": "student-001"},
                    "scoreDate": "2024-01-15",
                    "scoreStatus": "fully graded",
                    "score": 85.5,
                },
                {
                    "sourcedId": "ar-002",
                    "status": "active",
                    "assessmentLineItem": {"sourcedId": "ali-002"},
                    "student": {"sourcedId": "student-002"},
                    "scoreDate": "2024-01-16",
                    "scoreStatus": "partially graded",
                    "score": 92.0,
                },
            ],
            "totalCount": 2,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }


def test_get_all_assessment_results_success():
    """Test successful assessment results retrieval."""
    mock_http = MockHttp()
    request = TimebackGetAllAssessmentResultsRequest()
    resp = get_all_assessment_results(mock_http, request)

    assert isinstance(resp, TimebackGetAllAssessmentResultsResponse)
    assert len(resp.assessmentResults) == 2
    assert resp.assessmentResults[0].sourcedId == "ar-001"
    assert resp.assessmentResults[0].score == 85.5
    assert resp.total_count == 2
    assert resp.page_count == 1
    assert "/ims/oneroster/gradebook/v1p2/assessmentResults" in mock_http.last_path


def test_get_all_assessment_results_with_query_params():
    """Test assessment results retrieval with query parameters."""
    mock_http = MockHttp()
    query_params = TimebackQueryParams(
        limit=50,
        offset=10,
        sort="scoreDate",
        order_by="desc",
    )
    request = TimebackGetAllAssessmentResultsRequest(query_params=query_params)
    resp = get_all_assessment_results(mock_http, request)

    assert isinstance(resp, TimebackGetAllAssessmentResultsResponse)
    assert mock_http.last_params == {
        "limit": 50,
        "offset": 10,
        "sort": "scoreDate",
        "orderBy": "desc",
    }


def test_get_all_assessment_results_empty_list():
    """Test assessment results retrieval with empty list."""
    class MockHttpEmpty:
        def get(self, path, params=None):
            return {
                "assessmentResults": [],
                "totalCount": 0,
                "pageCount": 0,
                "pageNumber": 0,
                "offset": 0,
                "limit": 100,
            }

    request = TimebackGetAllAssessmentResultsRequest()
    resp = get_all_assessment_results(MockHttpEmpty(), request)

    assert isinstance(resp, TimebackGetAllAssessmentResultsResponse)
    assert len(resp.assessmentResults) == 0
    assert resp.total_count == 0

