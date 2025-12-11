"""API test for update_test_part endpoint.

This script tests the update_test_part endpoint against the QTI API.
Run with: python -m tests.api.qti.update_test_part

Requires environment variables:
- TIMEBACK_CLIENT_ID
- TIMEBACK_CLIENT_SECRET
- TIMEBACK_ENVIRONMENT (production or staging)
"""

from timeback import Timeback
from timeback.models.request import (
    TimebackSearchAssessmentTestsRequest,
    TimebackUpdateTestPartRequest,
)
from timeback.models.timeback_qti_section import TimebackQTISection
from timeback.enums import TimebackQTINavigationMode, TimebackQTISubmissionMode


def main():
    """Test the update_test_part endpoint."""
    client = Timeback()

    print("=" * 60)
    print("Testing update_test_part endpoint")
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

    # Update the test part
    print("\n2. Updating test part:")
    try:
        # Get current sections or create new ones
        sections = part.qti_assessment_section or []
        if not sections:
            sections = [TimebackQTISection(identifier="section-001", title="New Section")]
        
        request = TimebackUpdateTestPartRequest(
            identifier=part.identifier,
            navigation_mode=TimebackQTINavigationMode.NONLINEAR,
            submission_mode=TimebackQTISubmissionMode.SIMULTANEOUS,
            qti_assessment_section=sections
        )
        
        result = client.qti.update_test_part(test.identifier, part.identifier, request)
        print(f"   Updated: {result.identifier}")
        print(f"   Navigation: {result.navigation_mode.value}")
        print(f"   Submission: {result.submission_mode.value}")
    except Exception as e:
        print(f"   Error: {e}")

    print("\n" + "=" * 60)
    print("update_test_part test completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

