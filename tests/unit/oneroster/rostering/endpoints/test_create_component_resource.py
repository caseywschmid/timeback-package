from timeback.services.oneroster.rostering.endpoints.create_component_resource import create_component_resource
from timeback.models.request import TimebackCreateComponentResourceRequest, TimebackCreateComponentResourceBody
from timeback.models.response import TimebackCreateComponentResourceResponse
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class MockHttp:
    def __init__(self):
        self.last_json = None

    def post(self, path, json=None):
        self.last_json = json
        return {"sourcedIdPairs": {"suppliedSourcedId": json["componentResource"]["sourcedId"], "allocatedSourcedId": "alloc-001"}}


def test_create_component_resource_success():
    mock_http = MockHttp()
    body = TimebackCreateComponentResourceBody(
        sourcedId="new-cr",
        title="Lesson 1",
        courseComponent=TimebackSourcedIdReference(sourcedId="comp-001"),
        resource=TimebackSourcedIdReference(sourcedId="res-001"),
    )
    request = TimebackCreateComponentResourceRequest(componentResource=body)
    resp = create_component_resource(mock_http, request)
    assert isinstance(resp, TimebackCreateComponentResourceResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "new-cr"

