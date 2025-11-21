from timeback import Timeback
from timeback.models.request import (
    TimebackPostResultsForAcademicSessionForClassRequest,
    TimebackCreateResultBody,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus, TimebackScoreStatus


def main():
    client = Timeback()
    class_sourced_id = "class-123-456"
    academic_session_sourced_id = "session-789-012"

    # Create result bodies
    result1 = TimebackCreateResultBody(
        sourcedId="result-1",
        lineItem=TimebackSourcedIdReference(sourcedId="line-item-1"),
        student=TimebackSourcedIdReference(sourcedId="student-1"),
        scoreStatus=TimebackScoreStatus.FULLY_GRADED,
        scoreDate="2024-01-15T10:00:00Z",
        status=TimebackStatus.ACTIVE,
        score=95.5,
        textScore="A",
        comment="Excellent work",
        class_=TimebackSourcedIdReference(sourcedId=class_sourced_id),
    )

    result2 = TimebackCreateResultBody(
        sourcedId="result-2",
        lineItem=TimebackSourcedIdReference(sourcedId="line-item-1"),
        student=TimebackSourcedIdReference(sourcedId="student-2"),
        scoreStatus=TimebackScoreStatus.SUBMITTED,
        scoreDate="2024-01-16T10:00:00Z",
        status=TimebackStatus.ACTIVE,
        score=88.0,
        textScore="B+",
        comment="Good work",
        class_=TimebackSourcedIdReference(sourcedId=class_sourced_id),
    )

    # Create the request
    print(f"Creating results for class: {class_sourced_id} and academic session: {academic_session_sourced_id}")
    request = TimebackPostResultsForAcademicSessionForClassRequest(
        class_sourced_id=class_sourced_id,
        academic_session_sourced_id=academic_session_sourced_id,
        results=[result1, result2]
    )

    # Call the API
    resp = client.oneroster.gradebook.post_results_for_academic_session_for_class(request)

    print(f"Results Created Successfully!")
    print(f"Supplied SourcedId: {resp.sourcedIdPairs.suppliedSourcedId}")
    print(f"Allocated SourcedId: {resp.sourcedIdPairs.allocatedSourcedId}")


if __name__ == "__main__":
    main()

