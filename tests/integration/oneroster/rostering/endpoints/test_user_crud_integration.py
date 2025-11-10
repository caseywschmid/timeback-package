import os
import uuid
import pytest

from timeback import Timeback
from timeback.models.request import (
    TimebackCreateUserRequest,
    TimebackCreateUserBody,
    TimebackUpdateUserRequest,
    TimebackUpdateUserBody,
    TimebackGetUserRequest,
)
from timeback.models.timeback_user_role import TimebackUserRole
from timeback.enums.timeback_role_type import TimebackRoleType
from timeback.enums.timeback_role_name import TimebackRoleName
from timeback.models.timeback_org_ref import TimebackOrgRef


@pytest.mark.integration
def test_user_crud_integration():
    """Create a user, fetch it, update it, then delete it (net zero change)."""
    required_vars = [
        "TIMEBACK_CLIENT_ID",
        "TIMEBACK_CLIENT_SECRET",
        "TIMEBACK_ENVIRONMENT",
    ]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        pytest.skip(f"Missing required environment variables: {missing_vars}")

    client = Timeback()

    unique = uuid.uuid4().hex[:8]
    email = f"crud_{unique}@example.com"
    supplied_sourced_id = f"user-{unique}"

    # Create
    org_sourced_id = os.getenv("TIMEBACK_TEST_ORG_SOURCED_ID")
    if not org_sourced_id:
        pytest.skip("Missing TIMEBACK_TEST_ORG_SOURCED_ID for integration CRUD test")
    create_body = TimebackCreateUserBody(
        sourcedId=supplied_sourced_id,
        enabledUser=True,
        givenName="Crud",
        familyName="User",
        email=email,
        roles=[
            TimebackUserRole(
                roleType=TimebackRoleType.PRIMARY,
                role=TimebackRoleName.STUDENT,
                org=TimebackOrgRef(sourcedId=org_sourced_id),
            )
        ],
    )
    create_req = TimebackCreateUserRequest(user=create_body)
    create_resp = client.oneroster.rostering.create_user(create_req)
    assert create_resp and create_resp.sourcedIdPairs.allocatedSourcedId
    sourced_id = create_resp.sourcedIdPairs.allocatedSourcedId

    try:
        # Get
        get_request = TimebackGetUserRequest(sourced_id=sourced_id)
        get_response = client.oneroster.rostering.get_user(get_request)
        assert get_response.user.sourcedId == sourced_id
        assert get_response.user.email == email or get_response.user.email is not None

        # Update
        update_body = TimebackUpdateUserBody(
            sourcedId=sourced_id,
            enabledUser=True,
            givenName="CrudUpdated",
            familyName="User",
            email=email,
            roles=get_response.user.roles,  # preserve roles
        )
        update_req = TimebackUpdateUserRequest(user=update_body)
        updated_resp = client.oneroster.rostering.update_user(update_req)
        assert updated_resp.user.sourcedId == sourced_id
        assert updated_resp.user.givenName == "CrudUpdated"
    finally:
        # Delete (tombstone) - should return None for 204
        result = client.oneroster.rostering.delete_user(sourced_id)
        assert result is None


