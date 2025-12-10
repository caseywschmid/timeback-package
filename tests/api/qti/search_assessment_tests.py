"""API test for search_assessment_tests endpoint.

This script tests the search_assessment_tests endpoint against the QTI API.
Run with: python -m tests.api.qti.search_assessment_tests

Requires environment variables:
- TIMEBACK_CLIENT_ID
- TIMEBACK_CLIENT_SECRET
- TIMEBACK_ENVIRONMENT (production or staging)
"""

from timeback import Timeback
from timeback.models.request import TimebackSearchAssessmentTestsRequest
from timeback.enums import (
    TimebackQTIAssessmentTestSortField,
    TimebackSortOrder,
    TimebackQTINavigationMode,
    TimebackQTISubmissionMode,
)


def main():
    """Test the search_assessment_tests endpoint."""
    client = Timeback()

    print("=" * 60)
    print("Testing search_assessment_tests endpoint")
    print("=" * 60)

    # Basic search with default parameters
    print("\n1. Basic search with default parameters:")
    response = client.qti.search_assessment_tests()
    print(f"   Total assessment tests: {response.total}")
    print(f"   Page: {response.page} / {response.pages}")
    print(f"   Items on this page: {len(response.items)}")
    
    if response.items:
        first_test = response.items[0]
        print(f"   First test:")
        print(f"     - Identifier: {first_test.identifier}")
        print(f"     - Title: {first_test.title}")
        print(f"     - QTI Version: {first_test.qti_version}")
        if first_test.qti_test_part:
            print(f"     - Test parts: {len(first_test.qti_test_part)}")

    # Search with query parameter
    print("\n2. Search with query parameter:")
    request_with_query = TimebackSearchAssessmentTestsRequest(query="math")
    response_with_query = client.qti.search_assessment_tests(request_with_query)
    print(f"   Query: 'math'")
    print(f"   Total matches: {response_with_query.total}")
    print(f"   Items returned: {len(response_with_query.items)}")
    
    if response_with_query.items:
        for test in response_with_query.items[:3]:
            print(f"     - {test.title} ({test.identifier})")

    # Search with navigation mode filter
    print("\n3. Search with navigation mode filter:")
    request_nav = TimebackSearchAssessmentTestsRequest(
        navigation_mode=TimebackQTINavigationMode.LINEAR
    )
    response_nav = client.qti.search_assessment_tests(request_nav)
    print(f"   Navigation mode: LINEAR")
    print(f"   Total linear tests: {response_nav.total}")

    # Search with submission mode filter
    print("\n4. Search with submission mode filter:")
    request_sub = TimebackSearchAssessmentTestsRequest(
        submission_mode=TimebackQTISubmissionMode.INDIVIDUAL
    )
    response_sub = client.qti.search_assessment_tests(request_sub)
    print(f"   Submission mode: INDIVIDUAL")
    print(f"   Total individual tests: {response_sub.total}")

    # Search with pagination
    print("\n5. Search with pagination:")
    request_paginated = TimebackSearchAssessmentTestsRequest(page=1, limit=5)
    response_paginated = client.qti.search_assessment_tests(request_paginated)
    print(f"   Limit: 5 items per page")
    print(f"   Page 1 of {response_paginated.pages}")
    print(f"   Items on page: {len(response_paginated.items)}")

    # Search with sorting
    print("\n6. Search with sorting:")
    request_sorted = TimebackSearchAssessmentTestsRequest(
        sort=TimebackQTIAssessmentTestSortField.TITLE,
        order=TimebackSortOrder.ASC,
        limit=5
    )
    response_sorted = client.qti.search_assessment_tests(request_sorted)
    print(f"   Sort by: title (ascending)")
    print(f"   First 5 titles:")
    for test in response_sorted.items:
        print(f"     - {test.title}")

    print("\n" + "=" * 60)
    print("search_assessment_tests tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

