## PowerPath — Lesson Plans - Store Operation

### POST /powerpath/lessonPlans/{lessonPlanId}/operations

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)

Stores a new operation in a lesson plan's operation log. Primary endpoint for all lesson plan modifications.

### Request Body

```json
{
  "operation": {
    "type": "set-skipped",
    "payload": {
      "target": { "type": "component", "id": "comp-123" },
      "value": true
    }
  },
  "reason": "Optional reason for the change"
}
```

### Operation Types

| Type | Description |
|------|-------------|
| `set-skipped` | Show/hide content for the student |
| `move-item-before` | Move item before another item |
| `move-item-after` | Move item after another item |
| `move-item-to-start` | Move item to start of parent |
| `move-item-to-end` | Move item to end of parent |
| `add-custom-resource` | Add a custom resource |
| `change-item-parent` | Move item to a different parent |

### Response

```json
{
  "success": true,
  "message": "Operation stored",
  "operationId": "op-123-abc"
}
```

### Python Usage

```python
from timeback import Timeback
from timeback.models.request import TimebackStoreOperationRequest

client = Timeback()

# Set-skipped example
request = TimebackStoreOperationRequest(
    lesson_plan_id="lesson-plan-id",
    operation={
        "type": "set-skipped",
        "payload": {
            "target": {"type": "component", "id": "unit-123"},
            "value": True,
        },
    },
    reason="Skip this unit for now",
)

response = client.powerpath.store_operation(request)
print(f"Operation ID: {response.operationId}")
```

### Operation Payload Examples

**set-skipped:**
```python
{
    "type": "set-skipped",
    "payload": {
        "target": {"type": "component", "id": "comp-id"},
        "value": True
    }
}
```

**move-item-before:**
```python
{
    "type": "move-item-before",
    "payload": {
        "target": {"type": "resource", "id": "res-1"},
        "reference_id": "res-2"
    }
}
```

**add-custom-resource:**
```python
{
    "type": "add-custom-resource",
    "payload": {
        "resource_id": "custom-resource-id",
        "parent_component_id": "unit-id",
        "skipped": False
    }
}
```

**change-item-parent:**
```python
{
    "type": "change-item-parent",
    "payload": {
        "target": {"type": "resource", "id": "res-id"},
        "new_parent_id": "new-unit-id",
        "position": "end"  # or "start"
    }
}
```

