from timeback import Timeback
from timeback.models.request import (
    TimebackPostLineItemsForClassRequest,
    TimebackCreateLineItemBody,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus


def main():
    client = Timeback()
    class_sourced_id = "class-123-456"

    # Create line item bodies
    line_item1 = TimebackCreateLineItemBody(
        sourcedId="line-item-1",
        title="Math Quiz 1",
        assignDate="2024-01-15T00:00:00Z",
        dueDate="2024-01-20T23:59:59Z",
        class_=TimebackSourcedIdReference(sourcedId=class_sourced_id),
        school=TimebackSourcedIdReference(sourcedId="school-1"),
        category=TimebackSourcedIdReference(sourcedId="category-1"),
        status=TimebackStatus.ACTIVE,
        description="First quiz of the semester",
        scoreScale=TimebackSourcedIdReference(sourcedId="scale-1"),
        resultValueMin=0.0,
        resultValueMax=100.0,
    )

    line_item2 = TimebackCreateLineItemBody(
        sourcedId="line-item-2",
        title="Math Quiz 2",
        assignDate="2024-01-22T00:00:00Z",
        dueDate="2024-01-27T23:59:59Z",
        class_=TimebackSourcedIdReference(sourcedId=class_sourced_id),
        school=TimebackSourcedIdReference(sourcedId="school-1"),
        category=TimebackSourcedIdReference(sourcedId="category-1"),
        status=TimebackStatus.ACTIVE,
        description="Second quiz of the semester",
        scoreScale=TimebackSourcedIdReference(sourcedId="scale-1"),
        resultValueMin=0.0,
        resultValueMax=100.0,
    )

    # Create the request
    print(f"Creating line items for class: {class_sourced_id}")
    request = TimebackPostLineItemsForClassRequest(
        class_sourced_id=class_sourced_id,
        lineItems=[line_item1, line_item2]
    )

    # Call the API
    resp = client.oneroster.gradebook.post_line_items_for_class(request)

    print(f"Line Items Created Successfully!")
    print(f"Supplied SourcedId: {resp.sourcedIdPairs.suppliedSourcedId}")
    print(f"Allocated SourcedId: {resp.sourcedIdPairs.allocatedSourcedId}")


if __name__ == "__main__":
    main()

