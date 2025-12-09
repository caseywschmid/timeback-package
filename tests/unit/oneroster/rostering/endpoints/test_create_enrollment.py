from timeback.services.oneroster.rostering.endpoints.create_enrollment import create_enrollment
from timeback.models.request import TimebackCreateEnrollmentRequest, TimebackCreateEnrollmentBody
from timeback.models.response import TimebackCreateEnrollmentResponse
from timeback.enums import TimebackEnrollmentRole
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class MockHttp:
    def __init__(self):
        self.last_json = None

    def post(self, path, json=None):
        self.last_json = json
        return {"sourcedIdPairs": {"suppliedSourcedId": json["enrollment"]["sourcedId"], "allocatedSourcedId": "alloc-001"}}


def test_create_enrollment_success():
    mock_http = MockHttp()
    body = TimebackCreateEnrollmentBody(
        sourcedId="new-enroll",
        role=TimebackEnrollmentRole.STUDENT,
        user=TimebackSourcedIdReference(sourcedId="user-001"),
        class_=TimebackSourcedIdReference(sourcedId="class-001"),
    )
    request = TimebackCreateEnrollmentRequest(enrollment=body)
    resp = create_enrollment(mock_http, request)
    assert isinstance(resp, TimebackCreateEnrollmentResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "new-enroll"
    # Verify the body includes "class" not "class_"
    assert "class" in mock_http.last_json["enrollment"]

