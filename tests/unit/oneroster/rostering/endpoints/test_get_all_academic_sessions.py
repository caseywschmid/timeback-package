from timeback.services.oneroster.rostering.endpoints.get_all_academic_sessions import get_all_academic_sessions
from timeback.models.request import TimebackGetAllAcademicSessionsRequest
from timeback.models.response import TimebackGetAllAcademicSessionsResponse


class MockHttp:
    def get(self, path, params=None):
        return {
            "academicSessions": [
                {
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
            ],
            "totalCount": 1, "pageCount": 1, "pageNumber": 1, "offset": 0, "limit": 100,
        }


def test_get_all_academic_sessions_success():
    mock_http = MockHttp()
    request = TimebackGetAllAcademicSessionsRequest()
    resp = get_all_academic_sessions(mock_http, request)
    assert isinstance(resp, TimebackGetAllAcademicSessionsResponse)
    assert len(resp.academicSessions) == 1
    assert resp.academicSessions[0].sourcedId == "as-001"

