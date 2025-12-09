"""Request model for creating an academic session.

POST /ims/oneroster/rostering/v1p2/academicSessions
"""

from typing import Optional, Dict, Any, List
from uuid import uuid4
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus, TimebackAcademicSessionType
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class TimebackCreateAcademicSessionBody(BaseModel):
    """Body payload for academic session creation under the top-level 'academicSession' key.

    Attributes:
        Required:
            - title (str): The title of this academic session
            - type (TimebackAcademicSessionType): The type of session
            - startDate (str): When this session starts (ISO 8601 date)
            - endDate (str): When this session ends (ISO 8601 date)
            - schoolYear (str): The school year this session belongs to
            - org (TimebackSourcedIdReference): Reference to the organization

        Optional:
            - sourcedId (str, optional): Client-supplied sourcedId (auto-generated if omitted)
            - status (TimebackStatus, optional): Status. Defaults to "active".
            - metadata (Dict[str, Any], optional): Custom metadata
            - parent (TimebackSourcedIdReference, optional): Reference to parent academic session
            - children (List[TimebackSourcedIdReference], optional): References to child sessions
    """

    model_config = ConfigDict(populate_by_name=True)

    # Required fields
    title: str = Field(..., description="Title of the academic session")
    type: TimebackAcademicSessionType = Field(..., description="Type of session")
    startDate: str = Field(..., description="Start date (ISO 8601)")
    endDate: str = Field(..., description="End date (ISO 8601)")
    schoolYear: str = Field(..., description="School year")
    org: TimebackSourcedIdReference = Field(..., description="Reference to the organization")

    # Optional fields
    sourcedId: Optional[str] = Field(default_factory=lambda: str(uuid4()), description="Unique identifier")
    status: Optional[TimebackStatus] = Field(default=TimebackStatus.ACTIVE, description="Status")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    parent: Optional[TimebackSourcedIdReference] = Field(None, description="Reference to parent session")
    children: Optional[List[TimebackSourcedIdReference]] = Field(None, description="References to child sessions")


class TimebackCreateAcademicSessionRequest(BaseModel):
    """Top-level request wrapper for POST /academicSessions."""

    model_config = ConfigDict(populate_by_name=True)
    academicSession: TimebackCreateAcademicSessionBody = Field(..., description="Academic session data to create")

