from timeback.services.oneroster.rostering.endpoints.delete_agent import delete_agent
from timeback.models.request import TimebackDeleteAgentRequest
from timeback.errors import NotFoundError


class MockHttp:
    def __init__(self):
        self.called_with = None

    def delete(self, path):
        self.called_with = path
        return {"message": "Agent deleted successfully"}


def test_delete_agent_success():
    http = MockHttp()
    request = TimebackDeleteAgentRequest(user_id="u1", agent_sourced_id="a1")
    result = delete_agent(http, request)
    assert http.called_with.endswith(
        "/ims/oneroster/rostering/v1p2/users/u1/agents/a1"
    )
    assert isinstance(result, dict)
    assert result["message"] == "Agent deleted successfully"


def test_delete_agent_not_found_propagates():
    class MockHttpNotFound:
        def delete(self, path):
            raise NotFoundError("Resource not found")

    try:
        request = TimebackDeleteAgentRequest(user_id="missing", agent_sourced_id="missing")
        delete_agent(MockHttpNotFound(), request)
        assert False, "Expected NotFoundError"
    except NotFoundError:
        pass
