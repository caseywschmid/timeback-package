## PowerPath — Lesson Plans - Get Lesson Plan

### GET /powerpath/lessonPlans/tree/{lessonPlanId}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)

Returns the complete lesson plan tree by its ID.

### Purpose

Use this endpoint:
- When you need to display the full lesson plan to a student
- For rendering the personalized learning path

### Path Parameters

- `lessonPlanId` (string, required): The ID of the lesson plan

### What It Returns

- Lesson plan in syllabus-like format
- Only non-skipped items (visible content)
- Hierarchical structure with components and resources
- All original metadata needed for UI rendering

### Response

Returns a `LessonPlan` object with course info and nested components.

### Python Usage

```python
from timeback import Timeback

client = Timeback()

lesson_plan = client.powerpath.get_lesson_plan("lesson-plan-id")

print(f"Course: {lesson_plan.course.title}")
print(f"Components: {len(lesson_plan.subComponents)}")

for component in lesson_plan.subComponents:
    print(f"  - {component.title}")
```

### Notes

- This is similar to `get_tree` but uses `lessonPlanId` instead of `courseId/userId`
- Returns only visible (non-skipped) content
- For debugging with all items, use `get_lesson_plan_structure`

