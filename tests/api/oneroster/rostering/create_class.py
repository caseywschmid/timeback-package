from timeback import Timeback
from timeback.models.request import (
    TimebackCreateClassRequest,
    TimebackCreateClassBody,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus, TimebackClassType


def main():
    client = Timeback()

    # Example 1: Create a class with minimal required fields
    course_ref = TimebackSourcedIdReference(sourcedId="course-123")
    org_ref = TimebackSourcedIdReference(sourcedId="org-123")
    term_ref = TimebackSourcedIdReference(sourcedId="term-123")

    body = TimebackCreateClassBody(
        title="Math 101",
        course=course_ref,
        org=org_ref,
        terms=[term_ref],
    )
    request = TimebackCreateClassRequest(class_=body)
    response = client.oneroster.rostering.create_class(request)

    print(f"Created class:")
    print(f"  Supplied SourcedId: {response.sourcedIdPairs.suppliedSourcedId}")
    print(f"  Allocated SourcedId: {response.sourcedIdPairs.allocatedSourcedId}")

    # Example 2: Create a class with all optional fields
    course_ref2 = TimebackSourcedIdReference(sourcedId="course-456")
    org_ref2 = TimebackSourcedIdReference(sourcedId="org-456")
    term_ref2 = TimebackSourcedIdReference(sourcedId="term-456")
    resource_ref = TimebackSourcedIdReference(sourcedId="resource-123")

    body_full = TimebackCreateClassBody(
        sourcedId="my-custom-class-id",
        title="Advanced Mathematics",
        course=course_ref2,
        org=org_ref2,
        terms=[term_ref2],
        classCode="MATH-301",
        classType=TimebackClassType.SCHEDULED,
        location="Building A, Room 301",
        status=TimebackStatus.ACTIVE,
        grades=["11", "12"],
        subjects=["Math"],
        subjectCodes=["MATH"],
        periods=["Period 1"],
        resources=[resource_ref],
        metadata={"custom": "value"},
    )
    request_full = TimebackCreateClassRequest(class_=body_full)
    response_full = client.oneroster.rostering.create_class(request_full)

    print(f"\nCreated class with all fields:")
    print(f"  Supplied SourcedId: {response_full.sourcedIdPairs.suppliedSourcedId}")
    print(f"  Allocated SourcedId: {response_full.sourcedIdPairs.allocatedSourcedId}")


if __name__ == "__main__":
    main()

