"""Request model for creating a resource.

POST /ims/oneroster/resources/v1p2/resources
"""

from typing import Any, Dict, Optional, List
from pydantic import BaseModel, Field, ConfigDict
from uuid import uuid4
from timeback.enums import TimebackStatus, TimebackImportance, TimebackRoleType


class TimebackCreateResourceBody(BaseModel):
    """Body payload for resource creation under 'resource' key."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    sourcedId: Optional[str] = Field(default_factory=lambda: str(uuid4()), description="Unique identifier")
    status: Optional[TimebackStatus] = Field(default=TimebackStatus.ACTIVE, description="Status")
    title: str = Field(..., description="Resource title")
    vendorResourceId: str = Field(..., description="Vendor resource ID")
    importance: TimebackImportance = Field(..., description="Resource importance")
    roles: Optional[List[TimebackRoleType]] = Field(default_factory=list, description="Applicable roles")
    vendorId: Optional[str] = Field(None, description="Vendor ID")
    applicationId: Optional[str] = Field(None, description="Application ID")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")


class TimebackCreateResourceRequest(BaseModel):
    """Top-level request wrapper for POST /resources."""
    
    resource: TimebackCreateResourceBody

