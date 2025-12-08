"""Request model for updating a resource.

PUT /ims/oneroster/resources/v1p2/resources/{sourcedId}
"""

from typing import Any, Dict, Optional, List
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus, TimebackImportance, TimebackRoleType


class TimebackUpdateResourceBody(BaseModel):
    """Body payload for resource update under 'resource' key."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    sourcedId: Optional[str] = Field(None, description="Unique identifier (should match path)")
    status: Optional[TimebackStatus] = Field(default=TimebackStatus.ACTIVE, description="Status")
    title: str = Field(..., description="Resource title")
    vendorResourceId: str = Field(..., description="Vendor resource ID")
    importance: TimebackImportance = Field(..., description="Resource importance")
    roles: Optional[List[TimebackRoleType]] = Field(default_factory=list, description="Applicable roles")
    vendorId: Optional[str] = Field(None, description="Vendor ID")
    applicationId: Optional[str] = Field(None, description="Application ID")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")


class TimebackUpdateResourceRequest(BaseModel):
    """Request model for PUT /resources/{sourcedId}."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    sourced_id: str = Field(..., description="The sourcedId (path parameter)")
    resource: TimebackUpdateResourceBody = Field(..., description="Resource data")

