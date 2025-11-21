from timeback.services.oneroster.gradebook.endpoints.delete_result import (
    delete_result,
)
from timeback.models.request import TimebackDeleteResultRequest


class MockHttp:
    def delete(self, path):
        assert path == "/ims/oneroster/gradebook/v1p2/results/result-123"
        # Simulate 204 response (no content)
        return None


def test_delete_result_success():
    request = TimebackDeleteResultRequest(sourced_id="result-123")
    resp = delete_result(MockHttp(), request)
    assert resp is None


def test_delete_result_not_found_propagates():
    """Test that 404 errors are propagated correctly."""
    class MockHttpNotFound:
        def delete(self, path):
            from timeback.errors import NotFoundError
            raise NotFoundError("Result not found", status_code=404)
    
    request = TimebackDeleteResultRequest(sourced_id="result-nonexistent")
    try:
        delete_result(MockHttpNotFound(), request)
        assert False, "Expected NotFoundError"
    except Exception as e:
        assert "Result not found" in str(e)

