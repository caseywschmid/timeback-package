"""API test for get_stimulus endpoint.

This script tests the get_stimulus endpoint against the QTI API.
Run with: python -m tests.api.qti.get_stimulus

Requires environment variables:
- TIMEBACK_CLIENT_ID
- TIMEBACK_CLIENT_SECRET
- TIMEBACK_ENVIRONMENT (production or staging)
"""

from timeback import Timeback


def main():
    """Test the get_stimulus endpoint."""
    client = Timeback()

    print("=" * 60)
    print("Testing get_stimulus endpoint")
    print("=" * 60)

    # First, get a list of stimuli to find an identifier to fetch
    print("\n1. Getting list of stimuli to find an identifier:")
    search_response = client.qti.search_stimuli()
    
    if not search_response.items:
        print("   No stimuli found in the system. Cannot test get_stimulus.")
        print("   Please create a stimulus first using create_stimulus.")
        return

    first_stimulus = search_response.items[0]
    identifier = first_stimulus.identifier
    print(f"   Found {search_response.total} stimuli")
    print(f"   Using identifier: {identifier}")

    # Get the specific stimulus
    print(f"\n2. Getting stimulus by identifier: {identifier}")
    try:
        stimulus = client.qti.get_stimulus(identifier)
        print(f"   Retrieved successfully!")
        print(f"     - Identifier: {stimulus.identifier}")
        print(f"     - Title: {stimulus.title}")
        print(f"     - Language: {stimulus.language}")
        print(f"     - Label: {stimulus.label or '(none)'}")
        print(f"     - Created: {stimulus.created_at}")
        print(f"     - Updated: {stimulus.updated_at}")
        print(f"     - Raw XML length: {len(stimulus.raw_xml)} chars")
        
        if stimulus.stylesheet:
            print(f"     - Stylesheet: {stimulus.stylesheet.href}")
        
        if stimulus.catalog_info:
            print(f"     - Catalog entries: {len(stimulus.catalog_info)}")
        
        if stimulus.metadata:
            print(f"     - Metadata keys: {list(stimulus.metadata.keys())}")
        
        if stimulus.tool_name:
            print(f"     - Tool: {stimulus.tool_name} v{stimulus.tool_version or '?'}")
            
    except Exception as e:
        print(f"   Error getting stimulus: {e}")
        return

    # Show a preview of the raw XML
    print("\n3. Raw XML preview (first 500 chars):")
    xml_preview = stimulus.raw_xml[:500] if len(stimulus.raw_xml) > 500 else stimulus.raw_xml
    print(f"   {xml_preview}...")

    print("\n" + "=" * 60)
    print("get_stimulus tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

