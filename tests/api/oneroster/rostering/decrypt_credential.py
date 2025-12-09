from timeback import Timeback
from timeback.models.request import TimebackDecryptCredentialRequest


def main():
    client = Timeback()

    user_id = "31129aea-12b2-4e9e-a6e5-f5c8b712d674"
    credential_id = "cred-123-456-789"

    request = TimebackDecryptCredentialRequest(
        user_id=user_id, credential_id=credential_id
    )
    resp = client.oneroster.rostering.decrypt_credential(request)

    print(f"Decrypted Password: {resp.password}")


if __name__ == "__main__":
    main()
