"""Screening Session model for the PowerPath API.

This module defines models for screening session data from the PowerPath API.
"""

from typing import Optional, Literal
from pydantic import BaseModel, Field


class TimebackScreeningSessionAssignment(BaseModel):
    """Assignment information within a screening session.
    
    Attributes:
        - assignedTestKey (str, optional): The key of the assigned test
        - status (str, optional): The internal status of the assignment.
          Valid values: "enqueued", "assigned", "in_progress", "blocked", "completed", 
          "abandoned", "failed", null
        - nweaStatus (str, optional): The NWEA-specific status of the assignment.
          Valid values: "ENQUEUED", "AWAITING_STUDENT", "IN_PROGRESS", "PAUSED", 
          "SUSPENDED", "TERMINATED", "ABANDONED", "COMPLETED", "FAILED", null
    """

    assignedTestKey: Optional[str] = Field(None, description="The key of the assigned test")
    status: Optional[str] = Field(None, description="The internal status of the assignment")
    nweaStatus: Optional[str] = Field(None, description="The NWEA-specific status")


class TimebackScreeningSession(BaseModel):
    """Screening session information for a user.
    
    Attributes:
        - nweaStudentId (str): The NWEA student ID (UUID format)
        - createdOn (str): ISO timestamp when the session was created
        - password (str): The password for the screening session
        - name (str): The name associated with the session
        - proctorId (str): The proctor ID (UUID format)
        - pin (str): The PIN for the screening session
        - testSessionId (str): The test session ID (UUID format)
        - status (str): The status of the session. Valid values: "active", "inactive"
        - assignment (TimebackScreeningSessionAssignment): Assignment information
        - termId (str): The term ID
    """

    nweaStudentId: str = Field(..., description="The NWEA student ID (UUID)")
    createdOn: str = Field(..., description="ISO timestamp when the session was created")
    password: str = Field(..., description="The password for the screening session")
    name: str = Field(..., description="The name associated with the session")
    proctorId: str = Field(..., description="The proctor ID (UUID)")
    pin: str = Field(..., description="The PIN for the screening session")
    testSessionId: str = Field(..., description="The test session ID (UUID)")
    status: str = Field(..., description="The status of the session: 'active' or 'inactive'")
    assignment: TimebackScreeningSessionAssignment = Field(..., description="Assignment information")
    termId: str = Field(..., description="The term ID")

