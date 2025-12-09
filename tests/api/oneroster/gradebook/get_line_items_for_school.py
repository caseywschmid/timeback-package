from timeback import Timeback
from timeback.models.request import (
    TimebackGetLineItemsForSchoolRequest,
    TimebackQueryParams,
)


def main():
    client = Timeback()
    school_sourced_id = "school-123"

    # Example 1: Get line items for a school with default parameters
    print(f"Getting line items for school: {school_sourced_id}")
    request = TimebackGetLineItemsForSchoolRequest(school_sourced_id=school_sourced_id)
    resp = client.oneroster.gradebook.get_line_items_for_school(request)

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
    request_with_params = TimebackGetLineItemsForSchoolRequest(
        school_sourced_id=school_sourced_id,
        query_params=query_params
    )
    resp_filtered = client.oneroster.gradebook.get_line_items_for_school(request_with_params)

    print(f"Filtered Line Items: {len(resp_filtered.line_items)} line items")


if __name__ == "__main__":
    main()

