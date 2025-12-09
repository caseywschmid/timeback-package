from timeback import Timeback
from timeback.models.request import (
    TimebackCreateSchoolRequest,
    TimebackCreateSchoolBody,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackOrgType, TimebackStatus


def main():
    client = Timeback()

    # Basic school creation
    body = TimebackCreateSchoolBody(
        sourcedId="test-school-001",
        name="Test Elementary School",
        type=TimebackOrgType.SCHOOL,
    )
    req = TimebackCreateSchoolRequest(org=body)
    response = client.oneroster.rostering.create_school(req)
    print(f"Created school: {response.sourcedIdPairs.suppliedSourcedId} -> {response.sourcedIdPairs.allocatedSourcedId}")

    # School creation with parent organization
    parent = TimebackSourcedIdReference(sourcedId="district-123")
    body_with_parent = TimebackCreateSchoolBody(
        sourcedId="test-school-002",
        name="Test Middle School",
        type=TimebackOrgType.SCHOOL,
        status=TimebackStatus.ACTIVE,
        identifier="MS001",
        parent=parent,
    )
    req_with_parent = TimebackCreateSchoolRequest(org=body_with_parent)
    response_with_parent = client.oneroster.rostering.create_school(req_with_parent)
    print(f"Created school with parent: {response_with_parent.sourcedIdPairs.suppliedSourcedId} -> {response_with_parent.sourcedIdPairs.allocatedSourcedId}")


if __name__ == "__main__":
    main()

