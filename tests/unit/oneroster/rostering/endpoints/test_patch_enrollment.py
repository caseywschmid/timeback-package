from timeback.services.oneroster.rostering.endpoints.patch_enrollment import patch_enrollment
from timeback.models.request import TimebackPatchEnrollmentRequest, TimebackPatchEnrollmentBody
from timeback.models.response import TimebackUpdateEnrollmentResponse


class MockHttp:
    def patch(self, path, json=None):
        return {
            "enrollment": {
                "sourcedId": "enroll-001",
                "role": "student",
                "primary": False,
                "metadata": {"goal": "A+"},
                "user": {"sourcedId": "user-001"},
                "class": {"sourcedId": "class-001"},
            }
        }


def test_patch_enrollment_success():
    mock_http = MockHttp()
    body = TimebackPatchEnrollmentBody(metadata={"goal": "A+"})
    request = TimebackPatchEnrollmentRequest(sourced_id="enroll-001", enrollment=body)
    resp = patch_enrollment(mock_http, request)
    assert isinstance(resp, TimebackUpdateEnrollmentResponse)
    assert resp.enrollment.metadata == {"goal": "A+"}

