from timeback.services.oneroster.rostering.endpoints.create_class import create_class
from timeback.models.request import (
    TimebackCreateClassRequest,
    TimebackCreateClassBody,
)
from timeback.models.response import TimebackCreateClassResponse
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus, TimebackClassType


class MockHttp:
    def post(self, path, json=None):
        assert path == "/ims/oneroster/rostering/v1p2/classes"
        # Simulate 201 response body with sourcedIdPairs
        return {
            "sourcedIdPairs": {
                "suppliedSourcedId": json["class"].get("sourcedId", "temp-id"),
                "allocatedSourcedId": "allocated-class-123",
            }
        }


def test_create_class_success():
    course_ref = TimebackSourcedIdReference(sourcedId="course-123")
    org_ref = TimebackSourcedIdReference(sourcedId="org-123")
    term_ref = TimebackSourcedIdReference(sourcedId="term-123")
    
    body = TimebackCreateClassBody(
        sourcedId="class-created",
        title="Math 101",
        course=course_ref,
        org=org_ref,
        terms=[term_ref],
    )
    req = TimebackCreateClassRequest(class_=body)
    resp = create_class(MockHttp(), req)
    assert isinstance(resp, TimebackCreateClassResponse)
    assert resp.sourcedIdPairs.allocatedSourcedId == "allocated-class-123"
    assert resp.sourcedIdPairs.suppliedSourcedId == "class-created"


def test_create_class_with_optional_fields():
    course_ref = TimebackSourcedIdReference(sourcedId="course-456")
    org_ref = TimebackSourcedIdReference(sourcedId="org-456")
    term_ref = TimebackSourcedIdReference(sourcedId="term-456")
    
    body = TimebackCreateClassBody(
        sourcedId="class-with-options",
        title="Science Lab",
        course=course_ref,
        org=org_ref,
        terms=[term_ref],
        classCode="SCI-101",
        classType=TimebackClassType.SCHEDULED,
        location="Room 205",
        status=TimebackStatus.ACTIVE,
    )
    req = TimebackCreateClassRequest(class_=body)
    resp = create_class(MockHttp(), req)
    assert isinstance(resp, TimebackCreateClassResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "class-with-options"


def test_create_class_with_all_fields():
    course_ref = TimebackSourcedIdReference(sourcedId="course-789")
    org_ref = TimebackSourcedIdReference(sourcedId="org-789")
    term_ref1 = TimebackSourcedIdReference(sourcedId="term-789")
    term_ref2 = TimebackSourcedIdReference(sourcedId="term-790")
    resource_ref = TimebackSourcedIdReference(sourcedId="resource-123")
    
    body = TimebackCreateClassBody(
        sourcedId="class-full",
        title="Advanced Mathematics",
        course=course_ref,
        org=org_ref,
        terms=[term_ref1, term_ref2],
        classCode="MATH-301",
        classType=TimebackClassType.SCHEDULED,
        location="Building A, Room 301",
        status=TimebackStatus.ACTIVE,
        grades=["11", "12"],
        subjects=["Math"],
        subjectCodes=["MATH"],
        periods=["Period 1", "Period 2"],
        resources=[resource_ref],
        metadata={"custom": "value"},
    )
    req = TimebackCreateClassRequest(class_=body)
    resp = create_class(MockHttp(), req)
    assert isinstance(resp, TimebackCreateClassResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "class-full"

