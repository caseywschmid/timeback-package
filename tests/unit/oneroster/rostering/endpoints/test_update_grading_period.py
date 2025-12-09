from timeback.services.oneroster.rostering.endpoints.update_grading_period import update_grading_period
from timeback.models.request import TimebackUpdateGradingPeriodRequest
from timeback.models.response import TimebackUpdateGradingPeriodResponse
from timeback.models.timeback_academic_session import TimebackAcademicSession
from timeback.enums import TimebackAcademicSessionType
from timeback.models.timeback_org_ref import TimebackOrgRef


class MockHttp:
    def put(self, path, json=None):
        return {
            "academicSession": {
                "sourcedId": "gp-001",
                "title": "Updated Q1 2024",
                "type": "gradingPeriod",
                "startDate": "2024-08-01",
                "endDate": "2024-10-15",
                "schoolYear": 2024,
                "org": {"sourcedId": "school-001"},
            }
        }


def test_update_grading_period_success():
    mock_http = MockHttp()
    session = TimebackAcademicSession(
        sourcedId="gp-001",
        title="Updated Q1 2024",
        type=TimebackAcademicSessionType.GRADING_PERIOD,
        startDate="2024-08-01",
        endDate="2024-10-15",
        schoolYear=2024,
        org=TimebackOrgRef(sourcedId="school-001"),
    )
    request = TimebackUpdateGradingPeriodRequest(sourced_id="gp-001", academic_session=session)
    resp = update_grading_period(mock_http, request)
    assert isinstance(resp, TimebackUpdateGradingPeriodResponse)
    assert resp.academicSession.title == "Updated Q1 2024"

