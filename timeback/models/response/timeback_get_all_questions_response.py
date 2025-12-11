"""Response model for getting all questions from an assessment test.

GET /assessment-tests/{identifier}/questions

Used by:
- timeback/services/qti/endpoints/get_all_questions.py
"""

from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field
from timeback.models.timeback_qti_assessment_item import TimebackQTIAssessmentItem


class TimebackQuestionReference(BaseModel):
    """Reference information about where an assessment item is located in the test structure.
    
    Attributes:
        - identifier (str): Unique identifier for the assessment item reference
        - href (str): URL reference to the assessment item
        - test_part (str): Test part identifier where this item is located
        - section (str): Section identifier where this item is located
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    identifier: str = Field(..., description="Unique identifier for the assessment item reference")
    href: str = Field(..., description="URL reference to the assessment item")
    test_part: str = Field(..., alias="testPart", description="Test part identifier where this item is located")
    section: str = Field(..., description="Section identifier where this item is located")


class TimebackQuestionWithReference(BaseModel):
    """A question with its reference information in the test structure.
    
    Attributes:
        - reference (TimebackQuestionReference): Location info for the item
        - question (TimebackQTIAssessmentItem): The actual assessment item data
    """
    
    reference: TimebackQuestionReference = Field(
        ...,
        description="Reference information about where this item is located"
    )
    question: Optional[TimebackQTIAssessmentItem] = Field(
        None,
        description="The actual assessment item data"
    )


class TimebackGetAllQuestionsResponse(BaseModel):
    """Response model for getting all questions from an assessment test.
    
    This endpoint retrieves all assessment items (questions) referenced by
    an assessment test, along with their structural context (test part and section).
    
    Attributes:
        - assessment_test (str): Identifier of the assessment test
        - title (str): Title of the assessment test
        - total_questions (int): Total number of questions in the test
        - questions (list): List of questions with their reference information.
          See TimebackQuestionWithReference for structure.
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    assessment_test: str = Field(
        ...,
        alias="assessmentTest",
        description="Identifier of the assessment test"
    )
    title: str = Field(..., description="Title of the assessment test")
    total_questions: int = Field(
        ...,
        alias="totalQuestions",
        description="Total number of questions in the test"
    )
    questions: List[TimebackQuestionWithReference] = Field(
        ...,
        description="List of questions with their reference information"
    )

