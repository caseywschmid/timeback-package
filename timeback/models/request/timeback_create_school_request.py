"""Request model for creating a OneRoster School.

POST /ims/oneroster/rostering/v1p2/schools

Note: We use separate models (TimebackCreateSchoolBody) instead of reusing TimebackOrg because:
1. The API spec for creation only requires parent.sourcedId (not the full TimebackOrgRef with type field)
2. We need to exclude dateLastModified and children fields that shouldn't be sent on creation
3. We want to enforce type='school' validation specific to creation
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, field_validator
from uuid import uuid4
from timeback.enums import TimebackStatus, TimebackOrgType
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class TimebackCreateSchoolBody(BaseModel):
    """Body payload for school creation under the top-level 'org' key.
    
    Attributes:
        Required:
            - name (str): Name of the school
            - type (TimebackOrgType): Must be TimebackOrgType.SCHOOL ("school")
        
        Optional:
            - sourcedId (str, optional): Client-supplied sourcedId (auto-generated UUID if omitted)
            - status (TimebackStatus, optional): School status. Defaults to "active". See TimebackStatus enum.
            - metadata (Dict[str, Any], optional): Custom metadata
            - identifier (str, optional): External identifier for the school
            - parent (TimebackSourcedIdReference, optional): Reference to parent organization. See TimebackSourcedIdReference for structure.
    """
    
    # Optional client-supplied sourcedId; if omitted, auto-generate a UUID string
    sourcedId: Optional[str] = Field(default_factory=lambda: str(uuid4()))
    name: str = Field(..., description="Name of the school")
    type: TimebackOrgType = Field(default=TimebackOrgType.SCHOOL, description="Type must be 'school'")
    status: Optional[TimebackStatus] = Field(default=TimebackStatus.ACTIVE, description="School status")
    metadata: Optional[Dict[str, Any]] = None
    identifier: Optional[str] = None
    parent: Optional[TimebackSourcedIdReference] = None

    @field_validator("type", mode="before")
    @classmethod
    def validate_type(cls, v):
        """Ensure type is 'school'."""
        if isinstance(v, str) and v != "school":
            raise ValueError("Type must be 'school' for school creation")
        if isinstance(v, TimebackOrgType) and v != TimebackOrgType.SCHOOL:
            raise ValueError("Type must be TimebackOrgType.SCHOOL for school creation")
        return TimebackOrgType.SCHOOL


class TimebackCreateSchoolRequest(BaseModel):
    """Top-level request wrapper for POST /schools.
    
    Attributes:
        Required:
            - org (TimebackCreateSchoolBody): School data to create. See TimebackCreateSchoolBody for structure.
    """
    
    org: TimebackCreateSchoolBody

