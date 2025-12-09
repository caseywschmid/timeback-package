"""Request model for creating a OneRoster Class.

POST /ims/oneroster/rostering/v1p2/classes

Note: We use separate models (TimebackCreateClassBody) instead of reusing TimebackClass because:
1. The API spec for creation only requires sourcedId references (not full refs with href/type)
2. We need to exclude dateLastModified that shouldn't be sent on creation
3. We want to enforce validation specific to creation
"""

from typing import Any, Dict, Optional, List
from pydantic import BaseModel, Field, ConfigDict
from uuid import uuid4
from timeback.enums import TimebackStatus, TimebackClassType
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class TimebackCreateClassBody(BaseModel):
    """Body payload for class creation under the top-level 'class' key.
    
    Attributes:
        Required:
            - title (str): Title/name of the class
            - course (TimebackSourcedIdReference): Reference to the parent course. See TimebackSourcedIdReference for structure.
            - org (TimebackSourcedIdReference): Reference to the organization/school. See TimebackSourcedIdReference for structure.
            - terms (List[TimebackSourcedIdReference]): References to academic terms/sessions. See TimebackSourcedIdReference for structure.
        
        Optional:
            - sourcedId (str, optional): Client-supplied sourcedId (auto-generated UUID if omitted)
            - status (TimebackStatus, optional): Class status. Defaults to "active". See TimebackStatus enum.
            - metadata (Dict[str, Any], optional): Custom metadata
            - classCode (str, optional): Class code identifier
            - classType (TimebackClassType, optional): Type of class - "homeroom" or "scheduled". See TimebackClassType enum.
            - location (str, optional): Physical location of the class
            - grades (List[str], optional): List of grade levels (e.g., ["9", "10", "11", "12"])
            - subjects (List[str], optional): List of subjects (e.g., ["Math", "Science"])
            - subjectCodes (List[str], optional): List of subject codes
            - periods (List[str], optional): List of class periods
            - resources (List[TimebackSourcedIdReference], optional): References to learning resources. See TimebackSourcedIdReference for structure.
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    # Optional client-supplied sourcedId; if omitted, auto-generate a UUID string
    sourcedId: Optional[str] = Field(default_factory=lambda: str(uuid4()), description="Client-supplied sourcedId (auto-generated UUID if omitted)")
    
    # Required fields per spec
    title: str = Field(..., description="Title/name of the class")
    course: TimebackSourcedIdReference = Field(..., description="Reference to the parent course")
    org: TimebackSourcedIdReference = Field(..., description="Reference to the organization/school")
    terms: List[TimebackSourcedIdReference] = Field(..., description="References to academic terms/sessions")
    
    # Optional fields
    status: Optional[TimebackStatus] = Field(default=TimebackStatus.ACTIVE, description="Class status")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    classCode: Optional[str] = Field(None, description="Class code identifier")
    classType: Optional[TimebackClassType] = Field(None, description="Type of class - 'homeroom' or 'scheduled'")
    location: Optional[str] = Field(None, description="Physical location of the class")
    grades: Optional[List[str]] = Field(None, description="List of grade levels")
    subjects: Optional[List[str]] = Field(None, description="List of subjects")
    subjectCodes: Optional[List[str]] = Field(None, description="List of subject codes")
    periods: Optional[List[str]] = Field(None, description="List of class periods")
    resources: Optional[List[TimebackSourcedIdReference]] = Field(None, description="References to learning resources")


class TimebackCreateClassRequest(BaseModel):
    """Top-level request wrapper for POST /classes.
    
    Attributes:
        Required:
            - class_ (TimebackCreateClassBody): Class data to create. See TimebackCreateClassBody for structure.
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    class_: TimebackCreateClassBody = Field(..., alias="class", description="Class data to create")

