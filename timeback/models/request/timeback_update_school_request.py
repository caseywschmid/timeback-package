"""Request model for updating a OneRoster School.

This request mirrors the body for:
- PUT /ims/oneroster/rostering/v1p2/schools/{sourcedId}

The payload follows the OneRoster v1.2 spec with Timeback enums/models.
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, field_validator

from timeback.enums import TimebackStatus, TimebackOrgType
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class TimebackUpdateSchoolBody(BaseModel):
    """Body payload for school update under the top-level 'org' key.
    
    Attributes:
        Required:
            - sourcedId (str): School sourcedId (used in path and body)
            - name (str): Name of the school
            - type (TimebackOrgType): Must be TimebackOrgType.SCHOOL ("school")
        
        Optional:
            - status (TimebackStatus, optional): School status. See TimebackStatus enum.
            - metadata (Dict[str, Any], optional): Custom metadata
            - identifier (str, optional): External identifier for the school
            - parent (TimebackSourcedIdReference, optional): Reference to parent organization.
              See TimebackSourcedIdReference for structure.
    """

    # Required fields per spec
    sourcedId: str = Field(..., description="School sourcedId (used in path and body)")
    name: str = Field(..., description="Name of the school")
    type: TimebackOrgType = Field(..., description="Type must be 'school'")

    # Optional fields
    status: Optional[TimebackStatus] = Field(None, description="School status")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    identifier: Optional[str] = Field(None, description="External identifier")
    parent: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to parent organization")

    @field_validator("type", mode="before")
    @classmethod
    def validate_type(cls, v):
        """Ensure type is 'school'."""
        if isinstance(v, str) and v != "school":
            raise ValueError("Type must be 'school' for school update")
        if isinstance(v, TimebackOrgType) and v != TimebackOrgType.SCHOOL:
            raise ValueError("Type must be TimebackOrgType.SCHOOL for school update")
        return TimebackOrgType.SCHOOL


class TimebackUpdateSchoolRequest(BaseModel):
    """Top-level request wrapper for PUT /schools/{sourcedId}.
    
    Attributes:
        Required:
            - org (TimebackUpdateSchoolBody): School data to update. See TimebackUpdateSchoolBody for structure.
    """
    
    org: TimebackUpdateSchoolBody

