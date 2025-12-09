## PowerPath — Lesson Plans - Get Operations

### GET /powerpath/lessonPlans/{lessonPlanId}/operations

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)

Returns all operations for a lesson plan in chronological order.

### Purpose

Use this endpoint for:
- Audit trails and history tracking
- Debugging lesson plan issues
- Administrative oversight

### Path Parameters

- `lessonPlanId` (string, required): The ID of the lesson plan

### Response

```json
{
  "operations": [
    {
      "id": "op-123",
      "type": "set-skipped",
      "payload": {
        "target": { "type": "component", "id": "unit-1" },
        "value": true
      },
      "reason": "Skip this unit",
      "createdAt": "2024-01-15T10:30:00Z",
      "sequenceNumber": 1,
      "createdBy": "user-123"
    },
    {
      "id": "op-124",
      "type": "move-item-before",
      "payload": { ... },
      "reason": null,
      "createdAt": "2024-01-15T11:00:00Z",
      "sequenceNumber": 2,
      "createdBy": "user-456"
    }
  ]
}
```

### Operation Object Fields

- `id` (string): Unique identifier for the operation
- `type` (string): Operation type (set-skipped, move-item-before, etc.)
- `payload` (object): Operation-specific data
- `reason` (string|null): Reason for the operation
- `createdAt` (string): ISO timestamp when created
- `sequenceNumber` (number): Order in the operation log
- `createdBy` (string|null): User who made the change

### Python Usage

```python
from timeback import Timeback

client = Timeback()

response = client.powerpath.get_operations("lesson-plan-id")

for op in response.operations:
    print(f"[{op.sequenceNumber}] {op.type}")
    print(f"  Created: {op.createdAt}")
    print(f"  By: {op.createdBy or 'System'}")
    if op.reason:
        print(f"  Reason: {op.reason}")
```

### Notes

- Operations are returned in chronological order (by sequenceNumber)
- The `payload` structure varies based on the operation type
- `createdBy` may be null for system-generated operations

