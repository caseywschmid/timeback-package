from timeback.services.oneroster.rostering.endpoints.delete_course import delete_course


class MockHttp:
    def __init__(self):
        self.last_path = None

    def delete(self, path):
        self.last_path = path
        return None


def test_delete_course_success():
    mock_http = MockHttp()
    result = delete_course(mock_http, "course-001")
    assert result is None
    assert "/ims/oneroster/rostering/v1p2/courses/course-001" in mock_http.last_path

