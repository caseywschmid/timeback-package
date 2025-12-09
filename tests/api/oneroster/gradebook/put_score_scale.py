from timeback import Timeback
from timeback.models.request import TimebackPutScoreScaleRequest
from timeback.models.timeback_score_scale import (
    TimebackScoreScale,
    TimebackScoreScaleValue,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus


def main():
    client = Timeback()
    sourced_id = "scale-123-456"

    # Create scale values (grade ranges)
    scale_values = [
        TimebackScoreScaleValue(
            itemValueLHS="90",
            itemValueRHS="100",
            value="A",
            description="Excellent",
        ),
        TimebackScoreScaleValue(
            itemValueLHS="0",
            itemValueRHS="89",
            value="F",
            description="Failing",
        ),
    ]

    # Create the score scale
    score_scale = TimebackScoreScale(
        sourcedId=sourced_id,
        status=TimebackStatus.ACTIVE,
        title="Updated Letter Grade Scale",
        type="letter",
        **{"class": TimebackSourcedIdReference(sourcedId="class-123-456")},
        scoreScaleValue=scale_values,
    )

    # Create the request
    print(f"Updating score scale: {sourced_id}")
    request = TimebackPutScoreScaleRequest(
        sourced_id=sourced_id, score_scale=score_scale
    )

    # Call the API
    resp = client.oneroster.gradebook.put_score_scale(request)

    print(f"Score Scale Updated Successfully!")
    print(f"SourcedId: {resp.score_scale.sourcedId}")
    print(f"Title: {resp.score_scale.title}")
    print(f"Values: {len(resp.score_scale.scoreScaleValue)}")


if __name__ == "__main__":
    main()
