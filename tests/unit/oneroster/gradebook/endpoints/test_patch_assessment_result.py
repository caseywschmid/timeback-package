from timeback.services.oneroster.gradebook.endpoints.patch_assessment_result import (
    patch_assessment_result,
)
from timeback.models.request import (
    TimebackPatchAssessmentResultRequest,
    TimebackPatchAssessmentResultBody,
)
from timeback.models.response import TimebackPatchAssessmentResultResponse
from timeback.enums import TimebackScoreStatus


class MockHttp:
    def __init__(self):
        self.last_path = None
        self.last_json = None

    def patch(self, path, json=None):
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
                "score": 95.0,
                "comment": "Updated comment",
            }
        }


def test_patch_assessment_result_score_only():
    """Test partial update of just the score."""
    mock_http = MockHttp()
    body = TimebackPatchAssessmentResultBody(score=95.0)
    request = TimebackPatchAssessmentResultRequest(
        sourced_id="ar-001",
        assessmentResult=body
    )
    resp = patch_assessment_result(mock_http, request)

    assert isinstance(resp, TimebackPatchAssessmentResultResponse)
    assert resp.assessmentResult.sourcedId == "ar-001"
    assert resp.assessmentResult.score == 95.0
    assert "/ims/oneroster/gradebook/v1p2/assessmentResults/ar-001" in mock_http.last_path
    assert mock_http.last_json["assessmentResult"]["score"] == 95.0
    # Should not have other fields
    assert "student" not in mock_http.last_json["assessmentResult"]


def test_patch_assessment_result_multiple_fields():
    """Test partial update of multiple fields."""
    mock_http = MockHttp()
    body = TimebackPatchAssessmentResultBody(
        score=95.0,
        comment="Updated comment",
        scoreStatus=TimebackScoreStatus.FULLY_GRADED,
    )
    request = TimebackPatchAssessmentResultRequest(
        sourced_id="ar-001",
        assessmentResult=body
    )
    resp = patch_assessment_result(mock_http, request)

    assert isinstance(resp, TimebackPatchAssessmentResultResponse)
    assert mock_http.last_json["assessmentResult"]["score"] == 95.0
    assert mock_http.last_json["assessmentResult"]["comment"] == "Updated comment"


def test_patch_assessment_result_metadata_merge():
    """Test partial update with metadata (should merge with existing)."""
    mock_http = MockHttp()
    body = TimebackPatchAssessmentResultBody(
        metadata={"newField": "newValue", "anotherField": 123}
    )
    request = TimebackPatchAssessmentResultRequest(
        sourced_id="ar-002",
        assessmentResult=body
    )
    resp = patch_assessment_result(mock_http, request)

    assert isinstance(resp, TimebackPatchAssessmentResultResponse)
    assert mock_http.last_json["assessmentResult"]["metadata"] == {
        "newField": "newValue",
        "anotherField": 123
    }

