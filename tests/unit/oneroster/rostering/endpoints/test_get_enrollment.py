from timeback.services.oneroster.rostering.endpoints.get_enrollment import get_enrollment
from timeback.models.request import TimebackGetEnrollmentRequest
from timeback.models.response import TimebackGetEnrollmentResponse


class MockHttp:
    def get(self, path, params=None):
        return {
            "enrollment": {
                "sourcedId": "enroll-001",
                "role": "student",
                "user": {"sourcedId": "user-001"},
                "class": {"sourcedId": "class-001"},
            }
        }


def test_get_enrollment_success():
    mock_http = MockHttp()
    request = TimebackGetEnrollmentRequest(sourced_id="enroll-001")
    resp = get_enrollment(mock_http, request)
    assert isinstance(resp, TimebackGetEnrollmentResponse)
    assert resp.enrollment.sourcedId == "enroll-001"

