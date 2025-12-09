"""Request model for updating an academic session (PUT).

PUT /ims/oneroster/rostering/v1p2/academicSessions/{sourcedId}
"""

from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus, TimebackAcademicSessionType
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class TimebackUpdateAcademicSessionBody(BaseModel):
    """Body payload for academic session update under the top-level 'academicSession' key."""

    model_config = ConfigDict(populate_by_name=True)

    # Optional fields for update
    sourcedId: Optional[str] = Field(None, description="Unique identifier (should match path)")
    status: Optional[TimebackStatus] = Field(None, description="Status")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    title: Optional[str] = Field(None, description="Title of the academic session")
    type: Optional[TimebackAcademicSessionType] = Field(None, description="Type of session")
    startDate: Optional[str] = Field(None, description="Start date (ISO 8601)")
    endDate: Optional[str] = Field(None, description="End date (ISO 8601)")
    schoolYear: Optional[str] = Field(None, description="School year")
    org: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to the organization")
    parent: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to parent session")
    children: Optional[List[TimebackSourcedIdReference]] = Field(None, description="References to child sessions")


class TimebackUpdateAcademicSessionRequest(BaseModel):
    """Top-level request wrapper for PUT /academicSessions/{sourcedId}."""

    model_config = ConfigDict(populate_by_name=True)

    sourced_id: str = Field(..., description="The sourcedId of the academic session (path parameter)")
    academicSession: TimebackUpdateAcademicSessionBody = Field(..., description="Academic session data to update")

