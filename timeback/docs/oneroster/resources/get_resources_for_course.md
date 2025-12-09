## OneRoster - Resources - Get Resources for Course

### GET /ims/oneroster/resources/v1p2/courses/{courseSourcedId}/resources

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Get resources associated with a specific course.

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackGetResourcesForCourseRequest

client = Timeback()
request = TimebackGetResourcesForCourseRequest(course_sourced_id="<course-id>")
response = client.oneroster.resources.get_resources_for_course(request)
print(f"Total: {response.totalCount}")
```

