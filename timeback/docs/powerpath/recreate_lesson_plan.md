## PowerPath — Lesson Plans - Recreate Lesson Plan

### POST /powerpath/lessonPlans/{lessonPlanId}/recreate

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)

Recreates a lesson plan from scratch using its operation log.

### Purpose

Use this endpoint:
- When a lesson plan becomes corrupted or out of sync
- For testing or debugging purposes
- After detecting and correcting inconsistencies

### What It Does

1. Deletes all current lesson plan items
2. Rebuilds from the base course structure
3. Applies all operations from the operation log in sequence
4. Returns results of each operation for monitoring

### Path Parameters

- `lessonPlanId` (string, required): The ID of the lesson plan

### Response

```json
{
  "success": true,
  "message": "Lesson plan recreated",
  "operationCount": 5,
  "operationResults": [
    { "success": true },
    { "success": true },
    { "success": true },
    { "success": true },
    { "success": true }
  ]
}
```

### Python Usage

```python
from timeback import Timeback

client = Timeback()

# WARNING: This will rebuild the lesson plan from scratch
response = client.powerpath.recreate_lesson_plan("lesson-plan-id")

print(f"Success: {response.success}")
print(f"Operations reapplied: {response.operationCount}")
```

### Notes

- This is a potentially destructive operation
- All customizations are preserved through the operation log
- If operations fail during replay, the lesson plan may be in an inconsistent state

