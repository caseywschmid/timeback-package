from timeback.services.oneroster.rostering.endpoints.register_student_credentials import (
    register_student_credentials,
)
from timeback.models.request import (
    TimebackRegisterStudentCredentialsRequest,
    TimebackCredentials,
)
from timeback.models.response import TimebackRegisterStudentCredentialsResponse


class MockHttp:
    def post(self, path, json=None):
        assert path.endswith(
            "/ims/oneroster/rostering/v1p2/users/test-user-id/credentials"
        )
        assert json == {
            "applicationName": "TestApp",
            "credentials": {"username": "testuser", "password": "testpass"},
        }
        # Simulate 201 response body
        return {
            "userProfileId": "profile-123",
            "credentialId": "cred-456",
            "message": "Student credentials created successfully",
        }


def test_register_student_credentials_success():
    credentials = TimebackCredentials(username="testuser", password="testpass")
    request = TimebackRegisterStudentCredentialsRequest(
        user_id="test-user-id", application_name="TestApp", credentials=credentials
    )
    resp = register_student_credentials(MockHttp(), request)
    assert isinstance(resp, TimebackRegisterStudentCredentialsResponse)
    assert resp.user_profile_id == "profile-123"
    assert resp.credential_id == "cred-456"
    assert resp.message == "Student credentials created successfully"
