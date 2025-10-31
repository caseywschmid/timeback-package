from timeback.services.oneroster.rostering.endpoints.create_user import create_user
from timeback.models.request import TimebackCreateUserRequest, TimebackCreateUserBody
from timeback.models.response import TimebackCreateUserResponse
from timeback.models.timeback_user_role import TimebackUserRole
from timeback.enums.timeback_role_type import TimebackRoleType
from timeback.enums.timeback_role_name import TimebackRoleName
from timeback.models.timeback_org_ref import TimebackOrgRef


class MockHttp:
    def post(self, path, json=None):
        assert path.endswith("/ims/oneroster/rostering/v1p2/users/")
        # Simulate 201 response body with sourcedIdPairs
        return {
            "sourcedIdPairs": {
                "suppliedSourcedId": json["user"].get("sourcedId", "temp-id"),
                "allocatedSourcedId": "allocated-123",
            }
        }


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
    resp = create_user(MockHttp(), req)
    assert isinstance(resp, TimebackCreateUserResponse)
    assert resp.sourcedIdPairs.allocatedSourcedId == "allocated-123"

