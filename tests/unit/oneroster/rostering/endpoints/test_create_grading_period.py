from timeback.services.oneroster.rostering.endpoints.create_grading_period import create_grading_period
from timeback.models.request import TimebackCreateGradingPeriodRequest
from timeback.models.response import TimebackCreateGradingPeriodResponse
from timeback.models.timeback_academic_session import TimebackAcademicSession
from timeback.enums import TimebackAcademicSessionType
from timeback.models.timeback_org_ref import TimebackOrgRef


class MockHttp:
    def __init__(self):
        self.last_json = None

    def post(self, path, json=None):
        self.last_json = json
        return {"sourcedIdPairs": {"suppliedSourcedId": json["academicSession"]["sourcedId"], "allocatedSourcedId": "gp-001"}}


def test_create_grading_period_success():
    mock_http = MockHttp()
    session = TimebackAcademicSession(
        sourcedId="new-gp",
        title="Q1 2024",
        type=TimebackAcademicSessionType.GRADING_PERIOD,
        startDate="2024-08-01",
        endDate="2024-10-15",
        schoolYear=2024,
        org=TimebackOrgRef(sourcedId="school-001"),
    )
    request = TimebackCreateGradingPeriodRequest(academic_session=session)
    resp = create_grading_period(mock_http, request)
    assert isinstance(resp, TimebackCreateGradingPeriodResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "new-gp"

