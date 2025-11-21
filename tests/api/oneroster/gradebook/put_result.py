from timeback import Timeback
from timeback.models.request import (
    TimebackPutResultRequest,
    TimebackPutResultBody,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus, TimebackScoreStatus


def main():
    client = Timeback()
    sourced_id = "result-123-456"

    # Create the result body
    result_body = TimebackPutResultBody(
        sourcedId=sourced_id,
        lineItem=TimebackSourcedIdReference(sourcedId="line-item-1"),
        student=TimebackSourcedIdReference(sourcedId="student-1"),
        scoreStatus=TimebackScoreStatus.FULLY_GRADED,
        scoreDate="2024-01-15T10:00:00Z",
        status=TimebackStatus.ACTIVE,
        score=95.5,
        textScore="A",
        comment="Excellent work - updated",
        class_=TimebackSourcedIdReference(sourcedId="class-1"),
        scoreScale=TimebackSourcedIdReference(sourcedId="scale-1"),
    )

    # Create the request
    print(f"Updating/creating result: {sourced_id}")
    request = TimebackPutResultRequest(
        sourced_id=sourced_id, result=result_body
    )

    # Call the API
    resp = client.oneroster.gradebook.put_result(request)

    print(f"Result Updated/Created Successfully!")
    print(f"SourcedId: {resp.result.sourcedId}")
    print(f"Status: {resp.result.status}")
    print(f"Score Status: {resp.result.scoreStatus}")
    print(f"Score: {resp.result.score}")
    if resp.result.textScore:
        print(f"Text Score: {resp.result.textScore}")
    if resp.result.comment:
        print(f"Comment: {resp.result.comment}")
    print(f"Line Item: {resp.result.lineItem.sourcedId}")
    print(f"Student: {resp.result.student.sourcedId}")


if __name__ == "__main__":
    main()

