## PowerPath — Tests - Create Internal Test

### POST /powerpath/createInternalTest

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Create or update an internal test lesson in a course.

Creates or updates a ComponentResource to act as an internal test lesson in a course. This allows creating tests using internal QTI resources or assessment banks with multiple QTI resources.

### Test Types

**QTI Test (`testType: "qti"`):**
- Creates a single QTI resource
- Use for simple single-test scenarios

**Assessment Bank (`testType: "assessment-bank"`):**
- Creates multiple QTI resources wrapped in an assessment bank
- Use for placement tests or scenarios requiring multiple test variants

### Request Body - QTI Test

```json
{
  "courseId": "course-sourced-id",
  "lessonType": "quiz",
  "testType": "qti",
  "qti": {
    "url": "https://qti.example.com/test.xml",
    "title": "Chapter 1 Quiz",
    "metadata": {}
  },
  "lessonTitle": "Optional lesson title",
  "unitTitle": "Optional unit title"
}
```

### Request Body - Assessment Bank

```json
{
  "courseId": "course-sourced-id",
  "lessonType": "placement",
  "testType": "assessment-bank",
  "assessmentBank": {
    "resources": [
      { "url": "https://qti.example.com/test1.xml", "title": "Part 1" },
      { "url": "https://qti.example.com/test2.xml", "title": "Part 2" }
    ]
  },
  "grades": ["5", "6"]
}
```

**Required fields:**
- `courseId` (string): The sourcedId of the Course
- `lessonType` (string): Type of lesson. Valid values: `powerpath-100`, `quiz`, `test-out`, `placement`, `unit-test`, `alpha-read-article`
- `testType` (string): Either `qti` or `assessment-bank`
- `qti` or `assessmentBank`: Configuration object (depending on testType)

**Optional fields:**
- `lessonTitle`, `unitTitle`, `courseComponentSourcedId`, `resourceMetadata`
- `xp` (for test-out lessons)
- `grades`, `courseIdOnFail` (for placement tests)

### Response

```json
{
  "lessonType": "quiz",
  "testType": "qti",
  "lessonId": "component-resource-id",
  "courseComponentId": "course-component-id",
  "resourceId": "main-resource-id",
  "childResourceIds": ["child-1", "child-2"],  // only for assessment-bank
  "grades": ["5", "6"],
  "courseIdOnFail": null
}
```

### Python Usage

```python
from timeback import Timeback
from timeback.models.request import (
    TimebackCreateInternalQtiTestRequest,
    TimebackCreateInternalAssessmentBankTestRequest,
    TimebackQtiTestConfig,
    TimebackAssessmentBankConfig,
    TimebackAssessmentBankResource,
)

client = Timeback()

# Create a QTI test
qti_request = TimebackCreateInternalQtiTestRequest(
    courseId="course-id",
    lessonType="quiz",
    qti=TimebackQtiTestConfig(
        url="https://qti.example.com/test.xml",
        title="Chapter 1 Quiz",
    ),
)
response = client.powerpath.create_internal_test(qti_request)
print(f"Lesson ID: {response.lessonId}")

# Create an Assessment Bank test
bank_request = TimebackCreateInternalAssessmentBankTestRequest(
    courseId="course-id",
    lessonType="placement",
    grades=["5", "6"],
    assessmentBank=TimebackAssessmentBankConfig(
        resources=[
            TimebackAssessmentBankResource(url="https://qti.example.com/test1.xml"),
            TimebackAssessmentBankResource(url="https://qti.example.com/test2.xml"),
        ]
    ),
)
response = client.powerpath.create_internal_test(bank_request)
print(f"Child resources: {response.childResourceIds}")
```

### Notes

- For `test-out` and `placement` lessons, this updates existing tests of the same type.
- For other lesson types (`quiz`, `unit-test`, `pp-100`), it creates new lessons in the course structure.
- Assessment banks require at least one resource in the `resources` array.

