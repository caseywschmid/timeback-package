from timeback import Timeback
from timeback.models.request import (
    TimebackGetCategoriesForClassRequest,
    TimebackQueryParams,
)


def main():
    client = Timeback()
    class_sourced_id = "class-123"

    # Example 1: Get categories for a class with default parameters
    print(f"Getting categories for class: {class_sourced_id}")
    request = TimebackGetCategoriesForClassRequest(
        class_sourced_id=class_sourced_id
    )
    resp = client.oneroster.gradebook.get_categories_for_class(request)

    print(f"Total Categories: {resp.total_count}")
    print(f"Page {resp.page_number} of {resp.page_count}")
    print(f"Showing {len(resp.categories)} categories")
    print()

    for category in resp.categories:
        print(f"- Category {category.sourcedId}")
        print(f"  Title: {category.title}")
        print(f"  Status: {category.status}")
        if category.weight is not None:
            print(f"  Weight: {category.weight}")
        if category.dateLastModified:
            print(f"  Last Modified: {category.dateLastModified}")
        print()

    # Example 2: Get categories with query parameters
    print("\n--- With Query Parameters ---")
    query_params = TimebackQueryParams(limit=10, offset=0, fields="sourcedId,title,weight")
    request_with_params = TimebackGetCategoriesForClassRequest(
        class_sourced_id=class_sourced_id,
        query_params=query_params
    )
    resp_filtered = client.oneroster.gradebook.get_categories_for_class(request_with_params)

    print(f"Filtered Categories: {len(resp_filtered.categories)} categories")


if __name__ == "__main__":
    main()

