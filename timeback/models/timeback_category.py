"""Category model for OneRoster Gradebook API.

This module provides a Pydantic model for working with categories
in the Timeback API following the OneRoster 1.2 specification.
"""

from datetime import datetime, timezone
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from timeback.enums import TimebackStatus


class TimebackCategory(BaseModel):
    """Represents a category for line items in the gradebook.
    
    Categories are used to organize and group line items (assignments, assessments, etc.)
    in a class. Each category can have a weight that contributes to the overall grade calculation.
    
    Required fields per OneRoster 1.2 spec:
    - status: Status of the category
    - title: Title/name of the category
    """

    sourcedId: Optional[str] = Field(None, description="Unique identifier for the category")
    status: TimebackStatus = Field(..., description="Status of the category - 'active' or 'tobedeleted'")
    dateLastModified: Optional[str] = Field(
        None,
        description="Last modification timestamp in ISO 8601 format"
    )
    metadata: Optional[Dict[str, Any]] = Field(
        None,
        description="Additional metadata for the category"
    )
    title: str = Field(..., description="Title/name of the category")
    weight: Optional[float] = Field(None, description="Weight of the category for grade calculation")

