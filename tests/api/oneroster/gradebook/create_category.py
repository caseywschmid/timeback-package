from timeback import Timeback
from timeback.models.request import TimebackCreateCategoryRequest
from timeback.models.timeback_category import TimebackCategory
from timeback.enums import TimebackStatus


def main():
    client = Timeback()

    # Create a category with all fields
    category = TimebackCategory(
        sourcedId="test-category-001",  # Optional - will be auto-generated if not provided
        status=TimebackStatus.ACTIVE,
        title="Homework",
        weight=0.3,
        metadata={"description": "Daily homework assignments"},
    )

    request = TimebackCreateCategoryRequest(category=category)
    response = client.oneroster.gradebook.create_category(request)
    
    print(f"Category created!")
    print(f"  Supplied sourcedId: {response.sourcedIdPairs.suppliedSourcedId}")
    print(f"  Allocated sourcedId: {response.sourcedIdPairs.allocatedSourcedId}")

    # Create a minimal category (only required fields)
    minimal_category = TimebackCategory(
        status=TimebackStatus.ACTIVE,
        title="Exams",
    )
    
    minimal_request = TimebackCreateCategoryRequest(category=minimal_category)
    minimal_response = client.oneroster.gradebook.create_category(minimal_request)
    
    print(f"\nMinimal category created!")
    print(f"  Allocated sourcedId: {minimal_response.sourcedIdPairs.allocatedSourcedId}")


if __name__ == "__main__":
    main()

