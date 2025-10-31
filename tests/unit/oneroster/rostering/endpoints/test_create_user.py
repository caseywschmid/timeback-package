from timeback.services.oneroster.rostering.endpoints.create_user import create_user
from timeback.models.request import TimebackCreateUserRequest, TimebackCreateUserBody
from timeback.models.timeback_user import TimebackUser
from timeback.enums import TimebackStatus
from timeback.models.timeback_user_role import TimebackUserRole
from timeback.enums.timeback_role_type import TimebackRoleType
from timeback.enums.timeback_role_name import TimebackRoleName
from timeback.models.timeback_org_ref import TimebackOrgRef


class MockHttp:
    def post(self, path, json=None):
        assert path.endswith("/ims/oneroster/rostering/v1p2/users/")
        user = json["user"].copy()
        user.setdefault("sourcedId", "u-created")
        user.setdefault("status", TimebackStatus.ACTIVE)
        user.setdefault("agents", [])
        user.setdefault("userProfiles", [])
        return {"user": user}


def test_create_user_success():
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
    user = create_user(MockHttp(), req)
    assert isinstance(user, TimebackUser)
    assert user.sourcedId == "u-created"
    assert user.givenName == "Chris"

