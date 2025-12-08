from timeback.services.oneroster.rostering.endpoints.delete_demographic import delete_demographic


class MockHttp:
    def __init__(self):
        self.last_path = None

    def delete(self, path):
        self.last_path = path
        return None


def test_delete_demographic_success():
    mock_http = MockHttp()
    result = delete_demographic(mock_http, "demo-001")
    assert result is None
    assert "/ims/oneroster/rostering/v1p2/demographics/demo-001" in mock_http.last_path

