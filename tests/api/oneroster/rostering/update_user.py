from timeback import Timeback
from timeback.models.request import TimebackUpdateUserRequest, TimebackUpdateUserBody
from timeback.models.timeback_user_role import TimebackUserRole
from timeback.enums.timeback_role_type import TimebackRoleType
from timeback.enums.timeback_role_name import TimebackRoleName
from timeback.models.timeback_org_ref import TimebackOrgRef
from timeback.models.timeback_agent_ref import TimebackAgentRef
from timeback.enums.timeback_agent_type import TimebackAgentType


def main():
    client = Timeback()
    
    # Fitz Davis (test student)
    sourced_id = "20268c57-3828-4f4a-8144-2ef896681010"

    # Agent reference (parent)
    agents = [
        TimebackAgentRef(sourcedId="e7c72bb0-9264-49c0-a191-388f5741bbb1", type=TimebackAgentType.USER),
    ]

    body = TimebackUpdateUserBody(
        sourcedId=sourced_id,
        enabledUser=True,
        givenName="Fitz",
        familyName="Davis",
        email="fitz.davis@2hourlearning.com",
        roles=[
            TimebackUserRole(
                roleType=TimebackRoleType.PRIMARY,
                role=TimebackRoleName.STUDENT,
                org=TimebackOrgRef(sourcedId="f47ac10b-58cc-4372-a567-0e02b2c3d479"),
            )
        ],
        agents=agents,
        grades=["3"],  # Setting grade to 3
    )
    req = TimebackUpdateUserRequest(user=body)

    resp = client.oneroster.rostering.update_user(req)
    if not resp:
        print("Update succeeded (server returned no content)")
        print("Verifying by fetching user...")
        from timeback.models.request import TimebackGetUserRequest
        verify = client.oneroster.rostering.get_user(TimebackGetUserRequest(sourced_id=sourced_id))
        print(f"User: {verify.user.sourcedId}, {verify.user.givenName} {verify.user.familyName}")
        print(f"Grades: {verify.user.grades}")
        return
    print(f"Updated: {resp.user.sourcedId}, {resp.user.givenName} {resp.user.familyName}")
    print(f"Grades: {resp.user.grades}")


if __name__ == "__main__":
    main()
