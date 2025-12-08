from timeback.services.oneroster.rostering.endpoints.get_term import get_term
from timeback.models.request import TimebackGetTermRequest
from timeback.models.response import TimebackGetTermResponse


class MockHttp:
    def get(self, path, params=None):
        return {
            "academicSession": {
                "sourcedId": "term-001",
                "title": "Fall 2024",
                "type": "term",
                "startDate": "2024-08-01",
                "endDate": "2024-12-15",
                "schoolYear": 2024,
                "org": {"sourcedId": "school-001"},
            }
        }


def test_get_term_success():
    """Test successful retrieval of a term."""
    mock_http = MockHttp()
    request = TimebackGetTermRequest(sourced_id="term-001")
    resp = get_term(mock_http, request)

    assert isinstance(resp, TimebackGetTermResponse)
    assert resp.academicSession.sourcedId == "term-001"
    assert resp.academicSession.title == "Fall 2024"

