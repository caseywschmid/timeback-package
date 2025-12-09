from timeback.services.oneroster.rostering.endpoints.update_demographic import update_demographic
from timeback.models.request import TimebackUpdateDemographicRequest, TimebackUpdateDemographicBody
from timeback.models.response import TimebackUpdateDemographicResponse


class MockHttp:
    def put(self, path, json=None):
        return {
            "demographics": {"sourcedId": "demo-001", "birthDate": "2000-01-15", "sex": "female"}
        }


def test_update_demographic_success():
    mock_http = MockHttp()
    body = TimebackUpdateDemographicBody(sex="female")
    request = TimebackUpdateDemographicRequest(sourced_id="demo-001", demographics=body)
    resp = update_demographic(mock_http, request)
    assert isinstance(resp, TimebackUpdateDemographicResponse)
    assert resp.demographics.sex == "female"

