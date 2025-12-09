from timeback.services.oneroster.gradebook.endpoints.delete_score_scale import (
    delete_score_scale,
)
from timeback.models.request import TimebackDeleteScoreScaleRequest


class MockHttp:
    def delete(self, path):
        assert path == "/ims/oneroster/gradebook/v1p2/scoreScales/scale-123"
        # Simulate 204 response (no content)
        return None


def test_delete_score_scale_success():
    request = TimebackDeleteScoreScaleRequest(sourced_id="scale-123")
    resp = delete_score_scale(MockHttp(), request)
    assert resp is None
