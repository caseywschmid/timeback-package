from timeback.services.oneroster.rostering.endpoints.get_all_students import get_all_students
from timeback.models.request import TimebackGetAllStudentsRequest
from timeback.models.response import TimebackGetAllUsersResponse


class MockHttp:
    def get(self, path, params=None):
        return {
            "users": [{"sourcedId": "student-001", "givenName": "Jane", "familyName": "Doe", "enabledUser": True, "roles": [], "agents": [], "userProfiles": []}],
            "totalCount": 1, "pageCount": 1, "pageNumber": 1, "offset": 0, "limit": 100,
        }


def test_get_all_students_success():
    mock_http = MockHttp()
    request = TimebackGetAllStudentsRequest()
    resp = get_all_students(mock_http, request)
    assert isinstance(resp, TimebackGetAllUsersResponse)
    assert len(resp.users) == 1

