from timeback.services.oneroster.gradebook.endpoints.put_score_scale import (
    put_score_scale,
)
from timeback.models.request import TimebackPutScoreScaleRequest
from timeback.models.response import TimebackPutScoreScaleResponse
from timeback.models.timeback_score_scale import (
    TimebackScoreScale,
    TimebackScoreScaleValue,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus


class MockHttp:
    def put(self, path, json=None):
        assert path == "/ims/oneroster/gradebook/v1p2/scoreScales/scale-123"
        assert json is not None
        assert "scoreScale" in json
        assert json["scoreScale"]["sourcedId"] == "scale-123"
        # Simulate 201 response body
        return json


def test_put_score_scale_success():
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

    request = TimebackPutScoreScaleRequest(
        sourced_id="scale-123", score_scale=score_scale
    )
    resp = put_score_scale(MockHttp(), request)
    
    assert isinstance(resp, TimebackPutScoreScaleResponse)
    assert resp.score_scale.sourcedId == "scale-123"
    assert resp.score_scale.title == "Letter Grade Scale"
