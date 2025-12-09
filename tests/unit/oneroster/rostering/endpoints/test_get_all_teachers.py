from timeback.services.oneroster.rostering.endpoints.get_all_teachers import get_all_teachers
from timeback.models.request import TimebackGetAllTeachersRequest
from timeback.models.response import TimebackGetAllUsersResponse


class MockHttp:
    def get(self, path, params=None):
        return {
            "users": [{"sourcedId": "teacher-001", "givenName": "John", "familyName": "Doe", "enabledUser": True, "roles": [], "agents": [], "userProfiles": []}],
            "totalCount": 1, "pageCount": 1, "pageNumber": 1, "offset": 0, "limit": 100,
        }


def test_get_all_teachers_success():
    mock_http = MockHttp()
    request = TimebackGetAllTeachersRequest()
    resp = get_all_teachers(mock_http, request)
    assert isinstance(resp, TimebackGetAllUsersResponse)
    assert len(resp.users) == 1

