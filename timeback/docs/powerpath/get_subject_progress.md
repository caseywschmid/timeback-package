## PowerPath — Placement - Get Subject Progress

### GET /powerpath/placement/getSubjectProgress

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get the progress the student has made in a given subject.

Returns progress information for each course in the subject, including completion status, XP earned, and test-out usage.

Query params:

- `student` (string, required): The sourcedId of the student
- `subject` (string, required): The subject name. Valid values: `Reading`, `Language`, `Vocabulary`, `Social Studies`, `Writing`, `Science`, `FastMath`, `Math`

Successful response (HTTP 200):

- Body: `{ "progress": [...] }`
- The `progress` array contains one object per course in the subject, with these fields:
  - `course`: Course information object
    - `sourcedId`: Unique identifier for the course
    - `title`: Title of the course
    - `courseCode`: Course code (nullable)
    - `level`: Course level (nullable)
    - `grades`: List of grade levels (nullable)
    - `subjects`: List of subjects (nullable)
    - `status`: Course status
    - `orgSourcedId`: Organization sourcedId
    - `dateLastModified`: Last modification timestamp
  - `inEnrolled`: Whether the student is enrolled in the course
  - `hasUsedTestOut`: Whether the student has a fully graded test-out result
  - `testOutLessonId`: The sourcedId of the test-out lesson ComponentResource (nullable)
  - `completedLessons`: Number of lessons with 'fully graded' assessment results
  - `totalLessons`: Total number of lessons in the course
  - `totalAttainableXp`: Total XP that can be earned (not considering multipliers)
  - `totalXpEarned`: Total XP earned (considering calculated multipliers)

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
from timeback.models.request import TimebackGetSubjectProgressRequest
from timeback.enums import TimebackSubject

client = Timeback()

# Get subject progress for a student in Reading
request = TimebackGetSubjectProgressRequest(
    student="student-sourced-id",
    subject=TimebackSubject.READING,
)
response = client.powerpath.get_subject_progress(request)

print(f"Total courses in subject: {len(response.progress)}")

for item in response.progress:
    course = item.course
    print(f"Course: {course.title}")
    print(f"  Progress: {item.completedLessons}/{item.totalLessons} lessons")
    print(f"  XP: {item.totalXpEarned}/{item.totalAttainableXp}")
```

Notes:

- The `subject` parameter uses the `TimebackSubject` enum which maps to the API's expected string values.
- Progress includes all courses in the subject, even those the student isn't enrolled in (`inEnrolled = false`).
- XP values use integers; `totalAttainableXp` doesn't account for multipliers while `totalXpEarned` does.

