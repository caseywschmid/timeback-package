from timeback.services.oneroster.rostering.endpoints.update_component_resource import update_component_resource
from timeback.models.request import TimebackUpdateComponentResourceRequest, TimebackUpdateComponentResourceBody
from timeback.models.response import TimebackUpdateComponentResourceResponse


class MockHttp:
    def put(self, path, json=None):
        return {
            "componentResource": {
                "sourcedId": "cr-001",
                "title": "Lesson 2",
                "courseComponent": {"href": "/components/comp-001", "sourcedId": "comp-001", "type": "courseComponent"},
                "resource": {"href": "/resources/res-001", "sourcedId": "res-001", "type": "resource"},
            }
        }


def test_update_component_resource_success():
    mock_http = MockHttp()
    body = TimebackUpdateComponentResourceBody(title="Lesson 2")
    request = TimebackUpdateComponentResourceRequest(sourced_id="cr-001", componentResource=body)
    resp = update_component_resource(mock_http, request)
    assert isinstance(resp, TimebackUpdateComponentResourceResponse)
    assert resp.componentResource.title == "Lesson 2"

