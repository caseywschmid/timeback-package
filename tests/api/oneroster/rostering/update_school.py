from timeback import Timeback
from timeback.models.request import (
    TimebackUpdateSchoolRequest,
    TimebackUpdateSchoolBody,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackOrgType, TimebackStatus


def main():
    client = Timeback()
    sourced_id = "test-school-001"  # Replace with actual school sourcedId

    # Basic school update
    body = TimebackUpdateSchoolBody(
        sourcedId=sourced_id,
        name="Updated School Name",
        type=TimebackOrgType.SCHOOL,
        status=TimebackStatus.ACTIVE,
    )
    req = TimebackUpdateSchoolRequest(org=body)
    response = client.oneroster.rostering.update_school(req)
    print(f"Updated school: {response.org.sourcedId}, {response.org.name}")

    # School update with parent organization
    parent = TimebackSourcedIdReference(sourcedId="district-123")
    body_with_parent = TimebackUpdateSchoolBody(
        sourcedId=sourced_id,
        name="School with Parent",
        type=TimebackOrgType.SCHOOL,
        parent=parent,
    )
    req_with_parent = TimebackUpdateSchoolRequest(org=body_with_parent)
    response_with_parent = client.oneroster.rostering.update_school(req_with_parent)
    print(f"Updated school with parent: {response_with_parent.org.sourcedId}, {response_with_parent.org.name}")


if __name__ == "__main__":
    main()

