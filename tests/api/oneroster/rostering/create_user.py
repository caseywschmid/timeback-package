from timeback import Timeback
from timeback.models.request import TimebackCreateUserRequest, TimebackCreateUserBody
from timeback.models.timeback_user_role import TimebackUserRole
from timeback.enums.timeback_role_type import TimebackRoleType
from timeback.enums.timeback_role_name import TimebackRoleName
from timeback.models.timeback_org_ref import TimebackOrgRef


def main():
    client = Timeback()

    body = TimebackCreateUserBody(
        enabledUser=True,
        givenName="Chris",
        familyName="Doe",
        email="chris@example.com",
        roles=[
            TimebackUserRole(
                roleType=TimebackRoleType.PRIMARY,
                role=TimebackRoleName.STUDENT,
                org=TimebackOrgRef(sourcedId="org1"),
            )
        ],
    )
    req = TimebackCreateUserRequest(user=body)

    resp = client.oneroster.rostering.create_user(req)
    if not resp:
        print("No result")
        return
    print(
        resp.sourcedIdPairs.suppliedSourcedId,
        "->",
        resp.sourcedIdPairs.allocatedSourcedId,
    )


if __name__ == "__main__":
    main()


