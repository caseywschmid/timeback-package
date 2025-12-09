from timeback.services.oneroster.rostering.endpoints.get_component_resource import get_component_resource
from timeback.models.request import TimebackGetComponentResourceRequest
from timeback.models.response import TimebackGetComponentResourceResponse


class MockHttp:
    def get(self, path, params=None):
        return {
            "componentResource": {
                "sourcedId": "cr-001",
                "title": "Lesson 1",
                "courseComponent": {"href": "/components/comp-001", "sourcedId": "comp-001", "type": "courseComponent"},
                "resource": {"href": "/resources/res-001", "sourcedId": "res-001", "type": "resource"},
            }
        }


def test_get_component_resource_success():
    mock_http = MockHttp()
    request = TimebackGetComponentResourceRequest(sourced_id="cr-001")
    resp = get_component_resource(mock_http, request)
    assert isinstance(resp, TimebackGetComponentResourceResponse)
    assert resp.componentResource.sourcedId == "cr-001"

