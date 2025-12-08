from timeback.services.oneroster.rostering.endpoints.get_org import get_org
from timeback.models.request import TimebackGetOrgRequest
from timeback.models.response import TimebackGetOrgResponse


class MockHttp:
    def get(self, path, params=None):
        return {"org": {"sourcedId": "org-001", "name": "Test School", "type": "school"}}


def test_get_org_success():
    mock_http = MockHttp()
    request = TimebackGetOrgRequest(sourced_id="org-001")
    resp = get_org(mock_http, request)
    assert isinstance(resp, TimebackGetOrgResponse)
    assert resp.org.sourcedId == "org-001"

