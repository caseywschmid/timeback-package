from timeback.services.oneroster.rostering.endpoints.get_classes_for_term import get_classes_for_term
from timeback.models.request import TimebackGetClassesForTermRequest
from timeback.models.response import TimebackGetAllClassesResponse


class MockHttp:
    def __init__(self):
        self.last_path = None

    def get(self, path, params=None):
        self.last_path = path
        return {
            "classes": [
                {
                    "sourcedId": "class-001",
                    "title": "Math 101",
                    "status": "active",
                    "course": {"sourcedId": "course-001"},
                    "org": {"sourcedId": "org-001"},
                    "terms": [{"sourcedId": "term-001"}],
                }
            ],
            "totalCount": 1,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }


def test_get_classes_for_term_success():
    """Test successful retrieval of classes for a term."""
    mock_http = MockHttp()
    request = TimebackGetClassesForTermRequest(term_sourced_id="term-001")
    resp = get_classes_for_term(mock_http, request)

    assert isinstance(resp, TimebackGetAllClassesResponse)
    assert len(resp.classes) == 1
    assert "/ims/oneroster/rostering/v1p2/terms/term-001/classes" in mock_http.last_path

