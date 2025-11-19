from timeback import Timeback
from timeback.models.request import (
    TimebackGetScoreScalesForSchoolRequest,
    TimebackQueryParams,
)


def main():
    client = Timeback()
    school_sourced_id = "school-123-456"

    # Example 1: Get score scales for school
    print(f"Fetching score scales for school: {school_sourced_id}")
    request = TimebackGetScoreScalesForSchoolRequest(sourced_id=school_sourced_id)
    resp = client.oneroster.gradebook.get_score_scales_for_school(request)

    print(f"Total Count: {resp.total_count}")
    for scale in resp.score_scales:
        print(f"  - {scale.title} ({scale.sourcedId})")

    # Example 2: Get score scales with pagination
    print("\n--- With Pagination ---")
    query_params = TimebackQueryParams(limit=5, offset=0)
    request_paginated = TimebackGetScoreScalesForSchoolRequest(
        sourced_id=school_sourced_id, query_params=query_params
    )
    resp_paginated = client.oneroster.gradebook.get_score_scales_for_school(request_paginated)
    
    print(f"Page {resp_paginated.page_number} of {resp_paginated.page_count}")
    print(f"Returned {len(resp_paginated.score_scales)} items")


if __name__ == "__main__":
    main()
