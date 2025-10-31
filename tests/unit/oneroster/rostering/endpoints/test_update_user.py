from timeback.services.oneroster.rostering.endpoints.update_user import update_user
from timeback.models.request.timeback_update_user_request import (
    TimebackUpdateUserRequest,
    TimebackUpdateUserBody,
)
from timeback.models.timeback_user import TimebackUser
from timeback.enums import TimebackStatus
from timeback.models.timeback_user_role import TimebackUserRole
from timeback.enums.timeback_role_type import TimebackRoleType
from timeback.enums.timeback_role_name import TimebackRoleName
from timeback.models.timeback_org_ref import TimebackOrgRef
from timeback.errors import NotFoundError


class MockHttp:
    def put(self, path, json=None):
        assert "/ims/oneroster/rostering/v1p2/users/" in path
        # Echo back a realistic user wrapper
        user = json["user"].copy()
        user.setdefault("sourcedId", "u1")
        user.setdefault("status", TimebackStatus.ACTIVE)
        user.setdefault("agents", [])
        user.setdefault("userProfiles", [])
        return {"user": user}


def test_update_user_success():
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
    user = update_user(MockHttp(), "u1", req)
    assert isinstance(user, TimebackUser)
    assert user.sourcedId == "u1"
    assert user.givenName == "Alice"
    assert user.familyName == "Baker"
    assert user.enabledUser is True


def test_update_user_not_found_raises():
    class MockHttpNotFound:
        def put(self, path, json=None):
            raise NotFoundError("Resource not found (status=404)")

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

    try:
        update_user(MockHttpNotFound(), "missing-id", req)
        assert False, "Expected NotFoundError"
    except NotFoundError:
        pass

