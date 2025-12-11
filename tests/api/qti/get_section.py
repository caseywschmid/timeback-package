"""API test for get_section endpoint.

This script tests the get_section endpoint against the QTI API.
Run with: python -m tests.api.qti.get_section

Requires environment variables:
- TIMEBACK_CLIENT_ID
- TIMEBACK_CLIENT_SECRET
- TIMEBACK_ENVIRONMENT (production or staging)
"""

from timeback import Timeback
from timeback.models.request import TimebackSearchAssessmentTestsRequest


def main():
    """Test the get_section endpoint."""
    client = Timeback()

    print("=" * 60)
    print("Testing get_section endpoint")
    print("=" * 60)

    # Find an assessment test with test parts and sections
    print("\n1. Finding an assessment test with sections...")
    search_response = client.qti.search_assessment_tests(
        TimebackSearchAssessmentTestsRequest(limit=5)
    )
    
    if not search_response.items:
        print("   No assessment tests found.")
        return

    test = None
    part = None
    section = None
    for t in search_response.items:
        parts = client.qti.search_test_parts(t.identifier)
        for p in parts.items:
            sections = client.qti.search_sections(t.identifier, p.identifier)
            if sections.items:
                test = t
                part = p
                section = sections.items[0]
                break
        if section:
            break

    if not section:
        print("   No sections found.")
        return

    print(f"   Using test: {test.identifier}")
    print(f"   Using part: {part.identifier}")
    print(f"   Using section: {section.identifier}")

    # Get the section
    print("\n2. Getting section details:")
    try:
        result = client.qti.get_section(test.identifier, part.identifier, section.identifier)
        
        print(f"   Identifier: {result.identifier}")
        print(f"   Title: {result.title}")
        print(f"   Visible: {result.visible}")
        if result.qti_assessment_item_ref:
            print(f"   Items: {len(result.qti_assessment_item_ref)}")
            for item in result.qti_assessment_item_ref[:3]:
                print(f"     - {item.identifier}")
    except Exception as e:
        print(f"   Error: {e}")

    print("\n" + "=" * 60)
    print("get_section test completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

