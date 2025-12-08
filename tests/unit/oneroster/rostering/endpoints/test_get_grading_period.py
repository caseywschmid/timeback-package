from timeback.services.oneroster.rostering.endpoints.get_grading_period import get_grading_period
from timeback.models.request import TimebackGetGradingPeriodRequest
from timeback.models.response import TimebackGetTermResponse


class MockHttp:
    def get(self, path, params=None):
        return {
            "academicSession": {
                "sourcedId": "gp-001",
                "title": "Q1 2024",
                "type": "gradingPeriod",
                "startDate": "2024-08-01",
                "endDate": "2024-10-15",
                "schoolYear": 2024,
                "org": {"sourcedId": "school-001"},
            }
        }


def test_get_grading_period_success():
    mock_http = MockHttp()
    request = TimebackGetGradingPeriodRequest(sourced_id="gp-001")
    resp = get_grading_period(mock_http, request)
    assert isinstance(resp, TimebackGetTermResponse)
    assert resp.academicSession.sourcedId == "gp-001"

