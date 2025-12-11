"""API test for get_test_part endpoint.

This script tests the get_test_part endpoint against the QTI API.
Run with: python -m tests.api.qti.get_test_part

Requires environment variables:
- TIMEBACK_CLIENT_ID
- TIMEBACK_CLIENT_SECRET
- TIMEBACK_ENVIRONMENT (production or staging)
"""

from timeback import Timeback
from timeback.models.request import TimebackSearchAssessmentTestsRequest


def main():
    """Test the get_test_part endpoint."""
    client = Timeback()

    print("=" * 60)
    print("Testing get_test_part endpoint")
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

    # Find a test part
    print("\n2. Finding test parts...")
    parts_response = client.qti.search_test_parts(test.identifier)
    
    if not parts_response.items:
        print("   No test parts found. Create one first.")
        return

    part = parts_response.items[0]
    print(f"   Using part: {part.identifier}")

    # Get the test part
    print("\n3. Getting test part details:")
    try:
        result = client.qti.get_test_part(test.identifier, part.identifier)
        
        print(f"   Identifier: {result.identifier}")
        print(f"   Navigation: {result.navigation_mode.value}")
        print(f"   Submission: {result.submission_mode.value}")
        if result.qti_assessment_section:
            print(f"   Sections: {len(result.qti_assessment_section)}")
            for section in result.qti_assessment_section[:3]:
                print(f"     - {section.identifier}: {section.title}")
        if result.raw_xml:
            print(f"   Has raw XML: Yes ({len(result.raw_xml)} chars)")
    except Exception as e:
        print(f"   Error: {e}")

    print("\n" + "=" * 60)
    print("get_test_part test completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

