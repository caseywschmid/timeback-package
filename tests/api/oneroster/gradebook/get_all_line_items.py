from timeback import Timeback
from timeback.models.request import (
    TimebackGetAllLineItemsRequest,
    TimebackQueryParams,
)


def main():
    client = Timeback()

    # Example 1: Get all line items with default parameters
    request = TimebackGetAllLineItemsRequest()
    resp = client.oneroster.gradebook.get_all_line_items(request)

    print(f"Total Line Items: {resp.total_count}")
    print(f"Page {resp.page_number} of {resp.page_count}")
    print(f"Showing {len(resp.line_items)} line items")
    print()

    for line_item in resp.line_items:
        print(f"- Line Item {line_item.sourcedId}")
        print(f"  Title: {line_item.title}")
        if line_item.description:
            print(f"  Description: {line_item.description}")
        print(f"  Class: {line_item.class_.sourcedId}")
        print(f"  School: {line_item.school.sourcedId}")
        print(f"  Category: {line_item.category.sourcedId}")
        print(f"  Assign Date: {line_item.assignDate}")
        print(f"  Due Date: {line_item.dueDate}")
        if line_item.scoreScale:
            print(f"  Score Scale: {line_item.scoreScale.sourcedId}")
        if line_item.resultValueMin is not None:
            print(f"  Score Range: {line_item.resultValueMin} - {line_item.resultValueMax}")
        print()

    # Example 2: Get line items with query parameters
    print("\n--- With Query Parameters ---")
    query_params = TimebackQueryParams(limit=10, offset=0, fields="sourcedId,title,assignDate,dueDate")
    request_with_params = TimebackGetAllLineItemsRequest(query_params=query_params)
    resp_filtered = client.oneroster.gradebook.get_all_line_items(request_with_params)

    print(f"Filtered Line Items: {len(resp_filtered.line_items)} line items")


if __name__ == "__main__":
    main()

