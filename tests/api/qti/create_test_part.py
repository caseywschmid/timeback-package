"""API test for create_test_part endpoint.

This script tests the create_test_part endpoint against the QTI API.
Run with: python -m tests.api.qti.create_test_part

Requires environment variables:
- TIMEBACK_CLIENT_ID
- TIMEBACK_CLIENT_SECRET
- TIMEBACK_ENVIRONMENT (production or staging)
"""

from timeback import Timeback
from timeback.models.request import (
    TimebackSearchAssessmentTestsRequest,
    TimebackCreateTestPartRequest,
)
from timeback.models.timeback_qti_section import TimebackQTISection
from timeback.enums import TimebackQTINavigationMode, TimebackQTISubmissionMode


def main():
    """Test the create_test_part endpoint."""
    client = Timeback()

    print("=" * 60)
    print("Testing create_test_part endpoint")
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

    # Create a test part
    print("\n2. Creating a new test part:")
    import uuid
    part_id = f"api-test-part-{uuid.uuid4().hex[:8]}"
    
    request = TimebackCreateTestPartRequest(
        identifier=part_id,
        navigation_mode=TimebackQTINavigationMode.LINEAR,
        submission_mode=TimebackQTISubmissionMode.INDIVIDUAL,
        qti_assessment_section=[
            TimebackQTISection(
                identifier=f"section-{uuid.uuid4().hex[:8]}",
                title="Test Section"
            )
        ]
    )
    
    try:
        result = client.qti.create_test_part(test.identifier, request)
        print(f"   Created: {result.identifier}")
        print(f"   Navigation: {result.navigation_mode.value}")
        print(f"   Submission: {result.submission_mode.value}")
        if result.qti_assessment_section:
            print(f"   Sections: {len(result.qti_assessment_section)}")
    except Exception as e:
        print(f"   Error: {e}")

    print("\n" + "=" * 60)
    print("create_test_part test completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

