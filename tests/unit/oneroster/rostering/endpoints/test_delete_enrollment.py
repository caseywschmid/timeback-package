from timeback.services.oneroster.rostering.endpoints.delete_enrollment import delete_enrollment


class MockHttp:
    def __init__(self):
        self.last_path = None

    def delete(self, path):
        self.last_path = path
        return None


def test_delete_enrollment_success():
    mock_http = MockHttp()
    result = delete_enrollment(mock_http, "enroll-001")
    assert result is None
    assert "/ims/oneroster/rostering/v1p2/enrollments/enroll-001" in mock_http.last_path

