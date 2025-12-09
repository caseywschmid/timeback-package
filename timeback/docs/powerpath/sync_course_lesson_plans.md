## PowerPath — Lesson Plans - Sync Course Lesson Plans

### POST /powerpath/lessonPlans/course/{courseId}/sync

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)

Bulk synchronization of all lesson plans for a course.

### Purpose

Use this endpoint:
- After making significant structural changes to a base course
- When you need to ensure all students have the latest course content

### What It Does

1. Finds all lesson plans associated with the course
2. Recreates each lesson plan from the base course structure
3. Applies all historical operations to maintain personalizations
4. Returns list of affected lesson plan IDs

### Path Parameters

- `courseId` (string, required): The sourcedId of the course

### Response

```json
{
  "lessonPlansAffected": [
    "lp-student-1",
    "lp-student-2",
    "lp-student-3"
  ]
}
```

**Fields:**
- `lessonPlansAffected` (array): IDs of lesson plans that were synced

### Python Usage

```python
from timeback import Timeback

client = Timeback()

# WARNING: This will sync ALL lesson plans for the course
response = client.powerpath.sync_course_lesson_plans("course-sourced-id")

print(f"Lesson plans affected: {len(response.lessonPlansAffected)}")
for lp_id in response.lessonPlansAffected:
    print(f"  - {lp_id}")
```

### Notes

- This can be a long-running operation for courses with many students
- All student personalizations are maintained through operation logs
- Consider running during off-peak hours for large courses

