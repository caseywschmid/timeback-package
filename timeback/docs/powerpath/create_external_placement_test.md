## PowerPath — External Tests - Create External Placement Test

### POST /powerpath/createExternalPlacementTest

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Create or update an external placement test for a course.

Creates or updates a ComponentResource to act as a Placement Test lesson in a course. This allows integrating with external test-taking platforms (like Edulastic) for content delivery.

The endpoint creates or updates:
- A CourseComponent for the course to hold the Placement Test lesson
- A Resource with lessonType = "placement" and the external service details as metadata
- A ComponentResource acting as the Placement Test lesson

Request body (JSON):

**Required fields:**
- `courseId` (string): The sourcedId of the Course to create the external test for
- `toolProvider` (string): The type of external service. Valid values: `edulastic`, `mastery-track`
- `grades` (array of strings): The grades for the resource. Valid values: "-1", "0", "1"..."13"
- `lessonType` (string): Must be "placement" (automatically set)

**Optional fields:**
- `lessonTitle` (string): The title of the external test reference
- `launchUrl` (string): The URL to the external test system
- `unitTitle` (string): The title of the unit containing the external test
- `courseComponentSourcedId` (string): The sourcedId of an existing CourseComponent (unit). If not provided, a new unit will be created.
- `vendorId` (string): The ID of the test in the spreadsheet
- `description` (string): Description of the external test for the Resource metadata
- `resourceMetadata` (any): Additional metadata for the external test resource
- `courseIdOnFail` (string): The courseId to enroll the student in if they fail (score < 90%)
- `xp` (number): The XP value for the resource

Successful response (HTTP 200):

- `lessonType` (string): The type of lesson created
- `lessonId` (string): The sourcedId of the created external test reference (ComponentResource)
- `courseComponentId` (string): The sourcedId of the component (unit) containing the test
- `resourceId` (string): The sourcedId of the resource representing the external test
- `toolProvider` (string): The tool provider id
- `launchUrl` (string, optional): The URL to the external test system
- `vendorId` (string, optional): The ID of the test
- `courseIdOnFail` (string, optional): The fallback course ID
- `grades` (array, optional): The grades for the resource

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 403: Forbidden → raises `RequestError`
- 404: Not Found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackCreateExternalPlacementTestRequest

client = Timeback()

# Create an external placement test
request = TimebackCreateExternalPlacementTestRequest(
    courseId="course-sourced-id",
    toolProvider="edulastic",
    grades=["5", "6"],
    lessonTitle="Grade 5-6 Placement Test",
    launchUrl="https://edulastic.com/test/123",
    courseIdOnFail="remedial-course-id",  # Optional: enroll here if score < 90%
)
response = client.powerpath.create_external_placement_test(request)

print(f"Lesson ID: {response.lessonId}")
print(f"Resource ID: {response.resourceId}")
```

Notes:

- If `courseIdOnFail` is supplied, the student will be automatically enrolled in that course when the placement test is completed with a score below 90%.
- The request fails if the course doesn't exist or if an existing placement test targeting the same grade has a different toolProvider.
- A test assignment is required to obtain access credentials (use `make_external_test_assignment`).

