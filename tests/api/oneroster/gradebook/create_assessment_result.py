from timeback import Timeback
from timeback.models.request import (
    TimebackCreateAssessmentResultRequest,
    TimebackCreateAssessmentResultBody,
)
from timeback.models.timeback_assessment_line_item_ref import TimebackAssessmentLineItemRef
from timeback.models.timeback_student_ref import TimebackStudentRef
from timeback.enums import TimebackScoreStatus


def main():
    client = Timeback()

    # Create assessment result body with required fields
    body = TimebackCreateAssessmentResultBody(
        assessmentLineItem=TimebackAssessmentLineItemRef(sourcedId="<assessment-line-item-sourced-id>"),
        student=TimebackStudentRef(sourcedId="<student-sourced-id>"),
        scoreStatus=TimebackScoreStatus.FULLY_GRADED,
        scoreDate="2024-01-15",
        score=85.5,
        comment="Good work!",
    )

    request = TimebackCreateAssessmentResultRequest(assessmentResult=body)
    response = client.oneroster.gradebook.create_assessment_result(request)

    print(f"Assessment result created!")
    print(f"  Supplied sourcedId: {response.sourcedIdPairs.suppliedSourcedId}")
    print(f"  Allocated sourcedId: {response.sourcedIdPairs.allocatedSourcedId}")


if __name__ == "__main__":
    main()

