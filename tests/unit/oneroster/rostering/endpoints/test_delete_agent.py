from timeback.services.oneroster.rostering.endpoints.delete_agent import delete_agent
from timeback.errors import NotFoundError
from timeback.models.response import TimebackDeleteAgentResponse


class MockHttp:
    def __init__(self):
        self.called_with = None

    def delete(self, path):
        self.called_with = path
        return {"message": "Agent deleted successfully"}


def test_delete_agent_success():
    http = MockHttp()
    result = delete_agent(http, "u1", "a1")
    assert http.called_with.endswith(
        "/ims/oneroster/rostering/v1p2/users/u1/agents/a1"
    )
    assert isinstance(result, TimebackDeleteAgentResponse)
    assert result.message == "Agent deleted successfully"


def test_delete_agent_not_found_propagates():
    class MockHttpNotFound:
        def delete(self, path):
            raise NotFoundError("Resource not found")

    try:
        delete_agent(MockHttpNotFound(), "missing", "missing")
        assert False, "Expected NotFoundError"
    except NotFoundError:
        pass
