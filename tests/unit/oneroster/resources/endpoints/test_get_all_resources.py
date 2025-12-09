from timeback.services.oneroster.resources.endpoints.get_all_resources import get_all_resources
from timeback.models.request import TimebackGetAllResourcesRequest, TimebackQueryParams
from timeback.models.response import TimebackGetAllResourcesResponse
from datetime import datetime


class MockHttp:
    def __init__(self):
        self.last_path = None
        self.last_params = None

    def get(self, path, params=None):
        self.last_path = path
        self.last_params = params
        return {
            "resources": [
                {
                    "sourcedId": "res-001",
                    "status": "active",
                    "dateLastModified": "2024-01-15T12:00:00Z",
                    "title": "Math Video",
                    "vendorResourceId": "vendor-123",
                    "importance": "primary",
                    "roles": ["primary"],
                },
            ],
            "totalCount": 1,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }


def test_get_all_resources_success():
    """Test successful resources retrieval."""
    mock_http = MockHttp()
    request = TimebackGetAllResourcesRequest()
    resp = get_all_resources(mock_http, request)

    assert isinstance(resp, TimebackGetAllResourcesResponse)
    assert len(resp.resources) == 1
    assert resp.resources[0].sourcedId == "res-001"
    assert resp.totalCount == 1
    assert "/ims/oneroster/resources/v1p2/resources" in mock_http.last_path


def test_get_all_resources_with_query_params():
    """Test resources retrieval with query parameters."""
    mock_http = MockHttp()
    query_params = TimebackQueryParams(limit=50, offset=10)
    request = TimebackGetAllResourcesRequest(query_params=query_params)
    resp = get_all_resources(mock_http, request)

    assert isinstance(resp, TimebackGetAllResourcesResponse)
    assert mock_http.last_params == {"limit": 50, "offset": 10}

