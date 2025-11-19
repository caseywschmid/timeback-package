from timeback.services.oneroster.gradebook.endpoints.create_score_scale import (
    create_score_scale,
)
from timeback.models.request import TimebackCreateScoreScaleRequest
from timeback.models.response import TimebackCreateScoreScaleResponse
from timeback.models.timeback_score_scale import (
    TimebackScoreScale,
    TimebackScoreScaleValue,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus


class MockHttp:
    def post(self, path, json=None):
        assert path == "/ims/oneroster/gradebook/v1p2/scoreScales"
        assert json is not None
        assert "scoreScale" in json
        # Simulate 201 response body
        return {
            "sourcedIdPairs": {
                "suppliedSourcedId": "scale-123",
                "allocatedSourcedId": "allocated-scale-456",
            }
        }


def test_create_score_scale_success():
    # Create a score scale value
    scale_value = TimebackScoreScaleValue(
        itemValueLHS="90",
        itemValueRHS="100",
        value="A",
        description="Excellent",
    )

    # Create a score scale
    score_scale = TimebackScoreScale(
        sourcedId="scale-123",
        status=TimebackStatus.ACTIVE,
        title="Letter Grade Scale",
        type="letter",
        **{"class": TimebackSourcedIdReference(sourcedId="class-123")},
        scoreScaleValue=[scale_value],
    )

    request = TimebackCreateScoreScaleRequest(score_scale=score_scale)
    resp = create_score_scale(MockHttp(), request)
    
    assert isinstance(resp, TimebackCreateScoreScaleResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "scale-123"
    assert resp.sourcedIdPairs.allocatedSourcedId == "allocated-scale-456"
