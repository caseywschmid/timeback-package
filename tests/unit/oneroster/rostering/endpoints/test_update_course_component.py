from timeback.services.oneroster.rostering.endpoints.update_course_component import update_course_component
from timeback.models.request import TimebackUpdateCourseComponentRequest, TimebackUpdateCourseComponentBody
from timeback.models.response import TimebackUpdateCourseComponentResponse


class MockHttp:
    def put(self, path, json=None):
        return {
            "courseComponent": {
                "sourcedId": "cc-001",
                "status": "active",
                "title": "Unit 2",
                "course": {"sourcedId": "course-001"},
                "dateLastModified": "2024-01-02T00:00:00Z",
            }
        }


def test_update_course_component_success():
    mock_http = MockHttp()
    body = TimebackUpdateCourseComponentBody(title="Unit 2")
    request = TimebackUpdateCourseComponentRequest(sourced_id="cc-001", courseComponent=body)
    resp = update_course_component(mock_http, request)
    assert isinstance(resp, TimebackUpdateCourseComponentResponse)
    assert resp.courseComponent.title == "Unit 2"

