from timeback import Timeback
from timeback.models.request import TimebackGetAllAssessmentResultsRequest, TimebackQueryParams


def main():
    client = Timeback()

    # Basic request without query params
    request = TimebackGetAllAssessmentResultsRequest()
    response = client.oneroster.gradebook.get_all_assessment_results(request)

    print(f"Total assessment results: {response.total_count}")
    print(f"Page {response.page_number} of {response.page_count}")
    print(f"Showing {len(response.assessmentResults)} results\n")

    for ar in response.assessmentResults[:5]:  # Show first 5
        print(f"  - {ar.sourcedId}: score={ar.score}, status={ar.scoreStatus}")

    # Example with query params
    query_params = TimebackQueryParams(limit=10, offset=0, sort="scoreDate", order_by="desc")
    request_with_params = TimebackGetAllAssessmentResultsRequest(query_params=query_params)
    response_paged = client.oneroster.gradebook.get_all_assessment_results(request_with_params)
    print(f"\nWith pagination: {len(response_paged.assessmentResults)} results")


if __name__ == "__main__":
    main()

