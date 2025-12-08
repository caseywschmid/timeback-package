from timeback.services.oneroster.rostering.endpoints.get_student import get_student
from timeback.models.request import TimebackGetStudentRequest
from timeback.models.response import TimebackGetUserResponse


class MockHttp:
    def get(self, path, params=None):
        return {"user": {"sourcedId": "student-001", "givenName": "Jane", "familyName": "Doe", "enabledUser": True, "roles": [], "agents": [], "userProfiles": []}}


def test_get_student_success():
    mock_http = MockHttp()
    request = TimebackGetStudentRequest(sourced_id="student-001")
    resp = get_student(mock_http, request)
    assert isinstance(resp, TimebackGetUserResponse)
    assert resp.user.sourcedId == "student-001"

