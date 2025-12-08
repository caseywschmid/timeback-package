from timeback import Timeback
from timeback.models.request import (
    TimebackUpdateClassRequest,
    TimebackUpdateClassBody,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus, TimebackClassType


def main():
    client = Timeback()
    sourced_id = "test-class-001"  # Replace with actual class sourcedId

    # Basic class update
    body = TimebackUpdateClassBody(
        sourcedId=sourced_id,
        title="Updated Class Title",
        status=TimebackStatus.ACTIVE,
    )
    req = TimebackUpdateClassRequest(class_=body)
    response = client.oneroster.rostering.update_class(req)
    print(f"Updated class: {response.class_.sourcedId}, {response.class_.title}")

    # Class update with optional fields
    body_with_options = TimebackUpdateClassBody(
        sourcedId=sourced_id,
        title="Class with Options",
        classType=TimebackClassType.SCHEDULED,
        classCode="MATH-101-A",
        location="Room 101",
        grades=["9", "10"],
        subjects=["Math"],
    )
    req_with_options = TimebackUpdateClassRequest(class_=body_with_options)
    response_with_options = client.oneroster.rostering.update_class(req_with_options)
    print(f"Updated class with options: {response_with_options.class_.sourcedId}, {response_with_options.class_.classCode}")

    # Class update with terms and resources
    body_with_refs = TimebackUpdateClassBody(
        sourcedId=sourced_id,
        terms=[
            TimebackSourcedIdReference(sourcedId="term-001"),
            TimebackSourcedIdReference(sourcedId="term-002"),
        ],
        resources=[
            TimebackSourcedIdReference(sourcedId="resource-001"),
        ],
    )
    req_with_refs = TimebackUpdateClassRequest(class_=body_with_refs)
    response_with_refs = client.oneroster.rostering.update_class(req_with_refs)
    print(f"Updated class with refs: {response_with_refs.class_.sourcedId}")


if __name__ == "__main__":
    main()

