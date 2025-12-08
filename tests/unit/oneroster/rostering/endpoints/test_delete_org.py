from timeback.services.oneroster.rostering.endpoints.delete_org import delete_org


class MockHttp:
    def __init__(self):
        self.last_path = None

    def delete(self, path):
        self.last_path = path
        return None


def test_delete_org_success():
    mock_http = MockHttp()
    result = delete_org(mock_http, "org-001")
    assert result is None
    assert "/ims/oneroster/rostering/v1p2/orgs/org-001" in mock_http.last_path

