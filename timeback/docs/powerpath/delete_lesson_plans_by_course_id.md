## PowerPath — Lesson Plans - Delete Lesson Plans by Course ID

### DELETE /powerpath/lessonPlans/{courseId}/deleteAll

- Method: DELETE
- Auth: OAuth2 Client Credentials (Bearer token)

Deletes all lesson plans for a course.

**WARNING**: This is a destructive operation that cannot be undone.

### Path Parameters

- `courseId` (string, required): The sourcedId of the course

### Response

- HTTP 204 No Content (no response body)

### Python Usage

```python
from timeback import Timeback

client = Timeback()

# WARNING: This will delete all lesson plans for the course!
client.powerpath.delete_lesson_plans_by_course_id("course-sourced-id")

# Returns None (204 No Content)
```

### Notes

- This operation is irreversible
- All student lesson plans for the course will be deleted
- Use with caution in production environments
- Returns 404 if course is not found

