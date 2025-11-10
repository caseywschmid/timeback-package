from datetime import datetime
from typing import Optional, Dict, Any, List, Union
from pydantic import BaseModel, Field, field_validator
from timeback.enums import TimebackStatus
from timeback.models.timeback_user_id import TimebackUserId
from timeback.models.timeback_org_ref import TimebackOrgRef


class TimebackAgentForUser(BaseModel):
    """Simplified user model for agentFor endpoint response.

    This model matches the actual API response format which may:
    - Omit roles, agents, and userProfiles fields
    - Return primaryOrg as a string (sourcedId) instead of an object
    - Include additional fields like tenantId, clientAppId, identifier, isTestUser
    """

    # Required fields from API
    sourcedId: str = Field(..., description="Unique identifier")
    status: TimebackStatus = Field(
        default=TimebackStatus.ACTIVE, description="User's status"
    )
    enabledUser: bool = Field(..., description="Whether user has system access")
    givenName: str = Field(..., description="First name")
    familyName: str = Field(..., description="Last name")

    # Optional fields that may be omitted by this endpoint
    roles: Optional[List[Any]] = Field(
        None, description="User's roles and organizations"
    )
    agents: Optional[List[Any]] = Field(None, description="Related user references")
    userProfiles: Optional[List[Dict[str, Any]]] = Field(
        None, description="User profiles"
    )

    # Standard optional fields
    dateLastModified: Optional[str] = Field(
        None, description="Last modification timestamp"
    )
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    userMasterIdentifier: Optional[str] = Field(
        None, description="Master identifier across systems"
    )
    username: Optional[str] = Field(None, description="Legacy username")
    userIds: Optional[List[TimebackUserId]] = Field(
        None, description="External system identifiers"
    )
    middleName: Optional[str] = Field(None, description="Middle name")
    # primaryOrg can be a string (sourcedId) or a TimebackOrgRef object
    primaryOrg: Optional[Union[str, TimebackOrgRef]] = Field(
        None, description="Primary organization (may be sourcedId string or object)"
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

    # Additional fields specific to this endpoint response
    tenantId: Optional[str] = Field(None, description="Tenant identifier")
    clientAppId: Optional[str] = Field(
        None, description="Client application identifier"
    )
    identifier: Optional[str] = Field(None, description="User identifier")
    isTestUser: Optional[bool] = Field(None, description="Whether this is a test user")

    @field_validator("dateLastModified", mode="before")
    def convert_dateLastModified(cls, v):
        """Convert datetime dateLastModified to ISO string."""
        if isinstance(v, datetime):
            return v.isoformat() + "Z"
        return v


class TimebackGetAgentForResponse(BaseModel):
    """Response model for users that a given user is an agent for.

    Mirrors OneRoster response envelope for agentFor endpoint as documented in
    `timeback/docs/oneroster/rostering/get_agent_for.md`.
    """

    users: List[TimebackAgentForUser] = Field(
        ..., description="List of users this user is an agent for"
    )
