"""API test for search_test_parts endpoint.

This script tests the search_test_parts endpoint against the QTI API.
Run with: python -m tests.api.qti.search_test_parts

Requires environment variables:
- TIMEBACK_CLIENT_ID
- TIMEBACK_CLIENT_SECRET
- TIMEBACK_ENVIRONMENT (production or staging)
"""

from timeback import Timeback
from timeback.models.request import (
    TimebackSearchAssessmentTestsRequest,
    TimebackSearchTestPartsRequest,
)
from timeback.enums import TimebackQTINavigationMode


def main():
    """Test the search_test_parts endpoint."""
    client = Timeback()

    print("=" * 60)
    print("Testing search_test_parts endpoint")
    print("=" * 60)

    # First, find an assessment test
    print("\n1. Finding an assessment test...")
    search_response = client.qti.search_assessment_tests(
        TimebackSearchAssessmentTestsRequest(limit=5)
    )
    
    if not search_response.items:
        print("   No assessment tests found. Create one first.")
        return

    test = search_response.items[0]
    print(f"   Using test: {test.identifier} - {test.title}")

    # Search all test parts
    print("\n2. Searching all test parts:")
    try:
        result = client.qti.search_test_parts(test.identifier)
        
        print(f"   Total: {result.total}")
        print(f"   Page: {result.page}/{result.pages}")
        
        if result.items:
            print(f"\n   Test Parts:")
            for i, part in enumerate(result.items[:5], 1):
                print(f"   {i}. {part.identifier}")
                print(f"      - Navigation: {part.navigation_mode.value}")
                print(f"      - Submission: {part.submission_mode.value}")
                if part.qti_assessment_section:
                    print(f"      - Sections: {len(part.qti_assessment_section)}")
        else:
            print("   No test parts found.")
    except Exception as e:
        print(f"   Error: {e}")

    # Search with filter
    print("\n3. Searching for linear test parts:")
    try:
        request = TimebackSearchTestPartsRequest(
            navigation_mode=TimebackQTINavigationMode.LINEAR
        )
        result = client.qti.search_test_parts(test.identifier, request)
        print(f"   Found {result.total} linear test parts")
    except Exception as e:
        print(f"   Error: {e}")

    print("\n" + "=" * 60)
    print("search_test_parts test completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

