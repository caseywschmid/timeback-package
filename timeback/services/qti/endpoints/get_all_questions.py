"""Get All Questions endpoint for QTI API.

GET /assessment-tests/{identifier}/questions

Retrieve all assessment items referenced by an assessment test.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetAllQuestionsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_all_questions(
    http: HttpClient,
    identifier: str
) -> TimebackGetAllQuestionsResponse:
    """Get all assessment items referenced by an assessment test.
    
    GET /assessment-tests/{identifier}/questions
    
    Retrieves all assessment items (questions) that are referenced by
    an assessment test, along with their structural context (test part
    and section). This endpoint aggregates items from all sections
    across all test parts.
    
    Steps:
        1. Build the path with the test identifier
        2. Send GET request to /assessment-tests/{identifier}/questions
        3. Parse and validate response as TimebackGetAllQuestionsResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        identifier: The unique identifier of the assessment test
    
    Returns:
        TimebackGetAllQuestionsResponse containing:
            - assessment_test: Test identifier
            - title: Test title
            - total_questions: Total count of questions
            - questions: List of questions with reference info and item data
    
    Raises:
        HTTPError: If the request fails
        NotFoundError: If the assessment test doesn't exist
        ValidationError: If the response cannot be parsed
    
    Example:
        >>> response = get_all_questions(http, "test-001")
        >>> print(f"Test: {response.title}, Questions: {response.total_questions}")
        >>> for q in response.questions:
        ...     print(f"  {q.reference.section}: {q.question.title}")
    """
    path = f"/assessment-tests/{identifier}/questions"
    
    log.debug(f"Getting all questions for test: {identifier}")
    
    data: Dict[str, Any] = http.get(path)
    log.debug(f"Retrieved {data.get('totalQuestions', 0)} questions")
    
    return TimebackGetAllQuestionsResponse.model_validate(data)

