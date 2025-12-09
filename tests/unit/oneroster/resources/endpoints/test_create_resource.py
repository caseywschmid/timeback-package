from timeback.services.oneroster.resources.endpoints.create_resource import create_resource
from timeback.models.request import TimebackCreateResourceRequest, TimebackCreateResourceBody
from timeback.models.response import TimebackCreateResourceResponse
from timeback.enums import TimebackImportance


class MockHttp:
    def __init__(self):
        self.last_path = None
        self.last_json = None

    def post(self, path, json=None):
        self.last_path = path
        self.last_json = json
        return {
            "sourcedIdPairs": {
                "suppliedSourcedId": json["resource"]["sourcedId"],
                "allocatedSourcedId": "allocated-res-001",
            }
        }


def test_create_resource_success():
    """Test successful resource creation."""
    mock_http = MockHttp()
    body = TimebackCreateResourceBody(
        sourcedId="res-001",
        title="Math Video",
        vendorResourceId="vendor-123",
        importance=TimebackImportance.PRIMARY,
    )
    request = TimebackCreateResourceRequest(resource=body)
    resp = create_resource(mock_http, request)

    assert isinstance(resp, TimebackCreateResourceResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "res-001"
    assert resp.sourcedIdPairs.allocatedSourcedId == "allocated-res-001"
    assert "/ims/oneroster/resources/v1p2/resources" in mock_http.last_path

