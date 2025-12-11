"""API test for update_section endpoint.

This script tests the update_section endpoint against the QTI API.
Run with: python -m tests.api.qti.update_section

Requires environment variables:
- TIMEBACK_CLIENT_ID
- TIMEBACK_CLIENT_SECRET
- TIMEBACK_ENVIRONMENT (production or staging)
"""

from timeback import Timeback
from timeback.models.request import (
    TimebackSearchAssessmentTestsRequest,
    TimebackUpdateSectionRequest,
)


def main():
    """Test the update_section endpoint."""
    client = Timeback()

    print("=" * 60)
    print("Testing update_section endpoint")
    print("=" * 60)

    # Find a section to update
    print("\n1. Finding a section to update...")
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

    print(f"   Using: {test.identifier} / {part.identifier} / {section.identifier}")

    # Update the section
    print("\n2. Updating section:")
    try:
        request = TimebackUpdateSectionRequest(
            identifier=section.identifier,
            title=f"{section.title} - Updated",
            visible=section.visible
        )
        
        result = client.qti.update_section(
            test.identifier, part.identifier, section.identifier, request
        )
        print(f"   Updated: {result.identifier}")
        print(f"   Title: {result.title}")
    except Exception as e:
        print(f"   Error: {e}")

    print("\n" + "=" * 60)
    print("update_section test completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

