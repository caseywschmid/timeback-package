from timeback import Timeback
from timeback.models.request import (
    TimebackGetScoreScalesForClassRequest,
    TimebackQueryParams,
)


def main():
    client = Timeback()
    class_sourced_id = "class-123"

    # Example 1: Get score scales for a class with default parameters
    print(f"Getting score scales for class: {class_sourced_id}")
    request = TimebackGetScoreScalesForClassRequest(
        class_sourced_id=class_sourced_id
    )
    resp = client.oneroster.gradebook.get_score_scales_for_class(request)

    print(f"Total Score Scales: {resp.total_count}")
    print(f"Page {resp.page_number} of {resp.page_count}")
    print(f"Showing {len(resp.score_scales)} score scales")
    print()

    for scale in resp.score_scales:
        print(f"- Score Scale {scale.sourcedId}")
        print(f"  Title: {scale.title}")
        print(f"  Type: {scale.type}")
        print(f"  Status: {scale.status}")
        print(f"  Class: {scale.class_.sourcedId}")
        if scale.course:
            print(f"  Course: {scale.course.sourcedId}")
        print(f"  Score Scale Values:")
        for value in scale.scoreScaleValue:
            print(f"    {value.itemValueLHS}-{value.itemValueRHS}: {value.value}")
            if value.description:
                print(f"      Description: {value.description}")
        if scale.dateLastModified:
            print(f"  Last Modified: {scale.dateLastModified}")
        print()

    # Example 2: Get score scales with query parameters
    print("\n--- With Query Parameters ---")
    query_params = TimebackQueryParams(limit=10, offset=0, fields="sourcedId,title,type")
    request_with_params = TimebackGetScoreScalesForClassRequest(
        class_sourced_id=class_sourced_id,
        query_params=query_params
    )
    resp_filtered = client.oneroster.gradebook.get_score_scales_for_class(request_with_params)

    print(f"Filtered Score Scales: {len(resp_filtered.score_scales)} score scales")


if __name__ == "__main__":
    main()

