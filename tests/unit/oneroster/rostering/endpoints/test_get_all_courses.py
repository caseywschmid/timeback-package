from timeback.services.oneroster.rostering.endpoints.get_all_courses import get_all_courses
from timeback.models.request import TimebackGetAllCoursesRequest
from timeback.models.response import TimebackGetAllCoursesResponse


class MockHttp:
    def get(self, path, params=None):
        return {
            "courses": [
                {"sourcedId": "course-001", "title": "Math 101", "orgSourcedId": "org-001"}
            ],
            "totalCount": 1, "pageCount": 1, "pageNumber": 1, "offset": 0, "limit": 100,
        }


def test_get_all_courses_success():
    mock_http = MockHttp()
    request = TimebackGetAllCoursesRequest()
    resp = get_all_courses(mock_http, request)
    assert isinstance(resp, TimebackGetAllCoursesResponse)
    assert len(resp.courses) == 1
    assert resp.courses[0].sourcedId == "course-001"

