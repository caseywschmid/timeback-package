"""API test for delete_stimulus endpoint.

This script tests the delete_stimulus endpoint against the QTI API.
Run with: python -m tests.api.qti.delete_stimulus

Requires environment variables:
- TIMEBACK_CLIENT_ID
- TIMEBACK_CLIENT_SECRET
- TIMEBACK_ENVIRONMENT (production or staging)

WARNING: This test DELETES a stimulus permanently!
"""

import uuid
from timeback import Timeback
from timeback.models.request import TimebackCreateStimulusRequest


def main():
    """Test the delete_stimulus endpoint."""
    client = Timeback()

    print("=" * 60)
    print("Testing delete_stimulus endpoint")
    print("=" * 60)

    # First, create a stimulus specifically for deletion testing
    unique_id = f"test-delete-{uuid.uuid4().hex[:8]}"
    print(f"\n1. Creating a stimulus for deletion test (id: {unique_id}):")
    
    create_request = TimebackCreateStimulusRequest(
        identifier=unique_id,
        title="Test Stimulus for Deletion",
        content="<div>This stimulus will be deleted</div>",
        metadata={"purpose": "deletion test"}
    )
    
    try:
        created = client.qti.create_stimulus(create_request)
        print(f"   Created stimulus: {created.identifier}")
    except Exception as e:
        print(f"   Error creating stimulus: {e}")
        return

    # Verify it exists
    print(f"\n2. Verifying stimulus exists:")
    try:
        verified = client.qti.get_stimulus(unique_id)
        print(f"   Found: {verified.identifier} - {verified.title}")
    except Exception as e:
        print(f"   Error: {e}")
        return

    # Delete the stimulus
    print(f"\n3. Deleting stimulus: {unique_id}")
    try:
        client.qti.delete_stimulus(unique_id)
        print("   Deleted successfully (no error returned)")
    except Exception as e:
        print(f"   Error deleting stimulus: {e}")
        return

    # Verify deletion
    print(f"\n4. Verifying stimulus is deleted:")
    try:
        client.qti.get_stimulus(unique_id)
        print("   ERROR: Stimulus still exists!")
    except Exception as e:
        print(f"   Confirmed deleted (get returned error as expected)")

    print("\n" + "=" * 60)
    print("delete_stimulus tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

