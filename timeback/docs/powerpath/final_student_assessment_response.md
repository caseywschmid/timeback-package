## PowerPath — Assessment - Final Student Assessment Response

### POST /powerpath/finalStudentAssessmentResponse

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)

Finalizes a test assessment after all questions have been answered.

### Supported Lesson Types

- `quiz`
- `test-out`
- `placement`
- `unit-test`

**Not supported for external test lessons** - use `import_external_test_assignment_results` instead.

### Request Body

```json
{
  "student": "student-sourced-id",
  "lesson": "lesson-component-resource-id"
}
```

### What It Does

1. Evaluates answered questions
2. Attributes scores for each question and overall lesson
3. Creates/updates AssessmentLineItem and AssessmentResult objects
4. May trigger course enrollment for placement/test-out lessons

### Response

```json
{
  "lessonType": "quiz",
  "finalized": true,
  "attempt": 1
}
```

### Python Usage

```python
from timeback import Timeback
from timeback.models.request import TimebackFinalStudentAssessmentRequest

client = Timeback()

request = TimebackFinalStudentAssessmentRequest(
    student="student-id",
    lesson="lesson-component-resource-id",
)

response = client.powerpath.final_student_assessment_response(request)

if response.finalized:
    print(f"Assessment finalized! Attempt: {response.attempt}")
else:
    print("Already finalized in a previous call")
```

