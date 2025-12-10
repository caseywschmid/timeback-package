"""Response model for processing an assessment item response.

POST /assessment-items/{identifier}/process-response

Used by:
- timeback/services/qti/endpoints/process_response.py
"""

from pydantic import BaseModel, Field


class TimebackProcessResponseFeedback(BaseModel):
    """Feedback structure returned from response processing.
    
    Attributes:
        - identifier (str): Machine-readable feedback identifier
          (e.g., 'correct', 'incorrect', or custom identifiers)
        - value (str): Human-readable feedback message
    """
    
    identifier: str = Field(
        ...,
        description="Feedback classification identifier (e.g., 'correct', 'incorrect')"
    )
    value: str = Field(
        ...,
        description="Human-readable feedback message"
    )


class TimebackProcessResponseResponse(BaseModel):
    """Response model for processing an assessment item response.
    
    Contains the calculated score and feedback for the candidate's response.
    
    Attributes:
        - score (float): Numerical score for the response.
          - 1.0 for correct answers
          - 0.0 for incorrect answers
          - Decimal value (0.0-1.0) for AI-graded extended text responses
        - feedback (TimebackProcessResponseFeedback): Structured feedback info
    
    Example response:
        {
            "score": 1.0,
            "feedback": {
                "identifier": "correct",
                "value": "Correct! Well done."
            }
        }
    """
    
    score: float = Field(
        ...,
        description="Numerical score (0.0-1.0) for the response"
    )
    feedback: TimebackProcessResponseFeedback = Field(
        ...,
        description="Structured feedback with identifier and message"
    )

