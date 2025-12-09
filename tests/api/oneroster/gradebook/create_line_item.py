from timeback import Timeback
from timeback.models.request import (
    TimebackCreateLineItemRequest,
    TimebackCreateLineItemBody,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus


def main():
    client = Timeback()

    # Basic line item creation
    body = TimebackCreateLineItemBody(
        sourcedId="test-line-item-001",  # Optional; auto-generated if omitted
        title="Math Quiz 1",
        assignDate="2024-01-15T00:00:00Z",
        dueDate="2024-01-20T23:59:59Z",
        class_=TimebackSourcedIdReference(sourcedId="class-1"),
        school=TimebackSourcedIdReference(sourcedId="school-1"),
        category=TimebackSourcedIdReference(sourcedId="category-1"),
        description="First quiz of the semester",
        resultValueMin=0.0,
        resultValueMax=100.0,
    )
    req = TimebackCreateLineItemRequest(lineItem=body)
    response = client.oneroster.gradebook.create_line_item(req)
    print(f"Created line item: {response.sourcedIdPairs.suppliedSourcedId} -> {response.sourcedIdPairs.allocatedSourcedId}")

    # Line item creation with all fields
    body_with_all_fields = TimebackCreateLineItemBody(
        sourcedId="test-line-item-002",
        title="Math Quiz 2",
        assignDate="2024-01-22T00:00:00Z",
        dueDate="2024-01-27T23:59:59Z",
        class_=TimebackSourcedIdReference(sourcedId="class-1"),
        school=TimebackSourcedIdReference(sourcedId="school-1"),
        category=TimebackSourcedIdReference(sourcedId="category-1"),
        status=TimebackStatus.ACTIVE,
        description="Second quiz of the semester",
        scoreScale=TimebackSourcedIdReference(sourcedId="scale-1"),
        resultValueMin=0.0,
        resultValueMax=100.0,
        metadata={"semester": "Spring 2024"},
    )
    req_with_all_fields = TimebackCreateLineItemRequest(lineItem=body_with_all_fields)
    response_with_all_fields = client.oneroster.gradebook.create_line_item(req_with_all_fields)
    print(f"Created line item with all fields: {response_with_all_fields.sourcedIdPairs.suppliedSourcedId} -> {response_with_all_fields.sourcedIdPairs.allocatedSourcedId}")


if __name__ == "__main__":
    main()

