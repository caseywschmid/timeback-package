from timeback.services.oneroster.rostering.endpoints.get_all_component_resources import get_all_component_resources
from timeback.models.request import TimebackGetAllComponentResourcesRequest
from timeback.models.response import TimebackGetAllComponentResourcesResponse


class MockHttp:
    def get(self, path, params=None):
        return {
            "componentResources": [
                {
                    "sourcedId": "cr-001",
                    "title": "Lesson 1",
                    "courseComponent": {"href": "/components/comp-001", "sourcedId": "comp-001", "type": "courseComponent"},
                    "resource": {"href": "/resources/res-001", "sourcedId": "res-001", "type": "resource"},
                }
            ],
            "totalCount": 1, "pageCount": 1, "pageNumber": 1, "offset": 0, "limit": 100,
        }


def test_get_all_component_resources_success():
    mock_http = MockHttp()
    request = TimebackGetAllComponentResourcesRequest()
    resp = get_all_component_resources(mock_http, request)
    assert isinstance(resp, TimebackGetAllComponentResourcesResponse)
    assert len(resp.componentResources) == 1
    assert resp.componentResources[0].sourcedId == "cr-001"

