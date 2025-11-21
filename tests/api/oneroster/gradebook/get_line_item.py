from timeback import Timeback
from timeback.models.request import (
    TimebackGetLineItemRequest,
    TimebackQueryParams,
)


def main():
    client = Timeback()
    sourced_id = "line-item-123-456"

    # Example 1: Get line item by sourcedId
    print(f"Fetching line item: {sourced_id}")
    request = TimebackGetLineItemRequest(sourced_id=sourced_id)
    resp = client.oneroster.gradebook.get_line_item(request)

    line_item = resp.line_item
    print(f"Found Line Item: {line_item.sourcedId}")
    print(f"Title: {line_item.title}")
    if line_item.description:
        print(f"Description: {line_item.description}")
    print(f"Status: {line_item.status}")
    print(f"Assign Date: {line_item.assignDate}")
    print(f"Due Date: {line_item.dueDate}")
    print(f"Class: {line_item.class_.sourcedId}")
    print(f"School: {line_item.school.sourcedId}")
    print(f"Category: {line_item.category.sourcedId}")
    if line_item.scoreScale:
        print(f"Score Scale: {line_item.scoreScale.sourcedId}")
    if line_item.resultValueMin is not None:
        print(f"Score Range: {line_item.resultValueMin} - {line_item.resultValueMax}")

    # Example 2: Get line item with fields parameter
    print("\n--- With Fields Parameter ---")
    query_params = TimebackQueryParams(fields="sourcedId,title,assignDate,dueDate")
    request_fields = TimebackGetLineItemRequest(
        sourced_id=sourced_id, query_params=query_params
    )
    resp_fields = client.oneroster.gradebook.get_line_item(request_fields)
    
    print(f"Fetched partial line item: {resp_fields.line_item.sourcedId}")
    print(f"Title: {resp_fields.line_item.title}")


if __name__ == "__main__":
    main()

