from timeback.services.oneroster.rostering.endpoints.get_all_demographics import get_all_demographics
from timeback.models.request import TimebackGetAllDemographicsRequest
from timeback.models.response import TimebackGetAllDemographicsResponse


class MockHttp:
    def get(self, path, params=None):
        return {
            "demographics": [
                {"sourcedId": "demo-001", "birthDate": "2000-01-15", "sex": "male"}
            ],
            "totalCount": 1, "pageCount": 1, "pageNumber": 1, "offset": 0, "limit": 100,
        }


def test_get_all_demographics_success():
    mock_http = MockHttp()
    request = TimebackGetAllDemographicsRequest()
    resp = get_all_demographics(mock_http, request)
    assert isinstance(resp, TimebackGetAllDemographicsResponse)
    assert len(resp.demographics) == 1
    assert resp.demographics[0].sourcedId == "demo-001"

