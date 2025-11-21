from timeback import Timeback
from timeback.models.request import (
    TimebackGetResultRequest,
    TimebackQueryParams,
)


def main():
    client = Timeback()
    sourced_id = "result-123-456"

    # Example 1: Get result by sourcedId
    print(f"Fetching result: {sourced_id}")
    request = TimebackGetResultRequest(sourced_id=sourced_id)
    resp = client.oneroster.gradebook.get_result(request)

    result = resp.result
    print(f"Found Result: {result.sourcedId}")
    print(f"Status: {result.status}")
    print(f"Score Status: {result.scoreStatus}")
    print(f"Score Date: {result.scoreDate}")
    if result.score is not None:
        print(f"Score: {result.score}")
    if result.textScore is not None:
        print(f"Text Score: {result.textScore}")
    if result.comment is not None:
        print(f"Comment: {result.comment}")
    print(f"Line Item: {result.lineItem.sourcedId}")
    print(f"Student: {result.student.sourcedId}")

    # Example 2: Get result with fields parameter
    print("\n--- With Fields Parameter ---")
    query_params = TimebackQueryParams(fields="sourcedId,score,textScore,comment")
    request_fields = TimebackGetResultRequest(
        sourced_id=sourced_id, query_params=query_params
    )
    resp_fields = client.oneroster.gradebook.get_result(request_fields)
    
    print(f"Fetched partial result: {resp_fields.result.sourcedId}")
    if resp_fields.result.score is not None:
        print(f"Score: {resp_fields.result.score}")


if __name__ == "__main__":
    main()

