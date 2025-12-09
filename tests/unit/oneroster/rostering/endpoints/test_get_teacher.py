from timeback.services.oneroster.rostering.endpoints.get_teacher import get_teacher
from timeback.models.request import TimebackGetTeacherRequest
from timeback.models.response import TimebackGetUserResponse


class MockHttp:
    def get(self, path, params=None):
        return {"user": {"sourcedId": "teacher-001", "givenName": "John", "familyName": "Doe", "enabledUser": True, "roles": [], "agents": [], "userProfiles": []}}


def test_get_teacher_success():
    mock_http = MockHttp()
    request = TimebackGetTeacherRequest(sourced_id="teacher-001")
    resp = get_teacher(mock_http, request)
    assert isinstance(resp, TimebackGetUserResponse)
    assert resp.user.sourcedId == "teacher-001"

