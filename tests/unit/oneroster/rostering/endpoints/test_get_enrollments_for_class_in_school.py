from timeback.services.oneroster.rostering.endpoints.get_enrollments_for_class_in_school import get_enrollments_for_class_in_school
from timeback.models.request import TimebackGetEnrollmentsForClassInSchoolRequest
from timeback.models.response import TimebackGetAllEnrollmentsResponse


class MockHttp:
    def __init__(self):
        self.last_path = None

    def get(self, path, params=None):
        self.last_path = path
        return {
            "enrollments": [
                {
                    "sourcedId": "enroll-001",
                    "role": "student",
                    "user": {"sourcedId": "user-001"},
                    "class": {"sourcedId": "class-001"},
                }
            ],
            "totalCount": 1, "pageCount": 1, "pageNumber": 1, "offset": 0, "limit": 100,
        }


def test_get_enrollments_for_class_in_school_success():
    mock_http = MockHttp()
    request = TimebackGetEnrollmentsForClassInSchoolRequest(
        school_sourced_id="school-001",
        class_sourced_id="class-001"
    )
    resp = get_enrollments_for_class_in_school(mock_http, request)
    assert isinstance(resp, TimebackGetAllEnrollmentsResponse)
    assert len(resp.enrollments) == 1
    assert "/ims/oneroster/rostering/v1p2/schools/school-001/classes/class-001/enrollments" in mock_http.last_path

