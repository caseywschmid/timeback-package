from timeback import Timeback
from timeback.models.request import TimebackUpdateUserRequest, TimebackUpdateUserBody
from timeback.models.timeback_user_role import TimebackUserRole
from timeback.enums.timeback_role_type import TimebackRoleType
from timeback.enums.timeback_role_name import TimebackRoleName
from timeback.models.timeback_org_ref import TimebackOrgRef


def main():
    client = Timeback()
    sourced_id = "replace-with-real-user-sourced-id"

    body = TimebackUpdateUserBody(
        enabledUser=True,
        givenName="Alice",
        familyName="Baker",
        email="alice@example.com",
        roles=[
            TimebackUserRole(
                roleType=TimebackRoleType.PRIMARY,
                role=TimebackRoleName.TEACHER,
                org=TimebackOrgRef(sourcedId="org1"),
            )
        ],
    )
    req = TimebackUpdateUserRequest(user=body)

    user = client.oneroster.rostering.update_user(sourced_id, req)
    if not user:
        print("No result")
        return
    print(user.sourcedId, user.givenName, user.familyName)


if __name__ == "__main__":
    main()


