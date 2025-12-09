from timeback.services.oneroster.rostering.endpoints.create_school import create_school
from timeback.models.request import (
    TimebackCreateSchoolRequest,
    TimebackCreateSchoolBody,
)
from timeback.models.response import TimebackCreateSchoolResponse
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackOrgType, TimebackStatus


class MockHttp:
    def post(self, path, json=None):
        assert path == "/ims/oneroster/rostering/v1p2/schools"
        # Simulate 201 response body with sourcedIdPairs
        return {
            "sourcedIdPairs": {
                "suppliedSourcedId": json["org"].get("sourcedId", "temp-id"),
                "allocatedSourcedId": "allocated-school-123",
            }
        }


def test_create_school_success():
    body = TimebackCreateSchoolBody(
        sourcedId="school-created",
        name="Test Elementary School",
        type=TimebackOrgType.SCHOOL,
    )
    req = TimebackCreateSchoolRequest(org=body)
    resp = create_school(MockHttp(), req)
    assert isinstance(resp, TimebackCreateSchoolResponse)
    assert resp.sourcedIdPairs.allocatedSourcedId == "allocated-school-123"
    assert resp.sourcedIdPairs.suppliedSourcedId == "school-created"


def test_create_school_with_parent():
    parent = TimebackSourcedIdReference(sourcedId="district-123")
    body = TimebackCreateSchoolBody(
        sourcedId="school-with-parent",
        name="Test Middle School",
        type=TimebackOrgType.SCHOOL,
        parent=parent,
    )
    req = TimebackCreateSchoolRequest(org=body)
    resp = create_school(MockHttp(), req)
    assert isinstance(resp, TimebackCreateSchoolResponse)
    assert resp.sourcedIdPairs.allocatedSourcedId == "allocated-school-123"


def test_create_school_with_all_fields():
    parent = TimebackSourcedIdReference(sourcedId="district-456")
    body = TimebackCreateSchoolBody(
        sourcedId="school-full",
        name="Test High School",
        type=TimebackOrgType.SCHOOL,
        status=TimebackStatus.ACTIVE,
        identifier="HS001",
        metadata={"custom": "value"},
        parent=parent,
    )
    req = TimebackCreateSchoolRequest(org=body)
    resp = create_school(MockHttp(), req)
    assert isinstance(resp, TimebackCreateSchoolResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "school-full"

