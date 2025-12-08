from timeback.services.oneroster.rostering.endpoints.get_teachers_for_school import get_teachers_for_school
from timeback.models.request import TimebackGetTeachersForSchoolRequest
from timeback.models.response import TimebackGetAllUsersResponse


class MockHttp:
    def __init__(self):
        self.last_path = None

    def get(self, path, params=None):
        self.last_path = path
        return {
            "users": [{"sourcedId": "teacher-001", "givenName": "John", "familyName": "Doe", "enabledUser": True, "roles": [], "agents": [], "userProfiles": []}],
            "totalCount": 1, "pageCount": 1, "pageNumber": 1, "offset": 0, "limit": 100,
        }


def test_get_teachers_for_school_success():
    mock_http = MockHttp()
    request = TimebackGetTeachersForSchoolRequest(school_sourced_id="school-001")
    resp = get_teachers_for_school(mock_http, request)
    assert isinstance(resp, TimebackGetAllUsersResponse)
    assert "/ims/oneroster/rostering/v1p2/schools/school-001/teachers" in mock_http.last_path

