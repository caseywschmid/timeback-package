"""Request model for updating student question response.

PUT /powerpath/updateStudentQuestionResponse
"""

from typing import Optional, Dict, Any, Union, List
from pydantic import BaseModel, ConfigDict, Field


class TimebackUpdateStudentQuestionResponseRequest(BaseModel):
    """Request model for updating a student's response to a question.
    
    Updates the response and checks correctness using QTI
    response declarations. Creates/updates AssessmentLineItem
    and AssessmentResult objects.
    
    Attributes:
        Required:
            - student (str): The sourcedId of the student
            - question (str): The QTI question identifier from the lesson's question bank
            - lesson (str): The sourcedId of the lesson (ComponentResource)
        
        Optional:
            - response (Any): DEPRECATED - use responses instead.
              The student's single response to the question.
            - responses (dict): Object with response identifiers as keys
              and values as strings or arrays of strings.
    """

    model_config = ConfigDict(populate_by_name=True)

    student: str = Field(..., description="Student sourcedId")
    question: str = Field(..., description="QTI question identifier")
    lesson: str = Field(..., description="Lesson (ComponentResource) sourcedId")
    response: Optional[Union[str, List[str]]] = Field(
        None, description="DEPRECATED: Use responses instead"
    )
    responses: Optional[Dict[str, Union[str, List[str]]]] = Field(
        None, description="Response identifiers and values"
    )

