from timeback.services.oneroster.gradebook.endpoints.put_assessment_result import (
    put_assessment_result,
)
from timeback.models.request import (
    TimebackPutAssessmentResultRequest,
    TimebackPutAssessmentResultBody,
)
from timeback.models.response import TimebackPutAssessmentResultResponse
from timeback.models.timeback_assessment_line_item_ref import TimebackAssessmentLineItemRef
from timeback.models.timeback_student_ref import TimebackStudentRef
from timeback.enums import TimebackScoreStatus


class MockHttp:
    def __init__(self):
        self.last_path = None
        self.last_json = None

    def put(self, path, json=None):
        self.last_path = path
        self.last_json = json
        return {
            "assessmentResult": {
                "sourcedId": "ar-001",
                "status": "active",
                "assessmentLineItem": {"sourcedId": "ali-001"},
                "student": {"sourcedId": "student-001"},
                "scoreDate": "2024-01-15",
                "scoreStatus": "fully graded",
                "score": 90.0,
            }
        }


def test_put_assessment_result_success():
    """Test successful assessment result update."""
    mock_http = MockHttp()
    body = TimebackPutAssessmentResultBody(
        sourcedId="ar-001",
        assessmentLineItem=TimebackAssessmentLineItemRef(sourcedId="ali-001"),
        student=TimebackStudentRef(sourcedId="student-001"),
        scoreStatus=TimebackScoreStatus.FULLY_GRADED,
        scoreDate="2024-01-15",
        score=90.0,
    )
    request = TimebackPutAssessmentResultRequest(
        sourced_id="ar-001",
        assessmentResult=body
    )
    resp = put_assessment_result(mock_http, request)

    assert isinstance(resp, TimebackPutAssessmentResultResponse)
    assert resp.assessmentResult.sourcedId == "ar-001"
    assert resp.assessmentResult.score == 90.0
    assert "/ims/oneroster/gradebook/v1p2/assessmentResults/ar-001" in mock_http.last_path
    assert "sourced_id" not in mock_http.last_json
    assert "assessmentResult" in mock_http.last_json


def test_put_assessment_result_with_optional_fields():
    """Test assessment result update with optional fields."""
    mock_http = MockHttp()
    body = TimebackPutAssessmentResultBody(
        assessmentLineItem=TimebackAssessmentLineItemRef(sourcedId="ali-002"),
        student=TimebackStudentRef(sourcedId="student-002"),
        scoreStatus=TimebackScoreStatus.PARTIALLY_GRADED,
        scoreDate="2024-01-16",
        score=85.5,
        textScore="B+",
        comment="Good improvement!",
    )
    request = TimebackPutAssessmentResultRequest(
        sourced_id="ar-002",
        assessmentResult=body
    )
    resp = put_assessment_result(mock_http, request)

    assert isinstance(resp, TimebackPutAssessmentResultResponse)
    assert mock_http.last_json["assessmentResult"]["textScore"] == "B+"
    assert mock_http.last_json["assessmentResult"]["comment"] == "Good improvement!"


def test_put_assessment_result_minimal_fields():
    """Test assessment result update with only required fields."""
    mock_http = MockHttp()
    body = TimebackPutAssessmentResultBody(
        assessmentLineItem=TimebackAssessmentLineItemRef(sourcedId="ali-003"),
        student=TimebackStudentRef(sourcedId="student-003"),
        scoreStatus=TimebackScoreStatus.NOT_SUBMITTED,
        scoreDate="2024-01-17",
    )
    request = TimebackPutAssessmentResultRequest(
        sourced_id="ar-003",
        assessmentResult=body
    )
    resp = put_assessment_result(mock_http, request)

    assert isinstance(resp, TimebackPutAssessmentResultResponse)
    assert "score" not in mock_http.last_json["assessmentResult"]

