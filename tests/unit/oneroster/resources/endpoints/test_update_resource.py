from timeback.services.oneroster.resources.endpoints.update_resource import update_resource
from timeback.models.request import TimebackUpdateResourceRequest, TimebackUpdateResourceBody
from timeback.models.response import TimebackUpdateResourceResponse
from timeback.enums import TimebackImportance


class MockHttp:
    def __init__(self):
        self.last_path = None
        self.last_json = None

    def put(self, path, json=None):
        self.last_path = path
        self.last_json = json
        return {
            "resource": {
                "sourcedId": "res-001",
                "status": "active",
                "dateLastModified": "2024-01-15T12:00:00Z",
                "title": "Updated Math Video",
                "vendorResourceId": "vendor-123",
                "importance": "primary",
            }
        }


def test_update_resource_success():
    """Test successful resource update."""
    mock_http = MockHttp()
    body = TimebackUpdateResourceBody(
        sourcedId="res-001",
        title="Updated Math Video",
        vendorResourceId="vendor-123",
        importance=TimebackImportance.PRIMARY,
    )
    request = TimebackUpdateResourceRequest(sourced_id="res-001", resource=body)
    resp = update_resource(mock_http, request)

    assert isinstance(resp, TimebackUpdateResourceResponse)
    assert resp.resource.title == "Updated Math Video"
    assert "/ims/oneroster/resources/v1p2/resources/res-001" in mock_http.last_path
    assert "sourced_id" not in mock_http.last_json

