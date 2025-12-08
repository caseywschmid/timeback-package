from timeback.services.oneroster.rostering.endpoints.update_org import update_org
from timeback.models.request import TimebackUpdateOrgRequest
from timeback.models.response import TimebackUpdateOrgResponse
from timeback.models.timeback_org import TimebackOrg
from timeback.enums import TimebackOrgType


class MockHttp:
    def put(self, path, json=None):
        return {"org": {"sourcedId": "org-001", "name": "Updated School", "type": "school"}}


def test_update_org_success():
    mock_http = MockHttp()
    org = TimebackOrg(sourcedId="org-001", name="Updated School", type=TimebackOrgType.SCHOOL)
    request = TimebackUpdateOrgRequest(sourced_id="org-001", org=org)
    resp = update_org(mock_http, request)
    assert isinstance(resp, TimebackUpdateOrgResponse)
    assert resp.org.name == "Updated School"

