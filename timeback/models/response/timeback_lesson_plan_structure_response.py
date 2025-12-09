"""Response model for getting lesson plan structure.

GET /powerpath/lessonPlans/tree/{lessonPlanId}/structure

Returns a simplified structure for inspection and debugging.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class TimebackLessonPlanStructureNode(BaseModel):
    """A node in the lesson plan structure tree.
    
    Used for administrative tools and debugging to see the internal
    lesson plan structure without full metadata.
    
    Attributes:
        - type (str): Either "component" or "resource"
        - title (str): Display title
        - order (str): Sort order
        - skipped (bool): Whether the item is hidden from student
        - itemId (str): Internal item ID (not stable, don't rely on it)
        - componentId (str, optional): ID of the component
        - componentResourceId (str, optional): ID of the component resource
        - componentResources (list, optional): Child resources
        - subComponents (list, optional): Child components
    """

    type: str = Field(..., description="Either 'component' or 'resource'")
    title: str = Field(..., description="Display title")
    order: str = Field(..., description="Sort order")
    skipped: bool = Field(..., description="Whether item is hidden")
    itemId: str = Field(..., description="Internal item ID")
    componentId: Optional[str] = Field(None, description="Component ID")
    componentResourceId: Optional[str] = Field(None, description="Component resource ID")
    componentResources: Optional[List["TimebackLessonPlanStructureNode"]] = Field(
        None, description="Child resources"
    )
    subComponents: Optional[List["TimebackLessonPlanStructureNode"]] = Field(
        None, description="Child components"
    )


class TimebackLessonPlanStructureData(BaseModel):
    """Inner lesson plan structure data.
    
    Attributes:
        - id (str): Lesson plan ID
        - courseId (str): Associated course ID
        - courseTitle (str): Course title
        - structure (list): Tree structure of nodes
    """

    id: str = Field(..., description="Lesson plan ID")
    courseId: str = Field(..., description="Course ID")
    courseTitle: str = Field(..., description="Course title")
    structure: List[TimebackLessonPlanStructureNode] = Field(
        ..., description="Structure nodes"
    )


class TimebackLessonPlanStructureWrapper(BaseModel):
    """Wrapper containing the lesson plan structure data."""

    lessonPlan: TimebackLessonPlanStructureData


class TimebackLessonPlanStructureResponse(BaseModel):
    """Response model for getting lesson plan structure.
    
    GET /powerpath/lessonPlans/tree/{lessonPlanId}/structure
    
    Attributes:
        - lessonPlan (wrapper): Contains the lesson plan structure data
    """

    lessonPlan: TimebackLessonPlanStructureWrapper


# Enable forward references for recursive type
TimebackLessonPlanStructureNode.model_rebuild()

