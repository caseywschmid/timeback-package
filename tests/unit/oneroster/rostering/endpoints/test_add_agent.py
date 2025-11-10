from timeback.services.oneroster.rostering.endpoints.add_agent import add_agent
from timeback.models.request import TimebackAddAgentRequest


class MockHttp:
    def post(self, path, json=None):
        assert path.endswith("/ims/oneroster/rostering/v1p2/users/test-user-id/agents")
        assert json == {"agentSourcedId": "test-agent-id"}
        # Simulate 200 response body
        return {
            "message": "Successfully added agent for user",
        }


def test_add_agent_success():
    request = TimebackAddAgentRequest(user_id="test-user-id", agent_sourced_id="test-agent-id")
    resp = add_agent(MockHttp(), request)
    assert isinstance(resp, dict)
    assert resp["message"] == "Successfully added agent for user"

