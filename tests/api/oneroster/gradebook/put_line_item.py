from timeback import Timeback
from timeback.models.request import (
    TimebackPutLineItemRequest,
    TimebackPutLineItemBody,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus


def main():
    client = Timeback()
    sourced_id = "line-item-123-456"

    # Create the line item body
    line_item_body = TimebackPutLineItemBody(
        sourcedId=sourced_id,
        title="Updated Math Quiz 1",
        assignDate="2024-01-15T00:00:00Z",
        dueDate="2024-01-20T23:59:59Z",
        class_=TimebackSourcedIdReference(sourcedId="class-1"),
        school=TimebackSourcedIdReference(sourcedId="school-1"),
        category=TimebackSourcedIdReference(sourcedId="category-1"),
        status=TimebackStatus.ACTIVE,
        description="Updated quiz description",
        scoreScale=TimebackSourcedIdReference(sourcedId="scale-1"),
        resultValueMin=0.0,
        resultValueMax=100.0,
    )

    # Create the request
    print(f"Updating/creating line item: {sourced_id}")
    request = TimebackPutLineItemRequest(
        sourced_id=sourced_id, lineItem=line_item_body
    )

    # Call the API
    resp = client.oneroster.gradebook.put_line_item(request)

    print(f"Line Item Updated/Created Successfully!")
    print(f"SourcedId: {resp.line_item.sourcedId}")
    print(f"Title: {resp.line_item.title}")
    print(f"Status: {resp.line_item.status}")
    if resp.line_item.description:
        print(f"Description: {resp.line_item.description}")
    print(f"Assign Date: {resp.line_item.assignDate}")
    print(f"Due Date: {resp.line_item.dueDate}")
    print(f"Class: {resp.line_item.class_.sourcedId}")
    print(f"School: {resp.line_item.school.sourcedId}")
    print(f"Category: {resp.line_item.category.sourcedId}")


if __name__ == "__main__":
    main()

