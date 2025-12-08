from timeback.services.oneroster.rostering.endpoints.create_grading_period_for_term import create_grading_period_for_term
from timeback.models.request import TimebackCreateGradingPeriodForTermRequest
from timeback.models.response import TimebackCreateGradingPeriodResponse
from timeback.models.timeback_academic_session import TimebackAcademicSession
from timeback.enums import TimebackAcademicSessionType
from timeback.models.timeback_org_ref import TimebackOrgRef


class MockHttp:
    def __init__(self):
        self.last_path = None
        self.last_json = None

    def post(self, path, json=None):
        self.last_path = path
        self.last_json = json
        return {"sourcedIdPairs": {"suppliedSourcedId": json["academicSession"]["sourcedId"], "allocatedSourcedId": "gp-001"}}


def test_create_grading_period_for_term_success():
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
    request = TimebackCreateGradingPeriodForTermRequest(term_sourced_id="term-001", academic_session=session)
    resp = create_grading_period_for_term(mock_http, request)
    assert isinstance(resp, TimebackCreateGradingPeriodResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "new-gp"
    assert "/ims/oneroster/rostering/v1p2/terms/term-001/gradingPeriods" in mock_http.last_path

