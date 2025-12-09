from timeback.services.oneroster.rostering.endpoints.get_all_course_components import get_all_course_components
from timeback.models.request import TimebackGetAllCourseComponentsRequest
from timeback.models.response import TimebackGetAllCourseComponentsResponse


class MockHttp:
    def get(self, path, params=None):
        return {
            "courseComponents": [
                {
                    "sourcedId": "cc-001",
                    "status": "active",
                    "title": "Unit 1",
                    "course": {"sourcedId": "course-001"},
                    "dateLastModified": "2024-01-01T00:00:00Z",
                }
            ],
            "totalCount": 1, "pageCount": 1, "pageNumber": 1, "offset": 0, "limit": 100,
        }


def test_get_all_course_components_success():
    mock_http = MockHttp()
    request = TimebackGetAllCourseComponentsRequest()
    resp = get_all_course_components(mock_http, request)
    assert isinstance(resp, TimebackGetAllCourseComponentsResponse)
    assert len(resp.courseComponents) == 1
    assert resp.courseComponents[0].sourcedId == "cc-001"

