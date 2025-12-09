## PowerPath — External Tests - Create External Test-Out

### POST /powerpath/createExternalTestOut

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- **Status: DEPRECATED**

⚠️ **This endpoint is deprecated and will be removed in a future version.**

### Migration

Test-outs are now created on-demand using `POST /powerpath/lessonPlans/startTestOut`. This creates unlisted test assignments instead of course-linked lessons.

**New Flow:**
1. Check test-out availability: `GET /powerpath/lessonPlans/getCourseProgress/{courseId}/student/{studentId}`
2. Start test-out: `POST /powerpath/lessonPlans/startTestOut` with `{ courseId, studentId }`
3. Launch external test: `POST /powerpath/makeExternalTestAssignment` (unchanged)

---

### Legacy Behavior

Creates or updates a ComponentResource to act as a TestOut lesson in a course for integration with external test platforms like Edulastic.

Request body (JSON):

**Required fields:**
- `courseId` (string): The sourcedId of the Course
- `toolProvider` (string): Valid values: `edulastic`, `mastery-track`
- `grades` (array of strings): Valid values: "-1", "0", "1"..."13"
- `lessonType` (string): Must be "test-out" (automatically set)
- `xp` (number): The XP value for the resource (required for test-out)

**Optional fields:**
- `lessonTitle`, `launchUrl`, `unitTitle`, `courseComponentSourcedId`, `vendorId`, `description`, `resourceMetadata`

Successful response (HTTP 200):

- Same structure as `create_external_placement_test`
- `lessonType` will be "test-out"

Python usage (deprecated):

```python
import warnings
from timeback import Timeback
from timeback.models.request import TimebackCreateExternalTestOutRequest

client = Timeback()

# This will emit a DeprecationWarning
request = TimebackCreateExternalTestOutRequest(
    courseId="course-sourced-id",
    toolProvider="edulastic",
    grades=["5", "6"],
    xp=100,  # Required for test-out
)

with warnings.catch_warnings():
    warnings.simplefilter("always")  # To see the warning
    response = client.powerpath.create_external_test_out(request)
```

**Recommended: Use the new flow instead.**

