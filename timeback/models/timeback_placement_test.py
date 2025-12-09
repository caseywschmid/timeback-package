"""Placement Test model for the PowerPath API.

This module defines the PlacementTest model which represents a placement test
with its associated resources and assessment data from the PowerPath API.
"""

from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field


class TimebackPlacementTest(BaseModel):
    """Represents a placement test from the PowerPath API.
    
    A placement test is a ComponentResource object which has a Resource object
    with metadata.lessonType = "placement" associated with it.
    
    Attributes:
        - component_resources (Dict[str, Any]): The component resource data
        - resources (Dict[str, Any]): The resource data
        - resources_metadata (Dict[str, Any]): Metadata associated with the resource
        - assessment_line_items (Dict[str, Any], optional): Assessment line item data, if available
        - assessment_results (List[Dict[str, Any]], optional): List of assessment results, if available
    """

    component_resources: Dict[str, Any] = Field(
        ..., description="The component resource data"
    )
    resources: Dict[str, Any] = Field(
        ..., description="The resource data"
    )
    resources_metadata: Dict[str, Any] = Field(
        ..., description="Metadata associated with the resource"
    )
    assessment_line_items: Optional[Dict[str, Any]] = Field(
        None, description="Assessment line item data, if available"
    )
    assessment_results: Optional[List[Dict[str, Any]]] = Field(
        None, description="List of assessment results, if available"
    )

