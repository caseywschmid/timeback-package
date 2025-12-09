from timeback.services.oneroster.rostering.endpoints.get_academic_session import get_academic_session
from timeback.models.request import TimebackGetAcademicSessionRequest
from timeback.models.response import TimebackGetAcademicSessionResponse


class MockHttp:
    def get(self, path, params=None):
        return {
            "academicSession": {
                "sourcedId": "as-001",
                "status": "active",
                "title": "Fall 2024",
                "type": "term",
                "startDate": "2024-08-01",
                "endDate": "2024-12-31",
                "schoolYear": 2024,
                "org": {"href": "/orgs/org-001", "sourcedId": "org-001", "type": "org"},
                "dateLastModified": "2024-01-01T00:00:00Z",
            }
        }


def test_get_academic_session_success():
    mock_http = MockHttp()
    request = TimebackGetAcademicSessionRequest(sourced_id="as-001")
    resp = get_academic_session(mock_http, request)
    assert isinstance(resp, TimebackGetAcademicSessionResponse)
    assert resp.academicSession.sourcedId == "as-001"

