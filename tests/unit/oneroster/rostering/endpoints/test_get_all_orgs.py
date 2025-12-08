from timeback.services.oneroster.rostering.endpoints.get_all_orgs import get_all_orgs
from timeback.models.request import TimebackGetAllOrgsRequest
from timeback.models.response import TimebackGetAllOrgsResponse


class MockHttp:
    def get(self, path, params=None):
        return {
            "orgs": [{"sourcedId": "org-001", "name": "Test School", "type": "school"}],
            "totalCount": 1, "pageCount": 1, "pageNumber": 1, "offset": 0, "limit": 100,
        }


def test_get_all_orgs_success():
    mock_http = MockHttp()
    request = TimebackGetAllOrgsRequest()
    resp = get_all_orgs(mock_http, request)
    assert isinstance(resp, TimebackGetAllOrgsResponse)
    assert len(resp.orgs) == 1

