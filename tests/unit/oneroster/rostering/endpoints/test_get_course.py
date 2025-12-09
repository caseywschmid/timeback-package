from timeback.services.oneroster.rostering.endpoints.get_course import get_course
from timeback.models.request import TimebackGetCourseRequest
from timeback.models.response import TimebackGetCourseResponse


class MockHttp:
    def get(self, path, params=None):
        return {
            "course": {"sourcedId": "course-001", "title": "Math 101", "orgSourcedId": "org-001"}
        }


def test_get_course_success():
    mock_http = MockHttp()
    request = TimebackGetCourseRequest(sourced_id="course-001")
    resp = get_course(mock_http, request)
    assert isinstance(resp, TimebackGetCourseResponse)
    assert resp.course.sourcedId == "course-001"

