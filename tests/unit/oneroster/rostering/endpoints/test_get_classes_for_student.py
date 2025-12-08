from timeback.services.oneroster.rostering.endpoints.get_classes_for_student import get_classes_for_student
from timeback.models.request import TimebackGetClassesForStudentRequest
from timeback.models.response import TimebackGetAllClassesResponse


class MockHttp:
    def __init__(self):
        self.last_path = None

    def get(self, path, params=None):
        self.last_path = path
        return {
            "classes": [{"sourcedId": "class-001", "title": "Math 101", "status": "active", "course": {"sourcedId": "course-001"}, "org": {"sourcedId": "org-001"}, "terms": [{"sourcedId": "term-001"}]}],
            "totalCount": 1, "pageCount": 1, "pageNumber": 1, "offset": 0, "limit": 100,
        }


def test_get_classes_for_student_success():
    mock_http = MockHttp()
    request = TimebackGetClassesForStudentRequest(student_sourced_id="student-001")
    resp = get_classes_for_student(mock_http, request)
    assert isinstance(resp, TimebackGetAllClassesResponse)
    assert "/ims/oneroster/rostering/v1p2/students/student-001/classes" in mock_http.last_path

