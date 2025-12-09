from timeback.services.oneroster.rostering.endpoints.update_academic_session import update_academic_session
from timeback.models.request import TimebackUpdateAcademicSessionRequest, TimebackUpdateAcademicSessionBody
from timeback.models.response import TimebackUpdateAcademicSessionResponse


class MockHttp:
    def put(self, path, json=None):
        return {
            "academicSession": {
                "sourcedId": "as-001",
                "status": "active",
                "title": "Spring 2025",
                "type": "term",
                "startDate": "2025-01-01",
                "endDate": "2025-05-31",
                "schoolYear": 2025,
                "org": {"href": "/orgs/org-001", "sourcedId": "org-001", "type": "org"},
                "dateLastModified": "2024-01-02T00:00:00Z",
            }
        }


def test_update_academic_session_success():
    mock_http = MockHttp()
    body = TimebackUpdateAcademicSessionBody(title="Spring 2025")
    request = TimebackUpdateAcademicSessionRequest(sourced_id="as-001", academicSession=body)
    resp = update_academic_session(mock_http, request)
    assert isinstance(resp, TimebackUpdateAcademicSessionResponse)
    assert resp.academicSession.title == "Spring 2025"

