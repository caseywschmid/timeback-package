from timeback.services.oneroster.resources.endpoints.get_resource import get_resource
from timeback.models.request import TimebackGetResourceRequest
from timeback.models.response import TimebackGetResourceResponse


class MockHttp:
    def get(self, path, params=None):
        return {
            "resource": {
                "sourcedId": "res-001",
                "status": "active",
                "dateLastModified": "2024-01-15T12:00:00Z",
                "title": "Math Video",
                "vendorResourceId": "vendor-123",
                "importance": "primary",
            }
        }


def test_get_resource_success():
    """Test successful resource retrieval."""
    mock_http = MockHttp()
    request = TimebackGetResourceRequest(sourced_id="res-001")
    resp = get_resource(mock_http, request)

    assert isinstance(resp, TimebackGetResourceResponse)
    assert resp.resource.sourcedId == "res-001"
    assert resp.resource.title == "Math Video"

