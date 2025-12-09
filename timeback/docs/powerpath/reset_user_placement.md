## PowerPath — Placement - Reset User Placement

### POST /powerpath/placement/resetUserPlacement

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- **Access**: Administrators only

Resets a user's placement progress for a specific subject. **This operation cannot be undone.**

### What it does

- Soft deletes all placement assessment results for the specified subject
- Resets user onboarding state to "in_progress"
- Removes completedAt and courseId from the onboarding record if they exist

### Request Body

```json
{
  "student": "student-sourced-id",
  "subject": "Math"
}
```

**Required fields:**
- `student` (string): The sourcedId of the student
- `subject` (string): The subject to reset. Valid values: `Reading`, `Language`, `Vocabulary`, `Social Studies`, `Writing`, `Science`, `FastMath`, `Math`

### Response

```json
{
  "success": true,
  "placementResultsDeleted": 5,
  "onboardingReset": true
}
```

**Fields:**
- `success` (boolean): Whether the reset operation was successful
- `placementResultsDeleted` (number): Number of placement results that were soft-deleted
- `onboardingReset` (boolean): Whether the onboarding state was reset

### Python Usage

```python
from timeback import Timeback
from timeback.models.request import TimebackResetUserPlacementRequest
from timeback.enums import TimebackSubject

client = Timeback()

request = TimebackResetUserPlacementRequest(
    student="student-sourced-id",
    subject=TimebackSubject.MATH,
)

# WARNING: This cannot be undone!
response = client.powerpath.reset_user_placement(request)

print(f"Success: {response.success}")
print(f"Results deleted: {response.placementResultsDeleted}")
print(f"Onboarding reset: {response.onboardingReset}")
```

### Notes

- **Administrator access required** - This endpoint is restricted to admin users only
- **Irreversible operation** - All placement data for the subject will be soft-deleted
- Use cases include: correcting testing errors, allowing re-placement, resetting student progress

