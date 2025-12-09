from timeback.services.oneroster.rostering.endpoints.decrypt_credential import (
    decrypt_credential,
)
from timeback.models.request import TimebackDecryptCredentialRequest
from timeback.models.response import TimebackDecryptCredentialResponse


class MockHttp:
    def post(self, path, json=None):
        assert path.endswith(
            "/ims/oneroster/rostering/v1p2/users/test-user-id/credentials/test-cred-id/decrypt"
        )
        # Simulate 200 response body
        return {
            "password": "decrypted-password-123",
        }


def test_decrypt_credential_success():
    request = TimebackDecryptCredentialRequest(
        user_id="test-user-id", credential_id="test-cred-id"
    )
    resp = decrypt_credential(MockHttp(), request)
    assert isinstance(resp, TimebackDecryptCredentialResponse)
    assert resp.password == "decrypted-password-123"
