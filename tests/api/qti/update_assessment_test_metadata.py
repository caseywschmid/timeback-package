"""API test for update_assessment_test_metadata endpoint.

This script tests the update_assessment_test_metadata endpoint against the QTI API.
Run with: python -m tests.api.qti.update_assessment_test_metadata

Requires environment variables:
- TIMEBACK_CLIENT_ID
- TIMEBACK_CLIENT_SECRET
- TIMEBACK_ENVIRONMENT (production or staging)
"""

from timeback import Timeback
from timeback.models.request import (
    TimebackSearchAssessmentTestsRequest,
    TimebackUpdateAssessmentTestMetadataRequest,
)


def main():
    """Test the update_assessment_test_metadata endpoint."""
    client = Timeback()

    print("=" * 60)
    print("Testing update_assessment_test_metadata endpoint")
    print("=" * 60)

    # First, find an assessment test to update
    print("\n1. Finding an assessment test...")
    search_response = client.qti.search_assessment_tests(
        TimebackSearchAssessmentTestsRequest(limit=5)
    )
    
    if not search_response.items:
        print("   No assessment tests found. Create one first.")
        return

    # Use the first test
    test = search_response.items[0]
    print(f"   Using test: {test.identifier} - {test.title}")
    if test.metadata:
        print(f"   Current metadata: {test.metadata}")

    # Update metadata
    print("\n2. Updating test metadata:")
    request = TimebackUpdateAssessmentTestMetadataRequest(
        metadata={
            "subject": "Mathematics",
            "grade": "7",
            "description": "Updated via API test"
        }
    )
    
    try:
        result = client.qti.update_assessment_test_metadata(test.identifier, request)
        print(f"   Updated: {result.identifier}")
        print(f"   Title: {result.title}")
        if result.metadata:
            print(f"   New metadata: {result.metadata}")
    except Exception as e:
        print(f"   Error: {e}")

    print("\n" + "=" * 60)
    print("update_assessment_test_metadata test completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

