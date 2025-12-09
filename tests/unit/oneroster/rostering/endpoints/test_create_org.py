from timeback.services.oneroster.rostering.endpoints.create_org import create_org
from timeback.models.request import TimebackCreateOrgRequest
from timeback.models.response import TimebackCreateOrgResponse
from timeback.models.timeback_org import TimebackOrg
from timeback.enums import TimebackOrgType


class MockHttp:
    def __init__(self):
        self.last_json = None

    def post(self, path, json=None):
        self.last_json = json
        return {"sourcedIdPairs": {"suppliedSourcedId": json["org"]["sourcedId"], "allocatedSourcedId": "org-001"}}


def test_create_org_success():
    mock_http = MockHttp()
    org = TimebackOrg(name="Test School", type=TimebackOrgType.SCHOOL, sourcedId="new-org")
    request = TimebackCreateOrgRequest(org=org)
    resp = create_org(mock_http, request)
    assert isinstance(resp, TimebackCreateOrgResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "new-org"

