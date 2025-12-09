"""Get Lesson Plan Structure endpoint for PowerPath.

GET /powerpath/lessonPlans/tree/{lessonPlanId}/structure

Returns a simplified structure for inspection and debugging.
Shows both skipped and non-skipped items.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackLessonPlanStructureResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_lesson_plan_structure(
    http: HttpClient,
    lesson_plan_id: str,
) -> TimebackLessonPlanStructureResponse:
    """Get simplified lesson plan structure for debugging.

    GET /powerpath/lessonPlans/tree/{lessonPlanId}/structure

    Returns a lightweight view of the lesson plan structure showing:
    - Both skipped and non-skipped items
    - Order information
    - Component and resource IDs

    Args:
        http: Injected HTTP client for making requests
        lesson_plan_id: The ID of the lesson plan

    Returns:
        TimebackLessonPlanStructureResponse with structure tree
    """
    path = f"/powerpath/lessonPlans/tree/{lesson_plan_id}/structure"

    data: Dict[str, Any] = http.get(path)
    log.debug(f"Raw Data: {data}")
    return TimebackLessonPlanStructureResponse.model_validate(data)

