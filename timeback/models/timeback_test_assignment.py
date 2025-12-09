"""Test assignment models used across multiple endpoints.

Shared models for:
- POST /powerpath/test-assignments
- GET /powerpath/test-assignments
- GET /powerpath/test-assignments/admin
- GET /powerpath/test-assignments/{id}
- POST /powerpath/test-assignments/bulk
- POST /powerpath/test-assignments/import
"""

from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum


class TimebackTestAssignmentStatus(str, Enum):
    """Status values for test assignments."""

    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    EXPIRED = "expired"
    CANCELLED = "cancelled"


class TimebackTestAssignment(BaseModel):
    """A test assignment record.
    
    Attributes:
        - sourcedId (str): The assignment ID
        - studentSourcedId (str): The student's sourcedId
        - studentEmail (str): The student's email
        - assignedByUserSourcedId (str, optional): Who assigned the test
        - subject (str): Subject of the test
        - grade (str): Grade level
        - assignmentStatus (str): Current status
        - testName (str, optional): Display name
        - assignedAt (str, optional): When assigned
        - expiresAt (str, optional): When expires
        - completedAt (str, optional): When completed
        - resourceSourcedId (str, optional): Associated resource
        - componentResourceSourcedId (str, optional): Associated component resource
    """

    sourcedId: str = Field(..., description="Assignment ID")
    studentSourcedId: str = Field(..., description="Student ID")
    studentEmail: str = Field(..., description="Student email")
    assignedByUserSourcedId: Optional[str] = Field(None, description="Assigning user ID")
    subject: str = Field(..., description="Test subject")
    grade: str = Field(..., description="Grade level")
    assignmentStatus: str = Field(..., description="Current status")
    testName: Optional[str] = Field(None, description="Display name")
    assignedAt: Optional[str] = Field(None, description="Assignment timestamp")
    expiresAt: Optional[str] = Field(None, description="Expiration timestamp")
    completedAt: Optional[str] = Field(None, description="Completion timestamp")
    resourceSourcedId: Optional[str] = Field(None, description="Resource ID")
    componentResourceSourcedId: Optional[str] = Field(
        None, description="Component resource ID"
    )


class TimebackTestAssignmentResult(BaseModel):
    """Result of creating a test assignment.
    
    Used in create, bulk create, and import responses.
    
    Attributes:
        - assignmentId (str): The test assignment ID
        - lessonId (str): The component resource ID (unlisted lesson)
        - resourceId (str): The resource ID created
    """

    assignmentId: str = Field(..., description="Test assignment ID")
    lessonId: str = Field(..., description="Component resource ID")
    resourceId: str = Field(..., description="Resource ID")


class TimebackTestAssignmentError(BaseModel):
    """Error from bulk/import operations.
    
    Attributes:
        - row (int): Row number (0-based) where error occurred
        - message (str): Error description
    """

    row: int = Field(..., description="Row number (0-based)")
    message: str = Field(..., description="Error message")

