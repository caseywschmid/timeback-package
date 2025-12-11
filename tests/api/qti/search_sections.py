"""API test for search_sections endpoint.

This script tests the search_sections endpoint against the QTI API.
Run with: python -m tests.api.qti.search_sections

Requires environment variables:
- TIMEBACK_CLIENT_ID
- TIMEBACK_CLIENT_SECRET
- TIMEBACK_ENVIRONMENT (production or staging)
"""

from timeback import Timeback
from timeback.models.request import TimebackSearchAssessmentTestsRequest


def main():
    """Test the search_sections endpoint."""
    client = Timeback()

    print("=" * 60)
    print("Testing search_sections endpoint")
    print("=" * 60)

    # First, find an assessment test with test parts
    print("\n1. Finding an assessment test with test parts...")
    search_response = client.qti.search_assessment_tests(
        TimebackSearchAssessmentTestsRequest(limit=5)
    )
    
    if not search_response.items:
        print("   No assessment tests found.")
        return

    test = None
    part = None
    for t in search_response.items:
        parts = client.qti.search_test_parts(t.identifier)
        if parts.items:
            test = t
            part = parts.items[0]
            break

    if not test or not part:
        print("   No test parts found in any test.")
        return

    print(f"   Using test: {test.identifier}")
    print(f"   Using part: {part.identifier}")

    # Search sections
    print("\n2. Searching sections:")
    try:
        result = client.qti.search_sections(test.identifier, part.identifier)
        
        print(f"   Total: {result.total}")
        print(f"   Page: {result.page}/{result.pages}")
        
        if result.items:
            print(f"\n   Sections:")
            for i, section in enumerate(result.items[:5], 1):
                print(f"   {i}. {section.identifier}: {section.title}")
                if section.qti_assessment_item_ref:
                    print(f"      Items: {len(section.qti_assessment_item_ref)}")
        else:
            print("   No sections found.")
    except Exception as e:
        print(f"   Error: {e}")

    print("\n" + "=" * 60)
    print("search_sections test completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

