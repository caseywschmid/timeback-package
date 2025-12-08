from timeback import Timeback
from timeback.models.request import TimebackPutCategoryRequest
from timeback.models.timeback_category import TimebackCategory
from timeback.enums import TimebackStatus


def main():
    client = Timeback()
    sourced_id = "test-category-001"  # Replace with actual category sourcedId

    # Create a category object to update/create
    category = TimebackCategory(
        sourcedId=sourced_id,
        status=TimebackStatus.ACTIVE,
        title="Homework",
        weight=0.30,
    )

    request = TimebackPutCategoryRequest(
        sourced_id=sourced_id,
        category=category
    )
    response = client.oneroster.gradebook.put_category(request)
    
    print(f"Category updated/created: {response.category.sourcedId}")
    print(f"  Title: {response.category.title}")
    print(f"  Status: {response.category.status}")
    print(f"  Weight: {response.category.weight}")


if __name__ == "__main__":
    main()

