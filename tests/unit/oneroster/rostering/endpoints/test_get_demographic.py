from timeback.services.oneroster.rostering.endpoints.get_demographic import get_demographic
from timeback.models.request import TimebackGetDemographicRequest
from timeback.models.response import TimebackGetDemographicResponse


class MockHttp:
    def get(self, path, params=None):
        return {
            "demographics": {"sourcedId": "demo-001", "birthDate": "2000-01-15", "sex": "male"}
        }


def test_get_demographic_success():
    mock_http = MockHttp()
    request = TimebackGetDemographicRequest(sourced_id="demo-001")
    resp = get_demographic(mock_http, request)
    assert isinstance(resp, TimebackGetDemographicResponse)
    assert resp.demographics.sourcedId == "demo-001"

