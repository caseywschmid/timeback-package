from timeback.services.oneroster.rostering.endpoints.get_all_grading_periods import get_all_grading_periods
from timeback.models.request import TimebackGetAllGradingPeriodsRequest
from timeback.models.response import TimebackGetAllTermsResponse


class MockHttp:
    def get(self, path, params=None):
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


def test_get_all_grading_periods_success():
    mock_http = MockHttp()
    request = TimebackGetAllGradingPeriodsRequest()
    resp = get_all_grading_periods(mock_http, request)
    assert isinstance(resp, TimebackGetAllTermsResponse)
    assert len(resp.academicSessions) == 1
    assert resp.academicSessions[0].type.value == "gradingPeriod"

