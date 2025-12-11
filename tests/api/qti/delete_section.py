"""API test for delete_section endpoint.

This script tests the delete_section endpoint against the QTI API.
Run with: python -m tests.api.qti.delete_section

WARNING: This test actually deletes sections! Use with caution.

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
    """Test the delete_section endpoint."""
    client = Timeback()

    print("=" * 60)
    print("Testing delete_section endpoint")
    print("=" * 60)

    # Find a test part
    print("\n1. Finding a test part...")
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

    if not part:
        print("   No test parts found.")
        return

    print(f"   Using test: {test.identifier}")
    print(f"   Using part: {part.identifier}")

    # Create a section to delete
    print("\n2. Creating a section to delete...")
    section_id = f"delete-test-{uuid.uuid4().hex[:8]}"
    
    try:
        create_request = TimebackCreateSectionRequest(
            identifier=section_id,
            title="Temporary Section"
        )
        created = client.qti.create_section(test.identifier, part.identifier, create_request)
        print(f"   Created: {created.identifier}")
    except Exception as e:
        print(f"   Error creating section: {e}")
        return

    # Delete the section
    print("\n3. Deleting section:")
    try:
        client.qti.delete_section(test.identifier, part.identifier, section_id)
        print(f"   Deleted: {section_id}")
    except Exception as e:
        print(f"   Error: {e}")

    # Verify deletion
    print("\n4. Verifying deletion:")
    try:
        client.qti.get_section(test.identifier, part.identifier, section_id)
        print("   ERROR: Section still exists!")
    except Exception as e:
        print(f"   Confirmed deleted (expected error: {type(e).__name__})")

    print("\n" + "=" * 60)
    print("delete_section test completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

