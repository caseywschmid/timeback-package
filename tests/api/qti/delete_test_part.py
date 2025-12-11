"""API test for delete_test_part endpoint.

This script tests the delete_test_part endpoint against the QTI API.
Run with: python -m tests.api.qti.delete_test_part

WARNING: This test actually deletes test parts! Use with caution.

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
import uuid


def main():
    """Test the delete_test_part endpoint."""
    client = Timeback()

    print("=" * 60)
    print("Testing delete_test_part endpoint")
    print("=" * 60)

    # First, find an assessment test
    print("\n1. Finding an assessment test...")
    search_response = client.qti.search_assessment_tests(
        TimebackSearchAssessmentTestsRequest(limit=5)
    )
    
    if not search_response.items:
        print("   No assessment tests found.")
        return

    test = search_response.items[0]
    print(f"   Using test: {test.identifier}")

    # Create a test part to delete
    print("\n2. Creating a test part to delete...")
    part_id = f"delete-test-{uuid.uuid4().hex[:8]}"
    
    try:
        create_request = TimebackCreateTestPartRequest(
            identifier=part_id,
            navigation_mode=TimebackQTINavigationMode.LINEAR,
            submission_mode=TimebackQTISubmissionMode.INDIVIDUAL,
            qti_assessment_section=[
                TimebackQTISection(
                    identifier=f"section-{uuid.uuid4().hex[:8]}",
                    title="Temporary Section"
                )
            ]
        )
        created = client.qti.create_test_part(test.identifier, create_request)
        print(f"   Created: {created.identifier}")
    except Exception as e:
        print(f"   Error creating test part: {e}")
        return

    # Delete the test part
    print("\n3. Deleting test part:")
    try:
        client.qti.delete_test_part(test.identifier, part_id)
        print(f"   Deleted: {part_id}")
    except Exception as e:
        print(f"   Error: {e}")

    # Verify deletion
    print("\n4. Verifying deletion:")
    try:
        client.qti.get_test_part(test.identifier, part_id)
        print("   ERROR: Test part still exists!")
    except Exception as e:
        print(f"   Confirmed deleted (expected error: {type(e).__name__})")

    print("\n" + "=" * 60)
    print("delete_test_part test completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

