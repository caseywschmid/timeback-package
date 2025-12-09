from timeback.services.oneroster.rostering.endpoints.update_class import update_class
from timeback.models.request.timeback_update_class_request import (
    TimebackUpdateClassRequest,
    TimebackUpdateClassBody,
)
from timeback.models.response import TimebackUpdateClassResponse
from timeback.enums import TimebackStatus, TimebackClassType
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.errors import NotFoundError


class MockHttp:
    def put(self, path, json=None):
        assert "/ims/oneroster/rostering/v1p2/classes/class1" in path
        # Echo back a realistic class wrapper
        class_data = json["class"].copy()
        class_data.setdefault("sourcedId", "class1")
        class_data.setdefault("status", TimebackStatus.ACTIVE.value)
        class_data.setdefault("dateLastModified", "2024-01-01T00:00:00Z")
        class_data.setdefault("title", "Updated Class")
        class_data.setdefault("course", {"sourcedId": "course1"})
        class_data.setdefault("org", {"sourcedId": "school1", "type": "org"})
        class_data.setdefault("terms", [{"sourcedId": "term1"}])
        return {"class": class_data}


def test_update_class_success():
    """Test successful class update."""
    body = TimebackUpdateClassBody(
        sourcedId="class1",
        title="Updated Class Title",
        status=TimebackStatus.ACTIVE,
    )
    req = TimebackUpdateClassRequest(class_=body)
    resp = update_class(MockHttp(), req)
    assert isinstance(resp, TimebackUpdateClassResponse)
    assert resp.class_.sourcedId == "class1"
    assert resp.class_.title == "Updated Class Title"
    assert resp.class_.status == TimebackStatus.ACTIVE


def test_update_class_with_optional_fields():
    """Test class update with optional fields."""
    body = TimebackUpdateClassBody(
        sourcedId="class1",
        title="Class with Options",
        classType=TimebackClassType.SCHEDULED,
        classCode="MATH-101-A",
        location="Room 101",
        grades=["9", "10"],
        subjects=["Math"],
    )
    req = TimebackUpdateClassRequest(class_=body)
    resp = update_class(MockHttp(), req)
    assert isinstance(resp, TimebackUpdateClassResponse)
    assert resp.class_.sourcedId == "class1"
    assert resp.class_.classType == TimebackClassType.SCHEDULED
    assert resp.class_.classCode == "MATH-101-A"
    assert resp.class_.location == "Room 101"
    assert resp.class_.grades == ["9", "10"]
    assert resp.class_.subjects == ["Math"]


def test_update_class_with_resources_and_terms():
    """Test class update with resources and terms references."""
    body = TimebackUpdateClassBody(
        sourcedId="class1",
        resources=[
            TimebackSourcedIdReference(sourcedId="resource1"),
            TimebackSourcedIdReference(sourcedId="resource2"),
        ],
        terms=[
            TimebackSourcedIdReference(sourcedId="term1"),
            TimebackSourcedIdReference(sourcedId="term2"),
        ],
    )
    req = TimebackUpdateClassRequest(class_=body)
    resp = update_class(MockHttp(), req)
    assert isinstance(resp, TimebackUpdateClassResponse)
    assert resp.class_.sourcedId == "class1"
    # Resources and terms should be in the response
    assert len(resp.class_.terms) >= 1


def test_update_class_not_found_raises():
    """Test that NotFoundError is propagated when class doesn't exist."""
    class MockHttpNotFound:
        def put(self, path, json=None):
            raise NotFoundError("Resource not found (status=404)")

    body = TimebackUpdateClassBody(
        sourcedId="missing-id",
        title="Missing Class",
    )
    req = TimebackUpdateClassRequest(class_=body)

    try:
        update_class(MockHttpNotFound(), req)
        assert False, "Expected NotFoundError"
    except NotFoundError:
        pass

