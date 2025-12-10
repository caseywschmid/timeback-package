"""API test for create_stimulus endpoint.

This script tests the create_stimulus endpoint against the QTI API.
Run with: python -m tests.api.qti.create_stimulus

Requires environment variables:
- TIMEBACK_CLIENT_ID
- TIMEBACK_CLIENT_SECRET
- TIMEBACK_ENVIRONMENT (production or staging)

WARNING: This test creates actual stimuli in the QTI API.
"""

import uuid
from timeback import Timeback
from timeback.models.request import TimebackCreateStimulusRequest


def main():
    """Test the create_stimulus endpoint."""
    client = Timeback()

    print("=" * 60)
    print("Testing create_stimulus endpoint")
    print("=" * 60)

    # Generate unique identifier to avoid conflicts
    unique_id = f"test-stimulus-{uuid.uuid4().hex[:8]}"

    # Basic creation with required fields only
    print(f"\n1. Creating stimulus with minimal fields (id: {unique_id}):")
    
    request = TimebackCreateStimulusRequest(
        identifier=unique_id,
        title="Test Stimulus - Created by API Test",
        content="""
        <div class="stimulus-content">
            <h2>Test Stimulus Content</h2>
            <p>This is a test stimulus created by the Timeback Python SDK API test.</p>
            <p>It demonstrates the basic creation functionality.</p>
        </div>
        """
    )
    
    try:
        response = client.qti.create_stimulus(request)
        print(f"   Created successfully!")
        print(f"     - Identifier: {response.identifier}")
        print(f"     - Title: {response.title}")
        print(f"     - Language: {response.language}")
        print(f"     - Created at: {response.created_at}")
        print(f"     - Raw XML length: {len(response.raw_xml)} chars")
    except Exception as e:
        print(f"   Error creating stimulus: {e}")
        return

    # Creation with metadata
    unique_id_2 = f"test-stimulus-meta-{uuid.uuid4().hex[:8]}"
    print(f"\n2. Creating stimulus with metadata (id: {unique_id_2}):")
    
    request_with_metadata = TimebackCreateStimulusRequest(
        identifier=unique_id_2,
        title="Test Stimulus with Metadata",
        content="""
        <div class="stimulus-content">
            <h2>Science Reading Passage</h2>
            <p>This stimulus includes custom metadata for curriculum alignment.</p>
        </div>
        """,
        label="Science Passage",
        language="en",
        metadata={
            "subject": "Science",
            "grade": "7",
            "standard": "NGSS",
            "createdBy": "API Test"
        },
        tool_name="Timeback Python SDK",
        tool_version="0.3.0"
    )
    
    try:
        response_meta = client.qti.create_stimulus(request_with_metadata)
        print(f"   Created successfully!")
        print(f"     - Identifier: {response_meta.identifier}")
        print(f"     - Title: {response_meta.title}")
        print(f"     - Label: {response_meta.label}")
        print(f"     - Tool: {response_meta.tool_name} v{response_meta.tool_version}")
        if response_meta.metadata:
            print(f"     - Metadata: {response_meta.metadata}")
    except Exception as e:
        print(f"   Error creating stimulus: {e}")

    # Verify creation by searching
    print("\n3. Verifying created stimuli by searching:")
    search_response = client.qti.search_stimuli()
    print(f"   Total stimuli in system: {search_response.total}")
    
    # Look for our created stimuli
    our_stimuli = [s for s in search_response.items if s.identifier in [unique_id, unique_id_2]]
    print(f"   Found {len(our_stimuli)} of our test stimuli")

    print("\n" + "=" * 60)
    print("create_stimulus tests completed!")
    print("=" * 60)
    print(f"\nNote: Created stimuli with IDs:")
    print(f"  - {unique_id}")
    print(f"  - {unique_id_2}")
    print("You may want to delete these test stimuli manually.")


if __name__ == "__main__":
    main()

