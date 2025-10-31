from timeback.models.request import TimebackCreateUserRequest, TimebackCreateUserBody
from timeback.models.timeback_user_role import TimebackUserRole
from timeback.enums.timeback_role_type import TimebackRoleType
from timeback.enums.timeback_role_name import TimebackRoleName
from timeback.models.timeback_org_ref import TimebackOrgRef


def test_enabled_user_string_normalizes_on_create():
    body = TimebackCreateUserBody(
        enabledUser="true",
        givenName="A",
        familyName="B",
        email="a@example.com",
        roles=[
            TimebackUserRole(
                roleType=TimebackRoleType.PRIMARY,
                role=TimebackRoleName.STUDENT,
                org=TimebackOrgRef(sourcedId="org1"),
            )
        ],
    )
    req = TimebackCreateUserRequest(user=body)
    data = req.to_dict()
    assert data["user"]["enabledUser"] is True

