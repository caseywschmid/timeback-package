from timeback.services.oneroster.rostering.endpoints.get_courses_for_school import get_courses_for_school
from timeback.models.request import TimebackGetCoursesForSchoolRequest
from timeback.models.response import TimebackGetAllCoursesResponse


class MockHttp:
    def get(self, path, params=None):
        return {
            "courses": [
                {
                    "sourcedId": "course-001",
                    "status": "active",
                    "title": "Math 101",
                    "courseCode": "M101",
                    "dateLastModified": "2024-01-01T00:00:00Z",
                    "orgSourcedId": "org-001",
                }
            ],
            "totalCount": 1, "pageCount": 1, "pageNumber": 1, "offset": 0, "limit": 100,
        }


def test_get_courses_for_school_success():
    mock_http = MockHttp()
    request = TimebackGetCoursesForSchoolRequest(school_sourced_id="school-001")
    resp = get_courses_for_school(mock_http, request)
    assert isinstance(resp, TimebackGetAllCoursesResponse)
    assert len(resp.courses) == 1
    assert resp.courses[0].sourcedId == "course-001"

