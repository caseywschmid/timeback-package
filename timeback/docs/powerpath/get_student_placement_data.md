## PowerPath — Placement - Get Student Placement Data

### GET /powerpath/placement/{studentId}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)

Returns comprehensive placement data for a student across all subjects.

### Path Parameters

- `studentId` (string, required): The sourcedId of the student

### Response

The response is a dictionary with subject names as keys:

```json
{
  "Math": {
    "startingGrade": 3,
    "currentGrade": 5,
    "subjectLowestGrade": 1,
    "subjectHighestGrade": 8,
    "RIT": {
      "GROWTH": { "score": 210, "grade": 5 },
      "SCREENING": { "score": 205, "grade": 4 }
    },
    "results": [
      {
        "testId": "test-123",
        "title": "Grade 3 Math Placement",
        "subject": "Math",
        "grade": 3,
        "status": "PASSED",
        "score": 92.5,
        "completedAt": "2024-01-15T10:30:00Z",
        "source": "PLACEMENT",
        "masteryTrackProcessed": true
      }
    ],
    "status": "in_progress",
    "nextTestId": "test-456"
  },
  "Reading": { ... },
  "Language": { ... },
  ...
}
```

### Subject Data Structure

Each subject contains:
- `startingGrade` (int): The grade level where placement started
- `currentGrade` (int): The current grade level after placement
- `subjectLowestGrade` (int): The lowest grade available for this subject
- `subjectHighestGrade` (int): The highest grade available for this subject
- `RIT`: RIT scores for GROWTH and SCREENING tests
- `results`: Array of test results
- `status` (string): Overall placement status
- `nextTestId` (string|null): ID of the next test, or null if complete

### Test Result Status Values

- `PASSED` - Student passed the test
- `FAILED` - Student failed the test
- `STARTED` - Test is in progress
- `NOT_STARTED` - Test not yet started
- `SKIP` - Test was skipped

### Test Source Values

- `PLACEMENT` - Internal placement test
- `EDULASTIC` - External Edulastic test

### Available Subjects

- `Reading`
- `Language`
- `Vocabulary`
- `Social Studies`
- `Writing`
- `Science`
- `FastMath`
- `Math`

### Python Usage

```python
from timeback import Timeback

client = Timeback()

data = client.powerpath.get_student_placement_data("student-sourced-id")

for subject, placement in data.items():
    print(f"{subject}: Grade {placement.currentGrade} ({placement.status})")
    
    if placement.RIT.GROWTH:
        print(f"  RIT Growth: {placement.RIT.GROWTH.score}")
    
    for result in placement.results:
        print(f"  - {result.title}: {result.status.value}")
```

### Response Types

The response is typed as `Dict[str, TimebackSubjectPlacementData]`. The nested models include:
- `TimebackSubjectPlacementData` - Main subject data
- `TimebackRitScores` - Container for GROWTH and SCREENING scores
- `TimebackRitScoreData` - Individual RIT score with grade
- `TimebackPlacementTestResult` - Individual test result
- `TimebackPlacementTestStatus` - Enum for test status
- `TimebackPlacementTestSource` - Enum for test source

