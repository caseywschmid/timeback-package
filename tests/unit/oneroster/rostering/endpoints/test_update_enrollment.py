from timeback.services.oneroster.rostering.endpoints.update_enrollment import update_enrollment
from timeback.models.request import TimebackUpdateEnrollmentRequest, TimebackUpdateEnrollmentBody
from timeback.models.response import TimebackUpdateEnrollmentResponse


class MockHttp:
    def put(self, path, json=None):
        return {
            "enrollment": {
                "sourcedId": "enroll-001",
                "role": "student",
                "primary": True,
                "user": {"sourcedId": "user-001"},
                "class": {"sourcedId": "class-001"},
            }
        }


def test_update_enrollment_success():
    mock_http = MockHttp()
    body = TimebackUpdateEnrollmentBody(primary=True)
    request = TimebackUpdateEnrollmentRequest(sourced_id="enroll-001", enrollment=body)
    resp = update_enrollment(mock_http, request)
    assert isinstance(resp, TimebackUpdateEnrollmentResponse)
    assert resp.enrollment.primary is True

