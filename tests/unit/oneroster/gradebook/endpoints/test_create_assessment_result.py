from timeback.services.oneroster.gradebook.endpoints.create_assessment_result import (
    create_assessment_result,
)
from timeback.models.request import (
    TimebackCreateAssessmentResultRequest,
    TimebackCreateAssessmentResultBody,
)
from timeback.models.response import TimebackCreateAssessmentResultResponse
from timeback.models.timeback_assessment_line_item_ref import TimebackAssessmentLineItemRef
from timeback.models.timeback_student_ref import TimebackStudentRef
from timeback.enums import TimebackScoreStatus


class MockHttp:
    def __init__(self):
        self.last_path = None
        self.last_json = None

    def post(self, path, json=None):
        self.last_path = path
        self.last_json = json
        return {
            "sourcedIdPairs": {
                "suppliedSourcedId": json["assessmentResult"]["sourcedId"],
                "allocatedSourcedId": "allocated-ar-001",
            }
        }


def test_create_assessment_result_success():
    """Test successful assessment result creation."""
    mock_http = MockHttp()
    body = TimebackCreateAssessmentResultBody(
        sourcedId="ar-001",
        assessmentLineItem=TimebackAssessmentLineItemRef(sourcedId="ali-001"),
        student=TimebackStudentRef(sourcedId="student-001"),
        scoreStatus=TimebackScoreStatus.FULLY_GRADED,
        scoreDate="2024-01-15",
        score=85.5,
    )
    request = TimebackCreateAssessmentResultRequest(assessmentResult=body)
    resp = create_assessment_result(mock_http, request)

    assert isinstance(resp, TimebackCreateAssessmentResultResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "ar-001"
    assert resp.sourcedIdPairs.allocatedSourcedId == "allocated-ar-001"
    assert "/ims/oneroster/gradebook/v1p2/assessmentResults" in mock_http.last_path
    assert mock_http.last_json["assessmentResult"]["sourcedId"] == "ar-001"
    assert mock_http.last_json["assessmentResult"]["score"] == 85.5


def test_create_assessment_result_with_optional_fields():
    """Test assessment result creation with all optional fields."""
    mock_http = MockHttp()
    body = TimebackCreateAssessmentResultBody(
        sourcedId="ar-002",
        assessmentLineItem=TimebackAssessmentLineItemRef(sourcedId="ali-002"),
        student=TimebackStudentRef(sourcedId="student-002"),
        scoreStatus=TimebackScoreStatus.PARTIALLY_GRADED,
        scoreDate="2024-01-16",
        score=92.0,
        textScore="A-",
        comment="Great work!",
        late="false",
        missing="false",
    )
    request = TimebackCreateAssessmentResultRequest(assessmentResult=body)
    resp = create_assessment_result(mock_http, request)

    assert isinstance(resp, TimebackCreateAssessmentResultResponse)
    assert mock_http.last_json["assessmentResult"]["textScore"] == "A-"
    assert mock_http.last_json["assessmentResult"]["comment"] == "Great work!"


def test_create_assessment_result_minimal_fields():
    """Test assessment result creation with only required fields."""
    mock_http = MockHttp()
    body = TimebackCreateAssessmentResultBody(
        assessmentLineItem=TimebackAssessmentLineItemRef(sourcedId="ali-003"),
        student=TimebackStudentRef(sourcedId="student-003"),
        scoreStatus=TimebackScoreStatus.NOT_SUBMITTED,
        scoreDate="2024-01-17",
    )
    request = TimebackCreateAssessmentResultRequest(assessmentResult=body)
    resp = create_assessment_result(mock_http, request)

    assert isinstance(resp, TimebackCreateAssessmentResultResponse)
    # sourcedId should be auto-generated (UUID)
    assert mock_http.last_json["assessmentResult"]["sourcedId"] is not None
    assert "score" not in mock_http.last_json["assessmentResult"]

