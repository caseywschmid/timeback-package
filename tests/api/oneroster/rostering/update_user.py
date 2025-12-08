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
    
    # Mother (Tina Kevorkian)
    sourced_id = "9069005b-a061-466a-bd02-5018ac4ffd7b"

    # Correct agents (her 3 children)
    correct_agents = [
        TimebackAgentRef(sourcedId="8ef6786a-48fa-4edb-922b-e28493e75511", type=TimebackAgentType.USER),  # Arshag
        TimebackAgentRef(sourcedId="d1d3cf29-5743-478e-b9cd-889336765e01", type=TimebackAgentType.USER),  # Yeremya
        TimebackAgentRef(sourcedId="975f0849-8f4e-423f-9560-1b94af66b59e", type=TimebackAgentType.USER),  # NEW Siyon
    ]

    body = TimebackUpdateUserBody(
        sourcedId=sourced_id,
        enabledUser=True,
        givenName="Tina",
        familyName="Kevorkian",
        email="tinakevork@me.com",
        roles=[
            TimebackUserRole(
                roleType=TimebackRoleType.PRIMARY,
                role=TimebackRoleName.PARENT,
                org=TimebackOrgRef(sourcedId="346488d3-efb9-4f56-95ea-f4a441de2370"),
            )
        ],
        agents=correct_agents,
    )
    req = TimebackUpdateUserRequest(user=body)

    resp = client.oneroster.rostering.update_user(req)
    if not resp:
        print("Update succeeded (server returned no content)")
        print("Verifying by fetching user...")
        from timeback.models.request import TimebackGetUserRequest
        verify = client.oneroster.rostering.get_user(TimebackGetUserRequest(sourced_id=sourced_id))
        print(f"User: {verify.user.sourcedId}, {verify.user.givenName} {verify.user.familyName}")
        print(f"Agents: {verify.user.agents}")
        return
    print(f"Updated: {resp.user.sourcedId}, {resp.user.givenName} {resp.user.familyName}")
    print(f"Agents: {resp.user.agents}")


if __name__ == "__main__":
    main()


