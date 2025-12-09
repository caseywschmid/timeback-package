from timeback import Timeback
from timeback.models.request import (
    TimebackCreateResultRequest,
    TimebackCreateResultBody,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus, TimebackScoreStatus


def main():
    client = Timeback()

    # Basic result creation
    body = TimebackCreateResultBody(
        sourcedId="test-result-001",  # Optional; auto-generated if omitted
        lineItem=TimebackSourcedIdReference(sourcedId="line-item-1"),
        student=TimebackSourcedIdReference(sourcedId="student-1"),
        scoreStatus=TimebackScoreStatus.FULLY_GRADED,
        scoreDate="2024-01-15T10:00:00Z",
        score=95.5,
    )
    req = TimebackCreateResultRequest(result=body)
    response = client.oneroster.gradebook.create_result(req)
    print(f"Created result: {response.sourcedIdPairs.suppliedSourcedId} -> {response.sourcedIdPairs.allocatedSourcedId}")

    # Result creation with all fields
    body_with_all_fields = TimebackCreateResultBody(
        sourcedId="test-result-002",
        lineItem=TimebackSourcedIdReference(sourcedId="line-item-1"),
        student=TimebackSourcedIdReference(sourcedId="student-1"),
        scoreStatus=TimebackScoreStatus.FULLY_GRADED,
        scoreDate="2024-01-15T10:00:00Z",
        status=TimebackStatus.ACTIVE,
        score=95.5,
        textScore="A",
        comment="Excellent work",
        class_=TimebackSourcedIdReference(sourcedId="class-1"),
        scoreScale=TimebackSourcedIdReference(sourcedId="scale-1"),
    )
    req_with_all_fields = TimebackCreateResultRequest(result=body_with_all_fields)
    response_with_all_fields = client.oneroster.gradebook.create_result(req_with_all_fields)
    print(f"Created result with all fields: {response_with_all_fields.sourcedIdPairs.suppliedSourcedId} -> {response_with_all_fields.sourcedIdPairs.allocatedSourcedId}")


if __name__ == "__main__":
    main()

