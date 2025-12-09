from timeback import Timeback
from timeback.models.request import TimebackCreateUserRequest, TimebackCreateUserBody
from timeback.models.timeback_user_role import TimebackUserRole
from timeback.enums.timeback_role_type import TimebackRoleType
from timeback.enums.timeback_role_name import TimebackRoleName
from timeback.models.timeback_org_ref import TimebackOrgRef
from timeback.models.timeback_agent_ref import TimebackAgentRef
from timeback.enums.timeback_agent_type import TimebackAgentType
from timeback.logs.logger import configure_logging

log = configure_logging(__name__, log_level="DEBUG")


def main():
    client = Timeback()

    body = TimebackCreateUserBody(
        enabledUser=True,
        givenName="Charlie",
        familyName="Smith",
        email="onboarding-test-student@example.com",
        roles=[
            TimebackUserRole(
                roleType=TimebackRoleType.PRIMARY,
                role=TimebackRoleName.STUDENT,
                org=TimebackOrgRef(
                    sourcedId="f47ac10b-58cc-4372-a567-0e02b2c3d479"
                ),  # Alpha Anywhere Org Id
            )
        ],
        agents=[
            TimebackAgentRef(
                sourcedId="20b836c5-20d1-4a87-a4b3-7e6c39cb43b9",
                type=TimebackAgentType.USER,
            ),  # Alpha Anywhere Agent Id
        ],
        metadata={
            "alphaanywhere": {
                "schoolGrade": 8,
                "actualStartDate": "2025-12-08",
                "enrollmentStatus": "enrolled",
                "enrollmentStartDate": "2025-12-08",
            },
        },
        primaryOrg=TimebackOrgRef(sourcedId="f47ac10b-58cc-4372-a567-0e02b2c3d479"),
    )
    req = TimebackCreateUserRequest(user=body)

    resp = client.oneroster.rostering.create_user(req)
    if not resp:
        log.error("No result")
        return
    log.info(
        f"{resp.sourcedIdPairs.suppliedSourcedId} -> {resp.sourcedIdPairs.allocatedSourcedId}"
    )
    log.debug(resp.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
