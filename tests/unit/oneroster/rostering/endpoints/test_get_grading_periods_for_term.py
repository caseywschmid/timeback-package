from timeback.services.oneroster.rostering.endpoints.get_grading_periods_for_term import get_grading_periods_for_term
from timeback.models.request import TimebackGetGradingPeriodsForTermRequest
from timeback.models.response import TimebackGetAllTermsResponse


class MockHttp:
    def __init__(self):
        self.last_path = None

    def get(self, path, params=None):
        self.last_path = path
        return {
            "academicSessions": [
                {
                    "sourcedId": "gp-001",
                    "title": "Q1 2024",
                    "type": "gradingPeriod",
                    "startDate": "2024-08-01",
                    "endDate": "2024-10-15",
                    "schoolYear": 2024,
                    "org": {"sourcedId": "school-001"},
                }
            ],
            "totalCount": 1, "pageCount": 1, "pageNumber": 1, "offset": 0, "limit": 100,
        }


def test_get_grading_periods_for_term_success():
    mock_http = MockHttp()
    request = TimebackGetGradingPeriodsForTermRequest(term_sourced_id="term-001")
    resp = get_grading_periods_for_term(mock_http, request)
    assert isinstance(resp, TimebackGetAllTermsResponse)
    assert len(resp.academicSessions) == 1
    assert "/ims/oneroster/rostering/v1p2/terms/term-001/gradingPeriods" in mock_http.last_path

