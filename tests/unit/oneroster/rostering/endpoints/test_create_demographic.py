from timeback.services.oneroster.rostering.endpoints.create_demographic import create_demographic
from timeback.models.request import TimebackCreateDemographicRequest, TimebackCreateDemographicBody
from timeback.models.response import TimebackCreateDemographicResponse


class MockHttp:
    def __init__(self):
        self.last_json = None

    def post(self, path, json=None):
        self.last_json = json
        return {"sourcedIdPairs": {"suppliedSourcedId": json["demographics"]["sourcedId"], "allocatedSourcedId": "alloc-001"}}


def test_create_demographic_success():
    mock_http = MockHttp()
    body = TimebackCreateDemographicBody(sourcedId="new-demo", birthDate="2000-01-15", sex="male")
    request = TimebackCreateDemographicRequest(demographics=body)
    resp = create_demographic(mock_http, request)
    assert isinstance(resp, TimebackCreateDemographicResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "new-demo"

