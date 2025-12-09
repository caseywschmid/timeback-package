from timeback.services.oneroster.rostering.endpoints.delete_course_component import delete_course_component


class MockHttp:
    def __init__(self):
        self.last_path = None

    def delete(self, path):
        self.last_path = path
        return None


def test_delete_course_component_success():
    mock_http = MockHttp()
    result = delete_course_component(mock_http, "cc-001")
    assert result is None
    assert "/ims/oneroster/rostering/v1p2/courses/components/cc-001" in mock_http.last_path

