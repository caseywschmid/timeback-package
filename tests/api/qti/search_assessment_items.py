"""API test for search_assessment_items endpoint.

This script tests the search_assessment_items endpoint against the QTI API.
Run with: python -m tests.api.qti.search_assessment_items

Requires environment variables:
- TIMEBACK_CLIENT_ID
- TIMEBACK_CLIENT_SECRET
- TIMEBACK_ENVIRONMENT (production or staging)
"""

from timeback import Timeback
from timeback.models.request import TimebackSearchAssessmentItemsRequest
from timeback.enums import TimebackQTIAssessmentItemSortField, TimebackSortOrder


def main():
    """Test the search_assessment_items endpoint."""
    client = Timeback()

    print("=" * 60)
    print("Testing search_assessment_items endpoint")
    print("=" * 60)

    # Basic search with default parameters
    print("\n1. Basic search with default parameters:")
    response = client.qti.search_assessment_items()
    print(f"   Total assessment items: {response.total}")
    print(f"   Page: {response.page} / {response.pages}")
    print(f"   Items on this page: {len(response.items)}")
    
    if response.items:
        first_item = response.items[0]
        print(f"   First item:")
        print(f"     - Identifier: {first_item.identifier}")
        print(f"     - Title: {first_item.title}")
        print(f"     - Type: {first_item.type}")
        print(f"     - QTI Version: {first_item.qtiVersion}")

    # Search with query parameter
    print("\n2. Search with query parameter:")
    request_with_query = TimebackSearchAssessmentItemsRequest(query="math")
    response_with_query = client.qti.search_assessment_items(request_with_query)
    print(f"   Query: 'math'")
    print(f"   Total matches: {response_with_query.total}")
    print(f"   Items returned: {len(response_with_query.items)}")
    
    if response_with_query.items:
        for item in response_with_query.items[:3]:
            print(f"     - {item.title} ({item.identifier}) [{item.type}]")

    # Search with filter by type
    print("\n3. Search with type filter:")
    request_filtered = TimebackSearchAssessmentItemsRequest(filter="type='choice'")
    response_filtered = client.qti.search_assessment_items(request_filtered)
    print(f"   Filter: type='choice'")
    print(f"   Total choice items: {response_filtered.total}")
    
    if response_filtered.items:
        for item in response_filtered.items[:3]:
            print(f"     - {item.title} (type: {item.type})")

    # Search with pagination
    print("\n4. Search with pagination:")
    request_paginated = TimebackSearchAssessmentItemsRequest(page=1, limit=5)
    response_paginated = client.qti.search_assessment_items(request_paginated)
    print(f"   Limit: 5 items per page")
    print(f"   Page 1 of {response_paginated.pages}")
    print(f"   Items on page: {len(response_paginated.items)}")

    # Search with sorting
    print("\n5. Search with sorting:")
    request_sorted = TimebackSearchAssessmentItemsRequest(
        sort=TimebackQTIAssessmentItemSortField.TITLE,
        order=TimebackSortOrder.ASC,
        limit=5
    )
    response_sorted = client.qti.search_assessment_items(request_sorted)
    print(f"   Sort by: title (ascending)")
    print(f"   First 5 titles:")
    for item in response_sorted.items:
        print(f"     - {item.title}")

    print("\n" + "=" * 60)
    print("search_assessment_items tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

