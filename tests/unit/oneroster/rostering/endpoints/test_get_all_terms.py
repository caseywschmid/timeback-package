from timeback.services.oneroster.rostering.endpoints.get_all_terms import get_all_terms
from timeback.models.request import TimebackGetAllTermsRequest
from timeback.models.response import TimebackGetAllTermsResponse


class MockHttp:
    def __init__(self):
        self.last_path = None

    def get(self, path, params=None):
        self.last_path = path
        return {
            "academicSessions": [
                {
                    "sourcedId": "term-001",
                    "title": "Fall 2024",
                    "type": "term",
                    "startDate": "2024-08-01",
                    "endDate": "2024-12-15",
                    "schoolYear": 2024,
                    "org": {"sourcedId": "school-001"},
                }
            ],
            "totalCount": 1,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }


def test_get_all_terms_success():
    """Test successful retrieval of all terms."""
    mock_http = MockHttp()
    request = TimebackGetAllTermsRequest()
    resp = get_all_terms(mock_http, request)

    assert isinstance(resp, TimebackGetAllTermsResponse)
    assert len(resp.academicSessions) == 1
    assert "/ims/oneroster/rostering/v1p2/terms" in mock_http.last_path

