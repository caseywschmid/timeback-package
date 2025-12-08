from timeback.services.oneroster.rostering.endpoints.get_teachers_for_class_in_school import get_teachers_for_class_in_school
from timeback.models.request import TimebackGetTeachersForClassInSchoolRequest
from timeback.models.response import TimebackGetAllUsersResponse


class MockHttp:
    def __init__(self):
        self.last_path = None

    def get(self, path, params=None):
        self.last_path = path
        return {
            "users": [
                {
                    "sourcedId": "teacher-001",
                    "givenName": "John",
                    "familyName": "Doe",
                    "enabledUser": True,
                    "roles": [],
                    "agents": [],
                    "userProfiles": [],
                }
            ],
            "totalCount": 1,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }


def test_get_teachers_for_class_in_school_success():
    """Test successful retrieval of teachers for a class in a school."""
    mock_http = MockHttp()
    request = TimebackGetTeachersForClassInSchoolRequest(
        school_sourced_id="school-001",
        class_sourced_id="class-001"
    )
    resp = get_teachers_for_class_in_school(mock_http, request)

    assert isinstance(resp, TimebackGetAllUsersResponse)
    assert len(resp.users) == 1
    assert "/ims/oneroster/rostering/v1p2/schools/school-001/classes/class-001/teachers" in mock_http.last_path

