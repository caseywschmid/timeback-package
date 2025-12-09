from timeback.services.oneroster.rostering.endpoints.create_academic_session import create_academic_session
from timeback.models.request import TimebackCreateAcademicSessionRequest, TimebackCreateAcademicSessionBody
from timeback.models.response import TimebackCreateAcademicSessionResponse
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackAcademicSessionType


class MockHttp:
    def __init__(self):
        self.last_json = None

    def post(self, path, json=None):
        self.last_json = json
        return {"sourcedIdPairs": {"suppliedSourcedId": json["academicSession"]["sourcedId"], "allocatedSourcedId": "alloc-001"}}


def test_create_academic_session_success():
    mock_http = MockHttp()
    body = TimebackCreateAcademicSessionBody(
        sourcedId="new-as",
        title="Fall 2024",
        type=TimebackAcademicSessionType.TERM,
        startDate="2024-08-01",
        endDate="2024-12-31",
        schoolYear="2024",
        org=TimebackSourcedIdReference(sourcedId="org-001"),
    )
    request = TimebackCreateAcademicSessionRequest(academicSession=body)
    resp = create_academic_session(mock_http, request)
    assert isinstance(resp, TimebackCreateAcademicSessionResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "new-as"

