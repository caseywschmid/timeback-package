from timeback.services.oneroster.resources.endpoints.get_resources_for_course import get_resources_for_course
from timeback.models.request import TimebackGetResourcesForCourseRequest
from timeback.models.response import TimebackGetAllResourcesResponse


class MockHttp:
    def __init__(self):
        self.last_path = None

    def get(self, path, params=None):
        self.last_path = path
        return {
            "resources": [
                {
                    "sourcedId": "res-001",
                    "status": "active",
                    "dateLastModified": "2024-01-15T12:00:00Z",
                    "title": "Course Resource",
                    "vendorResourceId": "vendor-123",
                    "importance": "primary",
                }
            ],
            "totalCount": 1,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }


def test_get_resources_for_course_success():
    """Test successful retrieval of resources for a course."""
    mock_http = MockHttp()
    request = TimebackGetResourcesForCourseRequest(course_sourced_id="course-001")
    resp = get_resources_for_course(mock_http, request)

    assert isinstance(resp, TimebackGetAllResourcesResponse)
    assert len(resp.resources) == 1
    assert "/ims/oneroster/resources/v1p2/courses/course-001/resources" in mock_http.last_path

