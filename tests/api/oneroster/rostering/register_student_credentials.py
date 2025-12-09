from timeback import Timeback
from timeback.models.request import (
    TimebackRegisterStudentCredentialsRequest,
    TimebackCredentials,
)


def main():
    client = Timeback()

    user_id = "31129aea-12b2-4e9e-a6e5-f5c8b712d674"
    application_name = "PowerPath"
    credentials = TimebackCredentials(username="student123", password="securepass456")

    request = TimebackRegisterStudentCredentialsRequest(
        user_id=user_id, application_name=application_name, credentials=credentials
    )
    resp = client.oneroster.rostering.register_student_credentials(request)

    print(f"User Profile ID: {resp.user_profile_id}")
    print(f"Credential ID: {resp.credential_id}")
    print(f"Message: {resp.message}")


if __name__ == "__main__":
    main()
