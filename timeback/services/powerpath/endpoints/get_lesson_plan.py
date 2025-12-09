"""Get Lesson Plan endpoint for PowerPath.

GET /powerpath/lessonPlans/tree/{lessonPlanId}

Returns the complete lesson plan tree by its ID.
This is similar to get_tree but uses lessonPlanId instead of courseId/userId.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models import LessonPlan
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_lesson_plan(
    http: HttpClient,
    lesson_plan_id: str,
) -> LessonPlan:
    """Get the complete lesson plan tree by ID.

    GET /powerpath/lessonPlans/tree/{lessonPlanId}

    Returns the lesson plan in a syllabus-like format with:
    - Only non-skipped items (visible content)
    - Hierarchical structure with components and resources
    - All original metadata needed for UI rendering

    Args:
        http: Injected HTTP client for making requests
        lesson_plan_id: The ID of the lesson plan

    Returns:
        LessonPlan object with the complete tree structure
    """
    path = f"/powerpath/lessonPlans/tree/{lesson_plan_id}"

    data: Dict[str, Any] = http.get(path)
    log.debug(f"Raw Data: {data}")

    # The response has nested structure: { lessonPlan: { lessonPlan: {...} } }
    lesson_plan_data = data.get("lessonPlan", {}).get("lessonPlan", data)
    return LessonPlan.from_dict(lesson_plan_data)

