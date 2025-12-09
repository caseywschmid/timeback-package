from timeback import Timeback
from timeback.models.request import TimebackGetCategoryRequest, TimebackQueryParams


def main():
    client = Timeback()
    sourced_id = "test-category-001"  # Replace with actual category sourcedId

    # Basic request without query params
    request = TimebackGetCategoryRequest(sourced_id=sourced_id)
    response = client.oneroster.gradebook.get_category(request)
    
    print(f"Category: {response.category.sourcedId}")
    print(f"  Title: {response.category.title}")
    print(f"  Status: {response.category.status}")
    print(f"  Weight: {response.category.weight}")

    # Example with fields query param
    query_params = TimebackQueryParams(fields=["sourcedId", "title", "weight"])
    request_with_fields = TimebackGetCategoryRequest(
        sourced_id=sourced_id,
        query_params=query_params
    )
    response_min = client.oneroster.gradebook.get_category(request_with_fields)
    print(f"\nMinimal category: {response_min.category.sourcedId}, {response_min.category.title}")


if __name__ == "__main__":
    main()

