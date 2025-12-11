"""API test for create_section endpoint.

This script tests the create_section endpoint against the QTI API.
Run with: python -m tests.api.qti.create_section

Requires environment variables:
- TIMEBACK_CLIENT_ID
- TIMEBACK_CLIENT_SECRET
- TIMEBACK_ENVIRONMENT (production or staging)
"""

from timeback import Timeback
from timeback.models.request import (
    TimebackSearchAssessmentTestsRequest,
    TimebackCreateSectionRequest,
)
import uuid


def main():
    """Test the create_section endpoint."""
    client = Timeback()

    print("=" * 60)
    print("Testing create_section endpoint")
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

    # Create a section
    print("\n2. Creating a new section:")
    section_id = f"api-test-section-{uuid.uuid4().hex[:8]}"
    
    request = TimebackCreateSectionRequest(
        identifier=section_id,
        title="API Test Section",
        visible=True
    )
    
    try:
        result = client.qti.create_section(test.identifier, part.identifier, request)
        print(f"   Created: {result.identifier}")
        print(f"   Title: {result.title}")
        print(f"   Visible: {result.visible}")
    except Exception as e:
        print(f"   Error: {e}")

    print("\n" + "=" * 60)
    print("create_section test completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

