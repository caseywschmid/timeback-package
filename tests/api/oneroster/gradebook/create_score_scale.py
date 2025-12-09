from timeback import Timeback
from timeback.models.request import TimebackCreateScoreScaleRequest
from timeback.models.timeback_score_scale import (
    TimebackScoreScale,
    TimebackScoreScaleValue,
)
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus


def main():
    client = Timeback()

    # Create scale values (grade ranges)
    scale_values = [
        TimebackScoreScaleValue(
            itemValueLHS="90",
            itemValueRHS="100",
            value="A",
            description="Excellent",
        ),
        TimebackScoreScaleValue(
            itemValueLHS="80",
            itemValueRHS="89",
            value="B",
            description="Good",
        ),
        TimebackScoreScaleValue(
            itemValueLHS="70",
            itemValueRHS="79",
            value="C",
            description="Satisfactory",
        ),
        TimebackScoreScaleValue(
            itemValueLHS="60",
            itemValueRHS="69",
            value="D",
            description="Needs Improvement",
        ),
        TimebackScoreScaleValue(
            itemValueLHS="0",
            itemValueRHS="59",
            value="F",
            description="Failing",
        ),
    ]

    # Create the score scale
    score_scale = TimebackScoreScale(
        sourcedId="my-letter-grade-scale-001",
        status=TimebackStatus.ACTIVE,
        title="Standard Letter Grade Scale",
        type="letter",
        **{"class": TimebackSourcedIdReference(sourcedId="class-123-456")},
        course=None,
        scoreScaleValue=scale_values,
        metadata={"description": "Standard A-F grading scale"},
    )

    # Create the request
    request = TimebackCreateScoreScaleRequest(score_scale=score_scale)

    # Call the API
    resp = client.oneroster.gradebook.create_score_scale(request)

    print(f"Score Scale Created Successfully!")
    print(f"Supplied SourcedId: {resp.sourcedIdPairs.suppliedSourcedId}")
    print(f"Allocated SourcedId: {resp.sourcedIdPairs.allocatedSourcedId}")


if __name__ == "__main__":
    main()
