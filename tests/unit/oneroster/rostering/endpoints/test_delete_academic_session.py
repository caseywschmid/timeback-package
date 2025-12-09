from timeback.services.oneroster.rostering.endpoints.delete_academic_session import delete_academic_session


class MockHttp:
    def __init__(self):
        self.last_path = None

    def delete(self, path):
        self.last_path = path
        return None


def test_delete_academic_session_success():
    mock_http = MockHttp()
    result = delete_academic_session(mock_http, "as-001")
    assert result is None
    assert "/ims/oneroster/rostering/v1p2/academicSessions/as-001" in mock_http.last_path

