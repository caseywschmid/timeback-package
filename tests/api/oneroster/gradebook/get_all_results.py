from timeback import Timeback
from timeback.models.request import (
    TimebackGetAllResultsRequest,
    TimebackQueryParams,
)


def main():
    client = Timeback()

    # Example 1: Get all results with default parameters
    request = TimebackGetAllResultsRequest()
    resp = client.oneroster.gradebook.get_all_results(request)

    print(f"Total Results: {resp.total_count}")
    print(f"Page {resp.page_number} of {resp.page_count}")
    print(f"Showing {len(resp.results)} results")
    print()

    for result in resp.results:
        print(f"- Result {result.sourcedId}")
        print(f"  Student: {result.student.sourcedId}")
        print(f"  Line Item: {result.lineItem.sourcedId}")
        print(f"  Score Status: {result.scoreStatus}")
        if result.score is not None:
            print(f"  Score: {result.score}")
        if result.textScore:
            print(f"  Text Score: {result.textScore}")
        print(f"  Score Date: {result.scoreDate}")
        print()

    # Example 2: Get results with query parameters
    print("\n--- With Query Parameters ---")
    query_params = TimebackQueryParams(limit=10, offset=0, fields="sourcedId,scoreStatus,score")
    request_with_params = TimebackGetAllResultsRequest(query_params=query_params)
    resp_filtered = client.oneroster.gradebook.get_all_results(request_with_params)

    print(f"Filtered Results: {len(resp_filtered.results)} results")


if __name__ == "__main__":
    main()

