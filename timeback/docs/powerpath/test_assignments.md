# Test Assignments

Endpoints for managing standalone test-out assignments for students.

## Overview

Test assignments allow creating unlisted test-out assessments for students
without linking them to a course. These endpoints support individual creation,
bulk creation, and import from Google Sheets.

## Endpoints

### Create Test Assignment

```
POST /powerpath/test-assignments
```

Creates a standalone test-out assignment for a student.

**Request Body:**
```json
{
  "student": "student-123",
  "subject": "Math",
  "grade": "5",
  "testName": "Optional display name"
}
```

**Response:**
```json
{
  "assignmentId": "assign-123",
  "lessonId": "lesson-456",
  "resourceId": "resource-789"
}
```

**Usage:**
```python
from timeback import Timeback
from timeback.models.request import TimebackCreateTestAssignmentRequest
from timeback.enums import TimebackSubject, TimebackGrade

client = Timeback()

request = TimebackCreateTestAssignmentRequest(
    student="student-123",
    subject=TimebackSubject.MATH,
    grade=TimebackGrade.GRADE_5,
    testName="Unit 5 Assessment",
)

response = client.powerpath.create_test_assignment(request)
print(f"Created assignment: {response.assignmentId}")
```

---

### List Student Test Assignments

```
GET /powerpath/test-assignments
```

Returns paginated test assignments for a specific student.

**Query Parameters:**
| Parameter | Required | Description |
|-----------|----------|-------------|
| student | Yes | Student sourcedId |
| limit | No | Max items (1-3000, default 100) |
| offset | No | Items to skip (default 0) |
| status | No | Filter by status |
| subject | No | Filter by subject |
| grade | No | Filter by grade |

**Usage:**
```python
response = client.powerpath.list_student_test_assignments(
    student="student-123",
    status=TimebackTestAssignmentStatus.IN_PROGRESS,
)

for assignment in response.testAssignments:
    print(f"{assignment.sourcedId}: {assignment.assignmentStatus}")
```

---

### List All Test Assignments (Admin)

```
GET /powerpath/test-assignments/admin
```

Returns paginated test assignments across all students (admin view).

**Usage:**
```python
response = client.powerpath.list_all_test_assignments(
    limit=50,
    subject=TimebackSubject.READING,
)
```

---

### Create Bulk Test Assignments

```
POST /powerpath/test-assignments/bulk
```

Creates multiple test assignments in one request. All-or-nothing operation.

**Request Body:**
```json
{
  "items": [
    { "student": "student-1", "subject": "Math", "grade": "5" },
    { "student": "student-2", "subject": "Reading", "grade": "3" }
  ]
}
```

**Usage:**
```python
from timeback.models.request import (
    TimebackBulkTestAssignmentsRequest,
    TimebackBulkTestAssignmentItem,
)

request = TimebackBulkTestAssignmentsRequest(
    items=[
        TimebackBulkTestAssignmentItem(
            student="student-1",
            subject=TimebackSubject.MATH,
            grade=TimebackGrade.GRADE_5,
        ),
        TimebackBulkTestAssignmentItem(
            student="student-2",
            subject=TimebackSubject.READING,
            grade=TimebackGrade.GRADE_3,
        ),
    ]
)

response = client.powerpath.create_bulk_test_assignments(request)
if response.success:
    print(f"Created {len(response.results)} assignments")
else:
    for error in response.errors:
        print(f"Row {error.row}: {error.message}")
```

---

### Import Test Assignments from Google Sheets

```
POST /powerpath/test-assignments/import
```

Fetches a public Google Sheet and creates test assignments from its data.
Sheet must have columns: student, subject, grade.

**Usage:**
```python
from timeback.models.request import TimebackImportTestAssignmentsRequest

request = TimebackImportTestAssignmentsRequest(
    spreadsheetUrl="https://docs.google.com/spreadsheets/d/abc123",
    sheet="Assignments",
)

response = client.powerpath.import_test_assignments(request)
```

---

### Get Test Assignment

```
GET /powerpath/test-assignments/{id}
```

Returns a single test assignment by ID.

**Usage:**
```python
assignment = client.powerpath.get_test_assignment("assign-123")
print(f"Status: {assignment.assignmentStatus}")
```

---

### Update Test Assignment

```
PUT /powerpath/test-assignments/{id}
```

Updates a test assignment (currently only testName).

**Usage:**
```python
from timeback.models.request import TimebackUpdateTestAssignmentRequest

request = TimebackUpdateTestAssignmentRequest(testName="New Name")
client.powerpath.update_test_assignment("assign-123", request)
```

---

### Delete Test Assignment

```
DELETE /powerpath/test-assignments/{id}
```

Soft deletes a test assignment.

**Usage:**
```python
client.powerpath.delete_test_assignment("assign-123")
```

---

## Status Values

| Status | Description |
|--------|-------------|
| assigned | Test has been assigned but not started |
| in_progress | Student has started the test |
| completed | Test has been completed |
| failed | Student failed the test |
| expired | Test assignment has expired |
| cancelled | Test assignment was cancelled |

