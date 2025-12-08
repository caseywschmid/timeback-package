from timeback.services.oneroster.rostering.endpoints.get_all_enrollments import get_all_enrollments
from timeback.models.request import TimebackGetAllEnrollmentsRequest
from timeback.models.response import TimebackGetAllEnrollmentsResponse


class MockHttp:
    def get(self, path, params=None):
        return {
            "enrollments": [
                {
                    "sourcedId": "enroll-001",
                    "role": "student",
                    "user": {"sourcedId": "user-001"},
                    "class": {"sourcedId": "class-001"},
                }
            ],
            "totalCount": 1, "pageCount": 1, "pageNumber": 1, "offset": 0, "limit": 100,
        }


def test_get_all_enrollments_success():
    mock_http = MockHttp()
    request = TimebackGetAllEnrollmentsRequest()
    resp = get_all_enrollments(mock_http, request)
    assert isinstance(resp, TimebackGetAllEnrollmentsResponse)
    assert len(resp.enrollments) == 1
    assert resp.enrollments[0].sourcedId == "enroll-001"

