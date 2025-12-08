from timeback import Timeback
from timeback.models.request import (
    TimebackPatchAssessmentResultRequest,
    TimebackPatchAssessmentResultBody,
)
from timeback.enums import TimebackScoreStatus


def main():
    client = Timeback()
    sourced_id = "test-assessment-result-001"  # Replace with actual sourcedId

    # Partial update - just update the score
    body = TimebackPatchAssessmentResultBody(
        score=95.0,
        comment="Score updated via PATCH",
    )

    request = TimebackPatchAssessmentResultRequest(
        sourced_id=sourced_id,
        assessmentResult=body
    )
    response = client.oneroster.gradebook.patch_assessment_result(request)

    print(f"Assessment result patched: {response.assessmentResult.sourcedId}")
    print(f"  Score: {response.assessmentResult.score}")
    print(f"  Comment: {response.assessmentResult.comment}")


if __name__ == "__main__":
    main()

