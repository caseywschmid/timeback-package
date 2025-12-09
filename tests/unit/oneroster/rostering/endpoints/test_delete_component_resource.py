from timeback.services.oneroster.rostering.endpoints.delete_component_resource import delete_component_resource


class MockHttp:
    def __init__(self):
        self.last_path = None

    def delete(self, path):
        self.last_path = path
        return None


def test_delete_component_resource_success():
    mock_http = MockHttp()
    result = delete_component_resource(mock_http, "cr-001")
    assert result is None
    assert "/ims/oneroster/rostering/v1p2/courses/component-resources/cr-001" in mock_http.last_path

