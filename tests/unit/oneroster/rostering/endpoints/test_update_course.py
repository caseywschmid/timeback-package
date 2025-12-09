from timeback.services.oneroster.rostering.endpoints.update_course import update_course
from timeback.models.request import TimebackUpdateCourseRequest, TimebackUpdateCourseBody
from timeback.models.response import TimebackUpdateCourseResponse


class MockHttp:
    def put(self, path, json=None):
        return {
            "course": {"sourcedId": "course-001", "title": "Math 102", "orgSourcedId": "org-001"}
        }


def test_update_course_success():
    mock_http = MockHttp()
    body = TimebackUpdateCourseBody(title="Math 102")
    request = TimebackUpdateCourseRequest(sourced_id="course-001", course=body)
    resp = update_course(mock_http, request)
    assert isinstance(resp, TimebackUpdateCourseResponse)
    assert resp.course.title == "Math 102"

