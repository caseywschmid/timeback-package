from timeback.services.oneroster.rostering.endpoints.get_course_component import get_course_component
from timeback.models.request import TimebackGetCourseComponentRequest
from timeback.models.response import TimebackGetCourseComponentResponse


class MockHttp:
    def get(self, path, params=None):
        return {
            "courseComponent": {
                "sourcedId": "cc-001",
                "status": "active",
                "title": "Unit 1",
                "course": {"sourcedId": "course-001"},
                "dateLastModified": "2024-01-01T00:00:00Z",
            }
        }


def test_get_course_component_success():
    mock_http = MockHttp()
    request = TimebackGetCourseComponentRequest(sourced_id="cc-001")
    resp = get_course_component(mock_http, request)
    assert isinstance(resp, TimebackGetCourseComponentResponse)
    assert resp.courseComponent.sourcedId == "cc-001"

