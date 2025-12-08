from timeback.services.oneroster.gradebook.endpoints.get_assessment_result import (
    get_assessment_result,
)
from timeback.models.request import (
    TimebackGetAssessmentResultRequest,
    TimebackQueryParams,
)
from timeback.models.response import TimebackGetAssessmentResultResponse
from timeback.enums import TimebackStatus, TimebackScoreStatus


class MockHttp:
    def __init__(self):
        self.last_path = None
        self.last_params = None

    def get(self, path, params=None):
        self.last_path = path
        self.last_params = params
        return {
            "assessmentResult": {
                "sourcedId": "ar-001",
                "status": "active",
                "assessmentLineItem": {"sourcedId": "ali-001"},
                "student": {"sourcedId": "student-001"},
                "scoreDate": "2024-01-15",
                "scoreStatus": "fully graded",
                "score": 85.5,
            }
        }


def test_get_assessment_result_success():
    """Test successful assessment result retrieval."""
    mock_http = MockHttp()
    request = TimebackGetAssessmentResultRequest(sourced_id="ar-001")
    resp = get_assessment_result(mock_http, request)

    assert isinstance(resp, TimebackGetAssessmentResultResponse)
    assert resp.assessmentResult.sourcedId == "ar-001"
    assert resp.assessmentResult.status == TimebackStatus.ACTIVE
    assert resp.assessmentResult.score == 85.5
    assert resp.assessmentResult.scoreStatus == TimebackScoreStatus.FULLY_GRADED
    assert "/ims/oneroster/gradebook/v1p2/assessmentResults/ar-001" in mock_http.last_path


def test_get_assessment_result_with_fields_param():
    """Test assessment result retrieval with fields parameter."""
    mock_http = MockHttp()
    query_params = TimebackQueryParams(fields=["sourcedId", "score", "scoreStatus"])
    request = TimebackGetAssessmentResultRequest(
        sourced_id="ar-002",
        query_params=query_params
    )
    resp = get_assessment_result(mock_http, request)

    assert isinstance(resp, TimebackGetAssessmentResultResponse)
    assert "/ims/oneroster/gradebook/v1p2/assessmentResults/ar-002" in mock_http.last_path
    assert mock_http.last_params == {"fields": "sourcedId,score,scoreStatus"}


def test_get_assessment_result_minimal_response():
    """Test assessment result retrieval with minimal response fields."""
    class MockHttpMinimal:
        def get(self, path, params=None):
            return {
                "assessmentResult": {
                    "sourcedId": "ar-003",
                    "status": "active",
                    "assessmentLineItem": {"sourcedId": "ali-003"},
                    "student": {"sourcedId": "student-003"},
                    "scoreDate": "2024-01-17",
                    "scoreStatus": "not submitted",
                }
            }

    request = TimebackGetAssessmentResultRequest(sourced_id="ar-003")
    resp = get_assessment_result(MockHttpMinimal(), request)

    assert isinstance(resp, TimebackGetAssessmentResultResponse)
    assert resp.assessmentResult.sourcedId == "ar-003"
    assert resp.assessmentResult.score is None  # Optional field not provided
    assert resp.assessmentResult.scoreStatus == TimebackScoreStatus.NOT_SUBMITTED

