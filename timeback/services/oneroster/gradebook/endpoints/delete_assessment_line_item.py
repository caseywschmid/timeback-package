"""Delete Assessment Line Item endpoint for OneRoster Gradebook.

DELETE /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}
"""

from typing import Optional, Dict, Any
from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def delete_assessment_line_item(http: HttpClient, sourced_id: str) -> Optional[Dict[str, Any]]:
    """Soft delete an assessment line item (sets status to 'tobedeleted').

    DELETE /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}
    
    Returns:
        Optional[Dict[str, Any]]: Raw provider response (None for 204 No Content)
    """
    log.debug(f"Deleting assessment line item: {sourced_id}")
    return http.delete(f"/ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourced_id}")

