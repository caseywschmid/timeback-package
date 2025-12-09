## PowerPath — Lesson Plans - Sync Operations

### POST /powerpath/lessonPlans/{lessonPlanId}/operations/sync

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)

Applies pending operations to update a lesson plan's structure.

### Purpose

Use this endpoint:
- After storing operations, to see changes take effect
- For incremental updates without full recreation
- After running scripts that add many operations at once

### Path Parameters

- `lessonPlanId` (string, required): The ID of the lesson plan

### Response

```json
{
  "success": true,
  "message": "Operations synced",
  "operationCount": 3,
  "operationResults": [
    { "success": true },
    { "success": true },
    { "success": false, "errors": [{ "message": "Target not found" }] }
  ]
}
```

**Fields:**
- `success` (bool): Whether the overall sync succeeded
- `message` (string, optional): Additional information
- `operationCount` (int): Number of operations processed
- `operationResults` (array): Result of each operation

### Python Usage

```python
from timeback import Timeback

client = Timeback()

response = client.powerpath.sync_operations("lesson-plan-id")

print(f"Success: {response.success}")
print(f"Operations processed: {response.operationCount}")

for i, result in enumerate(response.operationResults):
    if result.success:
        print(f"  Operation {i+1}: Success")
    else:
        for error in result.errors or []:
            print(f"  Operation {i+1} failed: {error.message}")
```

### Notes

- Only applies operations that haven't been applied yet
- Operations are executed in sequence order
- If an operation fails, subsequent operations may still be attempted

