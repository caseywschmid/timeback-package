from timeback.services.oneroster.rostering.endpoints.get_students_for_class import get_students_for_class
from timeback.models.request import TimebackGetStudentsForClassRequest
from timeback.models.response import TimebackGetAllUsersResponse


class MockHttp:
    def __init__(self):
        self.last_path = None

    def get(self, path, params=None):
        self.last_path = path
        return {
            "users": [{"sourcedId": "student-001", "givenName": "Jane", "familyName": "Doe", "enabledUser": True, "roles": [], "agents": [], "userProfiles": []}],
            "totalCount": 1, "pageCount": 1, "pageNumber": 1, "offset": 0, "limit": 100,
        }


def test_get_students_for_class_success():
    mock_http = MockHttp()
    request = TimebackGetStudentsForClassRequest(class_sourced_id="class-001")
    resp = get_students_for_class(mock_http, request)
    assert isinstance(resp, TimebackGetAllUsersResponse)
    assert "/ims/oneroster/rostering/v1p2/classes/class-001/students" in mock_http.last_path

