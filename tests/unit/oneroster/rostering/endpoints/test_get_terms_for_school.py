from timeback.services.oneroster.rostering.endpoints.get_terms_for_school import get_terms_for_school
from timeback.models.request import TimebackGetTermsForSchoolRequest
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


def test_get_terms_for_school_success():
    """Test successful retrieval of terms for a school."""
    mock_http = MockHttp()
    request = TimebackGetTermsForSchoolRequest(school_sourced_id="school-001")
    resp = get_terms_for_school(mock_http, request)

    assert isinstance(resp, TimebackGetAllTermsResponse)
    assert len(resp.academicSessions) == 1
    assert "/ims/oneroster/rostering/v1p2/schools/school-001/terms" in mock_http.last_path

