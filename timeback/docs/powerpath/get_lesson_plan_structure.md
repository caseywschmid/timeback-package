## PowerPath — Lesson Plans - Get Lesson Plan Structure

### GET /powerpath/lessonPlans/tree/{lessonPlanId}/structure

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)

Returns a simplified structure for inspection and debugging.

### Purpose

Use this endpoint:
- For administrative tools and debugging
- When you need to see internal structure without full metadata
- To view both skipped and non-skipped items

### Path Parameters

- `lessonPlanId` (string, required): The ID of the lesson plan

### Response

```json
{
  "lessonPlan": {
    "lessonPlan": {
      "id": "lp-123",
      "courseId": "course-456",
      "courseTitle": "Math 101",
      "structure": [
        {
          "type": "component",
          "title": "Unit 1",
          "order": "1",
          "skipped": false,
          "itemId": "item-1",
          "componentId": "comp-1",
          "subComponents": []
        },
        {
          "type": "resource",
          "title": "Video 1",
          "order": "1.1",
          "skipped": true,
          "itemId": "item-2",
          "componentResourceId": "res-1"
        }
      ]
    }
  }
}
```

### Structure Node Fields

- `type`: Either "component" or "resource"
- `title`: Display title
- `order`: Sort order string
- `skipped`: Whether item is hidden from student
- `itemId`: Internal ID (not stable, don't rely on it)
- `componentId`: Component ID (for components)
- `componentResourceId`: Resource ID (for resources)
- `subComponents`: Nested child components
- `componentResources`: Nested child resources

### Python Usage

```python
from timeback import Timeback

client = Timeback()

response = client.powerpath.get_lesson_plan_structure("lesson-plan-id")

data = response.lessonPlan.lessonPlan
print(f"Course: {data.courseTitle}")

for node in data.structure:
    skip = "[SKIPPED] " if node.skipped else ""
    print(f"{skip}[{node.type}] {node.title}")
```

### Notes

- Shows both visible and hidden (skipped) items
- Useful for debugging lesson plan state
- The `itemId` field is internal and may change

