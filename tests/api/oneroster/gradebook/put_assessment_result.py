from timeback import Timeback
from timeback.models.request import (
    TimebackPutAssessmentResultRequest,
    TimebackPutAssessmentResultBody,
)
from timeback.models.timeback_assessment_line_item_ref import TimebackAssessmentLineItemRef
from timeback.models.timeback_student_ref import TimebackStudentRef
from timeback.enums import TimebackScoreStatus


def main():
    client = Timeback()
    sourced_id = "test-assessment-result-001"  # Replace with actual sourcedId

    body = TimebackPutAssessmentResultBody(
        sourcedId=sourced_id,
        assessmentLineItem=TimebackAssessmentLineItemRef(sourcedId="<assessment-line-item-id>"),
        student=TimebackStudentRef(sourcedId="<student-id>"),
        scoreStatus=TimebackScoreStatus.FULLY_GRADED,
        scoreDate="2024-01-15",
        score=92.5,
        comment="Updated score",
    )

    request = TimebackPutAssessmentResultRequest(
        sourced_id=sourced_id,
        assessmentResult=body
    )
    response = client.oneroster.gradebook.put_assessment_result(request)

    print(f"Assessment result updated: {response.assessmentResult.sourcedId}")
    print(f"  Score: {response.assessmentResult.score}")
    print(f"  Status: {response.assessmentResult.scoreStatus}")


if __name__ == "__main__":
    main()

