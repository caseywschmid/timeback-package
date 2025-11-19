"""User models for the TimeBack API.

This module defines the data models for users following the OneRoster v1.2 specification
with our simplified reference handling.

API Endpoints:
- GET /users - List users
- GET /users/{id} - Get a specific user
- POST /users - Create a new user
- PUT /users/{id} - Update a user
- DELETE /users/{id} - Delete a user (sets status to tobedeleted)
"""

from datetime import datetime
from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field, field_validator
from timeback.enums import (
    TimebackStatus,
)
from .timeback_user_role import TimebackUserRole
from .timeback_user_id import TimebackUserId
from .timeback_agent_ref import TimebackAgentRef
from .timeback_org_ref import TimebackOrgRef


class TimebackUser(BaseModel):
    """OneRoster User model with simplified reference handling.

    Required Fields (when full response is returned):
    - sourcedId: Unique identifier
    - givenName: First name
    - familyName: Last name

    Optional Fields (may be missing when using `fields` query parameter):
    - status: active or tobedeleted (defaults to ACTIVE if not provided)
    - enabledUser: Whether user has system access
    - roles: List of role assignments
    - dateLastModified: Last modification timestamp

    Note: When using the `fields` query parameter, the API returns only the requested fields.
    Fields like `enabledUser`, `roles`, and `dateLastModified` may be missing in partial responses.
    Always check for None before accessing these fields when field filtering is used.
    """

    # Always required
    sourcedId: str = Field(..., description="Unique identifier")
    givenName: str = Field(..., description="First name")
    familyName: str = Field(..., description="Last name")
    
    # Optional - may be missing when fields parameter is used
    status: Optional[TimebackStatus] = Field(
        default=TimebackStatus.ACTIVE, description="User's status"
    )
    enabledUser: Optional[bool] = Field(None, description="Whether user has system access")
    roles: Optional[List[TimebackUserRole]] = Field(
        None, description="User's roles and organizations"
    )
    # Optional per schema
    agents: Optional[List[TimebackAgentRef]] = Field(
        None, description="Related user references"
    )
    # Not defined in OneRoster User schema; keep optional if present in provider responses
    userProfiles: Optional[List[Dict[str, Any]]] = Field(
        None, description="User profiles"
    )

    # Optional - may be missing when fields parameter is used
    dateLastModified: Optional[str] = Field(
        None, description="Last modification timestamp (ISO datetime with UTC timezone)"
    )
    # Optional fields
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    userMasterIdentifier: Optional[str] = Field(
        None, description="Master identifier across systems"
    )
    username: Optional[str] = Field(None, description="Legacy username")
    userIds: Optional[List[TimebackUserId]] = Field(
        None, description="External system identifiers"
    )
    middleName: Optional[str] = Field(None, description="Middle name")
    primaryOrg: Optional[TimebackOrgRef] = Field(
        None, description="Primary organization"
    )
    email: Optional[str] = Field(None, description="Email address")
    preferredFirstName: Optional[str] = Field(None, description="Preferred first name")
    preferredMiddleName: Optional[str] = Field(
        None, description="Preferred middle name"
    )
    preferredLastName: Optional[str] = Field(None, description="Preferred last name")
    pronouns: Optional[str] = Field(None, description="Preferred pronouns")
    grades: Optional[List[str]] = Field(None, description="Grade levels")
    password: Optional[str] = Field(None, description="User password")
    sms: Optional[str] = Field(None, description="SMS number")
    phone: Optional[str] = Field(None, description="Phone number")


    @field_validator("dateLastModified", mode="before")
    def convert_dateLastModified(cls, v):
        """Convert datetime dateLastModified to ISO string."""
        if isinstance(v, datetime):
            return v.isoformat() + "Z"
        return v

    def to_dict(self) -> Dict[str, Any]:
        """Convert model to dictionary for API requests."""
        data = self.model_dump(exclude_none=True)

        # Set dateLastModified if not provided
        if not self.dateLastModified:
            data["dateLastModified"] = datetime.utcnow().isoformat() + "Z"

        return {"user": data}

    def to_create_dict(self) -> Dict[str, Any]:
        """Convert model to dict for POST operations."""
        return self.to_dict()

    def to_update_dict(self) -> Dict[str, Any]:
        """Convert model to dict for PUT operations."""
        return self.to_dict()
