from timeback import Timeback
from timeback.models.request import TimebackGetAllCategoriesRequest, TimebackQueryParams


def main():
    client = Timeback()

    # Basic request without query params
    request = TimebackGetAllCategoriesRequest()
    response = client.oneroster.gradebook.get_all_categories(request)
    
    print(f"Total categories: {response.total_count}")
    print(f"Page {response.page_number} of {response.page_count}")
    
    for category in response.categories:
        weight_str = f" (weight: {category.weight})" if category.weight else ""
        print(f"  - {category.sourcedId}: {category.title}{weight_str}")

    # Example with pagination and filtering
    query_params = TimebackQueryParams(
        limit=10,
        offset=0,
        filter="status='active'",
        sort="title",
        order_by="asc",
    )
    request_with_params = TimebackGetAllCategoriesRequest(query_params=query_params)
    response_filtered = client.oneroster.gradebook.get_all_categories(request_with_params)
    print(f"\nFiltered categories: {len(response_filtered.categories)} of {response_filtered.total_count}")


if __name__ == "__main__":
    main()

