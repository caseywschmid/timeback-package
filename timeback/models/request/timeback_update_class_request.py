"""Request model for updating a OneRoster Class.

This request mirrors the body for:
- PUT /ims/oneroster/rostering/v1p2/classes/{sourcedId}

The payload follows the OneRoster v1.2 spec with Timeback enums/models.
"""

from typing import Any, Dict, Optional, List
from pydantic import BaseModel, Field, ConfigDict

from timeback.enums import TimebackStatus, TimebackClassType
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class TimebackUpdateClassBody(BaseModel):
    """Body payload for class update under the top-level 'class' key.
    
    Attributes:
        Required:
            - sourcedId (str): Class sourcedId (used in path and body)
        
        Optional:
            - status (TimebackStatus, optional): Class status. See TimebackStatus enum.
            - metadata (Dict[str, Any], optional): Custom metadata
            - title (str, optional): Title/name of the class
            - classCode (str, optional): Class code identifier
            - classType (TimebackClassType, optional): Type of class - "homeroom" or "scheduled". See TimebackClassType enum.
            - location (str, optional): Physical location of the class
            - grades (List[str], optional): List of grade levels (e.g., ["9", "10", "11", "12"])
            - subjects (List[str], optional): List of subjects (e.g., ["Math", "Science"])
            - subjectCodes (List[str], optional): List of subject codes
            - periods (List[str], optional): List of class periods
            - resources (List[TimebackSourcedIdReference], optional): References to learning resources. See TimebackSourcedIdReference for structure.
            - terms (List[TimebackSourcedIdReference], optional): References to academic terms. See TimebackSourcedIdReference for structure.
    """
    
    model_config = ConfigDict(populate_by_name=True)

    # Required field - used in path and body
    sourcedId: str = Field(..., description="Class sourcedId (used in path and body)")

    # Optional fields - only include what needs to be updated
    status: Optional[TimebackStatus] = Field(None, description="Class status")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    title: Optional[str] = Field(None, description="Title/name of the class")
    classCode: Optional[str] = Field(None, description="Class code identifier")
    classType: Optional[TimebackClassType] = Field(None, description="Type of class - 'homeroom' or 'scheduled'")
    location: Optional[str] = Field(None, description="Physical location of the class")
    grades: Optional[List[str]] = Field(None, description="List of grade levels")
    subjects: Optional[List[str]] = Field(None, description="List of subjects")
    subjectCodes: Optional[List[str]] = Field(None, description="List of subject codes")
    periods: Optional[List[str]] = Field(None, description="List of class periods")
    resources: Optional[List[TimebackSourcedIdReference]] = Field(None, description="References to learning resources")
    terms: Optional[List[TimebackSourcedIdReference]] = Field(None, description="References to academic terms")


class TimebackUpdateClassRequest(BaseModel):
    """Top-level request wrapper for PUT /classes/{sourcedId}.
    
    Attributes:
        Required:
            - class_ (TimebackUpdateClassBody): Class data to update. See TimebackUpdateClassBody for structure.
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    class_: TimebackUpdateClassBody = Field(..., alias="class", description="Class data to update")

