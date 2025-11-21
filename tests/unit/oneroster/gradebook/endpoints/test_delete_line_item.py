from typing import Optional, Dict, Any
from timeback.services.oneroster.gradebook.endpoints.delete_line_item import (
    delete_line_item,
)
from timeback.models.request import TimebackDeleteLineItemRequest


class MockHttp:
    def delete(self, path) -> Optional[Dict[str, Any]]:
        assert path.startswith("/ims/oneroster/gradebook/v1p2/lineItems/")
        # Simulate HTTP 204 No Content response
        return None


def test_delete_line_item_success():
    """Test successful line item deletion."""
    request = TimebackDeleteLineItemRequest(sourced_id="line-item-123")
    result = delete_line_item(MockHttp(), request)
    
    # DELETE returns None for 204 No Content
    assert result is None


def test_delete_line_item_with_different_id():
    """Test line item deletion with different sourcedId."""
    request = TimebackDeleteLineItemRequest(sourced_id="line-item-456")
    result = delete_line_item(MockHttp(), request)
    
    # DELETE returns None for 204 No Content
    assert result is None

