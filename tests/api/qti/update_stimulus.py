"""API test for update_stimulus endpoint.

This script tests the update_stimulus endpoint against the QTI API.
Run with: python -m tests.api.qti.update_stimulus

Requires environment variables:
- TIMEBACK_CLIENT_ID
- TIMEBACK_CLIENT_SECRET
- TIMEBACK_ENVIRONMENT (production or staging)

WARNING: This test modifies an existing stimulus in the QTI API.
"""

from timeback import Timeback
from timeback.models.request import TimebackUpdateStimulusRequest


def main():
    """Test the update_stimulus endpoint."""
    client = Timeback()

    print("=" * 60)
    print("Testing update_stimulus endpoint")
    print("=" * 60)

    # First, get a stimulus to update
    print("\n1. Finding a stimulus to update:")
    search_response = client.qti.search_stimuli()
    
    if not search_response.items:
        print("   No stimuli found. Please create a stimulus first.")
        return

    # Find a test stimulus or use the first one
    target_stimulus = None
    for stimulus in search_response.items:
        if stimulus.identifier.startswith("test-stimulus"):
            target_stimulus = stimulus
            break
    
    if not target_stimulus:
        target_stimulus = search_response.items[0]
        print(f"   Warning: Using non-test stimulus: {target_stimulus.identifier}")
        print("   Consider creating a test stimulus first to avoid modifying real data.")
    
    identifier = target_stimulus.identifier
    original_title = target_stimulus.title
    print(f"   Found stimulus: {identifier}")
    print(f"   Original title: {original_title}")

    # Update the stimulus with new content
    print(f"\n2. Updating stimulus: {identifier}")
    
    new_title = f"{original_title} (Updated)"
    request = TimebackUpdateStimulusRequest(
        identifier=identifier,
        title=new_title,
        content="""
        <div class="stimulus-content">
            <h2>Updated Stimulus Content</h2>
            <p>This stimulus has been updated by the API test.</p>
            <p>Original title was: """ + original_title + """</p>
        </div>
        """,
        metadata={
            "updatedBy": "API Test",
            "updateReason": "Testing update_stimulus endpoint"
        }
    )
    
    try:
        response = client.qti.update_stimulus(request)
        print(f"   Updated successfully!")
        print(f"     - Identifier: {response.identifier}")
        print(f"     - New title: {response.title}")
        print(f"     - Updated at: {response.updated_at}")
        print(f"     - Raw XML length: {len(response.raw_xml)} chars")
    except Exception as e:
        print(f"   Error updating stimulus: {e}")
        return

    # Verify by fetching the stimulus
    print("\n3. Verifying update by fetching stimulus:")
    try:
        verified = client.qti.get_stimulus(identifier)
        print(f"   Title matches: {verified.title == new_title}")
        if verified.metadata:
            print(f"   Metadata updated: {verified.metadata.get('updatedBy') == 'API Test'}")
    except Exception as e:
        print(f"   Error verifying: {e}")

    # Restore original title (optional cleanup)
    print("\n4. Restoring original title:")
    try:
        restore_request = TimebackUpdateStimulusRequest(
            identifier=identifier,
            title=original_title,
            content=response.raw_xml.split("<qti-stimulus-body>")[1].split("</qti-stimulus-body>")[0] if "<qti-stimulus-body>" in response.raw_xml else "<div>Content</div>"
        )
        # Note: This may not perfectly restore the original content
        # restored = client.qti.update_stimulus(restore_request)
        print("   Skipping restoration to preserve test update.")
    except Exception as e:
        print(f"   Could not restore: {e}")

    print("\n" + "=" * 60)
    print("update_stimulus tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

