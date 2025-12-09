from timeback import Timeback
from timeback.models.request import (
    TimebackGetScoreScaleRequest,
    TimebackQueryParams,
)


def main():
    client = Timeback()
    sourced_id = "scale-123-456"

    # Example 1: Get score scale by sourcedId
    print(f"Fetching score scale: {sourced_id}")
    request = TimebackGetScoreScaleRequest(sourced_id=sourced_id)
    resp = client.oneroster.gradebook.get_score_scale(request)

    scale = resp.score_scale
    print(f"Found Score Scale: {scale.title} ({scale.sourcedId})")
    print(f"Type: {scale.type}")
    print(f"Status: {scale.status}")
    print(f"Values:")
    for val in scale.scoreScaleValue:
        print(f"  - {val.value}: {val.itemValueLHS} - {val.itemValueRHS} ({val.description})")

    # Example 2: Get score scale with fields parameter
    print("\n--- With Fields Parameter ---")
    query_params = TimebackQueryParams(fields="sourcedId,title,type")
    request_fields = TimebackGetScoreScaleRequest(
        sourced_id=sourced_id, query_params=query_params
    )
    resp_fields = client.oneroster.gradebook.get_score_scale(request_fields)
    
    print(f"Fetched partial score scale: {resp_fields.score_scale.title}")


if __name__ == "__main__":
    main()
