from timeback import Timeback
from timeback.models.request import (
    TimebackGetAllScoreScalesRequest,
    TimebackQueryParams,
)


def main():
    client = Timeback()

    # Example 1: Get all score scales with default parameters
    request = TimebackGetAllScoreScalesRequest()
    resp = client.oneroster.gradebook.get_all_score_scales(request)

    print(f"Total Score Scales: {resp.total_count}")
    print(f"Page {resp.page_number} of {resp.page_count}")
    print(f"Showing {len(resp.score_scales)} score scales")
    print()

    for scale in resp.score_scales:
        print(f"- {scale.title} ({scale.sourcedId})")
        print(f"  Type: {scale.type}")
        print(f"  Status: {scale.status}")
        print(f"  Values: {len(scale.scoreScaleValue)} scale values")
        print()

    # Example 2: Get score scales with query parameters
    print("\n--- With Query Parameters ---")
    query_params = TimebackQueryParams(limit=10, offset=0, fields="sourcedId,title,type")
    request_with_params = TimebackGetAllScoreScalesRequest(query_params=query_params)
    resp_filtered = client.oneroster.gradebook.get_all_score_scales(request_with_params)

    print(f"Filtered Results: {len(resp_filtered.score_scales)} score scales")


if __name__ == "__main__":
    main()
