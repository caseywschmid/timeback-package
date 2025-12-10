"""API test for search_stimuli endpoint.

This script tests the search_stimuli endpoint against the QTI API.
Run with: python -m tests.api.qti.search_stimuli

Requires environment variables:
- TIMEBACK_CLIENT_ID
- TIMEBACK_CLIENT_SECRET
- TIMEBACK_ENVIRONMENT (production or staging)
"""

from timeback import Timeback
from timeback.models.request import TimebackSearchStimuliRequest
from timeback.enums import TimebackQTISortField, TimebackSortOrder


def main():
    """Test the search_stimuli endpoint."""
    client = Timeback()

    print("=" * 60)
    print("Testing search_stimuli endpoint")
    print("=" * 60)

    # Basic request without parameters
    print("\n1. Basic search with default parameters:")
    response = client.qti.search_stimuli()
    print(f"   Total stimuli: {response.total}")
    print(f"   Page: {response.page} / {response.pages}")
    print(f"   Items on this page: {len(response.items)}")
    
    if response.items:
        first_stimulus = response.items[0]
        print(f"   First stimulus:")
        print(f"     - Identifier: {first_stimulus.identifier}")
        print(f"     - Title: {first_stimulus.title}")
        print(f"     - Language: {first_stimulus.language}")
        print(f"     - Created: {first_stimulus.created_at}")

    # Search with query parameter
    print("\n2. Search with query parameter:")
    request_with_query = TimebackSearchStimuliRequest(query="ecosystem")
    response_with_query = client.qti.search_stimuli(request_with_query)
    print(f"   Query: 'ecosystem'")
    print(f"   Total matches: {response_with_query.total}")
    print(f"   Items returned: {len(response_with_query.items)}")
    
    if response_with_query.items:
        for stimulus in response_with_query.items[:3]:
            print(f"     - {stimulus.title} ({stimulus.identifier})")

    # Search with pagination
    print("\n3. Search with pagination:")
    request_paginated = TimebackSearchStimuliRequest(page=1, limit=5)
    response_paginated = client.qti.search_stimuli(request_paginated)
    print(f"   Limit: 5 items per page")
    print(f"   Page 1 of {response_paginated.pages}")
    print(f"   Items on page: {len(response_paginated.items)}")

    # Search with sorting
    print("\n4. Search with sorting:")
    request_sorted = TimebackSearchStimuliRequest(
        sort=TimebackQTISortField.TITLE,
        order=TimebackSortOrder.ASC,
        limit=5
    )
    response_sorted = client.qti.search_stimuli(request_sorted)
    print(f"   Sort by: title (ascending)")
    print(f"   First 5 titles:")
    for stimulus in response_sorted.items:
        print(f"     - {stimulus.title}")

    # Search with all parameters
    print("\n5. Search with all parameters:")
    request_full = TimebackSearchStimuliRequest(
        query="test",
        page=1,
        limit=3,
        sort=TimebackQTISortField.UPDATED_AT,
        order=TimebackSortOrder.DESC
    )
    response_full = client.qti.search_stimuli(request_full)
    print(f"   Query: 'test'")
    print(f"   Sort: updatedAt (desc)")
    print(f"   Page 1, limit 3")
    print(f"   Results: {len(response_full.items)} of {response_full.total} total")

    print("\n" + "=" * 60)
    print("search_stimuli tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

