from timeback import Timeback
from timeback.models.request import (
    TimebackCreateResultForLineItemRequest,
    TimebackCreateResultBody,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus, TimebackScoreStatus


def main():
    client = Timeback()
    line_item_sourced_id = "line-item-123-456"

    # Create result bodies
    result1 = TimebackCreateResultBody(
        sourcedId="result-1",
        lineItem=TimebackSourcedIdReference(sourcedId=line_item_sourced_id),
        student=TimebackSourcedIdReference(sourcedId="student-1"),
        scoreStatus=TimebackScoreStatus.FULLY_GRADED,
        scoreDate="2024-01-15T10:00:00Z",
        status=TimebackStatus.ACTIVE,
        score=95.5,
        textScore="A",
        comment="Excellent work",
    )

    result2 = TimebackCreateResultBody(
        sourcedId="result-2",
        lineItem=TimebackSourcedIdReference(sourcedId=line_item_sourced_id),
        student=TimebackSourcedIdReference(sourcedId="student-2"),
        scoreStatus=TimebackScoreStatus.SUBMITTED,
        scoreDate="2024-01-16T10:00:00Z",
        status=TimebackStatus.ACTIVE,
        score=88.0,
        textScore="B+",
        comment="Good work",
    )

    # Create the request
    print(f"Creating results for line item: {line_item_sourced_id}")
    request = TimebackCreateResultForLineItemRequest(
        line_item_sourced_id=line_item_sourced_id,
        results=[result1, result2]
    )

    # Call the API
    resp = client.oneroster.gradebook.create_result_for_line_item(request)

    print(f"Results Created Successfully!")
    print(f"Supplied SourcedId: {resp.sourcedIdPairs.suppliedSourcedId}")
    print(f"Allocated SourcedId: {resp.sourcedIdPairs.allocatedSourcedId}")


if __name__ == "__main__":
    main()

