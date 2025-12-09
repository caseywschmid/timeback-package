## PowerPath — Syllabus - Get Course Syllabus

### GET /powerpath/syllabus/{courseSourcedId}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)

Returns the syllabus for a course.

### Path Parameters

- `courseSourcedId` (string, required): The sourcedId of the course

### Response

```json
{
  "syllabus": {
    // Syllabus content varies based on course configuration
  }
}
```

### Python Usage

```python
from timeback import Timeback

client = Timeback()

response = client.powerpath.get_course_syllabus("course-sourced-id")

print(response.syllabus)
```

