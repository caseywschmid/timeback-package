from timeback import Timeback
from timeback.models.request import TimebackGetAllAssessmentLineItemsRequest, TimebackQueryParams


def main():
    client = Timeback()

    # Basic request without query params
    request = TimebackGetAllAssessmentLineItemsRequest()
    response = client.oneroster.gradebook.get_all_assessment_line_items(request)

    print(f"Total assessment line items: {response.total_count}")
    print(f"Page {response.page_number} of {response.page_count}")
    print(f"Showing {len(response.assessmentLineItems)} items\n")

    for ali in response.assessmentLineItems[:5]:  # Show first 5
        print(f"  - {ali.sourcedId}: {ali.title}")

    # Example with query params
    query_params = TimebackQueryParams(limit=10, offset=0, sort="title", order_by="asc")
    request_with_params = TimebackGetAllAssessmentLineItemsRequest(query_params=query_params)
    response_paged = client.oneroster.gradebook.get_all_assessment_line_items(request_with_params)
    print(f"\nWith pagination: {len(response_paged.assessmentLineItems)} items")


if __name__ == "__main__":
    main()

