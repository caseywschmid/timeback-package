from timeback.services.oneroster.rostering.endpoints.update_school import update_school
from timeback.models.request.timeback_update_school_request import (
    TimebackUpdateSchoolRequest,
    TimebackUpdateSchoolBody,
)
from timeback.models.response import TimebackUpdateSchoolResponse
from timeback.enums import TimebackStatus, TimebackOrgType
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.errors import NotFoundError


class MockHttp:
    def put(self, path, json=None):
        assert "/ims/oneroster/rostering/v1p2/schools/school1" in path
        # Echo back a realistic school wrapper
        org = json["org"].copy()
        org.setdefault("sourcedId", "school1")
        org.setdefault("status", TimebackStatus.ACTIVE)
        org.setdefault("dateLastModified", "2024-01-01T00:00:00Z")
        return {"org": org}


def test_update_school_success():
    """Test successful school update."""
    body = TimebackUpdateSchoolBody(
        sourcedId="school1",
        name="Updated School Name",
        type=TimebackOrgType.SCHOOL,
        status=TimebackStatus.ACTIVE,
    )
    req = TimebackUpdateSchoolRequest(org=body)
    resp = update_school(MockHttp(), req)
    assert isinstance(resp, TimebackUpdateSchoolResponse)
    assert resp.org.sourcedId == "school1"
    assert resp.org.name == "Updated School Name"
    assert resp.org.type == TimebackOrgType.SCHOOL
    assert resp.org.status == TimebackStatus.ACTIVE


def test_update_school_with_parent():
    """Test school update with parent organization."""
    body = TimebackUpdateSchoolBody(
        sourcedId="school1",
        name="School with Parent",
        type=TimebackOrgType.SCHOOL,
        parent=TimebackSourcedIdReference(sourcedId="district1"),
    )
    req = TimebackUpdateSchoolRequest(org=body)
    resp = update_school(MockHttp(), req)
    assert isinstance(resp, TimebackUpdateSchoolResponse)
    assert resp.org.sourcedId == "school1"
    assert resp.org.parent is not None
    assert resp.org.parent.sourcedId == "district1"


def test_update_school_not_found_raises():
    """Test that NotFoundError is propagated when school doesn't exist."""
    class MockHttpNotFound:
        def put(self, path, json=None):
            raise NotFoundError("Resource not found (status=404)")

    body = TimebackUpdateSchoolBody(
        sourcedId="missing-id",
        name="Missing School",
        type=TimebackOrgType.SCHOOL,
    )
    req = TimebackUpdateSchoolRequest(org=body)

    try:
        update_school(MockHttpNotFound(), req)
        assert False, "Expected NotFoundError"
    except NotFoundError:
        pass

