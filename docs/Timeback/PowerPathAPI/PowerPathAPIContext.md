# PowerPath API Endpoints

TimeBack PowerPath 100 API

# Authentication

All endpoints require authentication using the `Authorization: Bearer <token>` header.
The token can be obtained with:

```bash
curl -X POST https://alpha-auth-production-idp.auth.us-west-2.amazoncognito.com/oauth2/token \\
-H \"Content-Type: application/x-www-form-urlencoded\" \\
-d \"grant_type=client_credentials&client_id=<your-client-id>&client_secret=<your-client-secret>\"
```

Use the correct IDP server depending on the environment you're using:

- Production Server:
  https://alpha-auth-production-idp.auth.us-west-2.amazoncognito.com
- Staging Server:
  https://alpha-auth-development-idp.auth.us-west-2.amazoncognito.com
  Reach out to the platform team to get a client/secret pair for your application.

# Pagination

Our API uses offset pagination for list endpoints. Paginated responses include the following fields:

- `offset`: Offset for the next page of results
- `limit`: Number of items per page (default: 100, maximum: 3000)
  **Note:** While the OneRoster specification does not define a maximum limit, this implementation enforces a maximum of 3000 items per page to prevent abuse and ensure optimal performance.
  Example request:
  `GET /ims/oneroster/rostering/v1p2/users?offset=20&limit=20`
  All listing endpoints support offset pagination.

# Filtering

All listing endpoints support filtering using the `filter` query parameter, following 1EdTech's filtering specification.
The filter should be a string with the following format:
`?filter=[field][operator][value]`
Example request:
`GET /ims/oneroster/rostering/v1p2/users?filter=status='active'`
Example request with multiple filters:
`GET /ims/oneroster/rostering/v1p2/users?filter=status='active' AND name='John'`
**Filtering by nested relations is not supported**.

# Sorting

All listing endpoints support sorting using the `sort` and `orderBy` query parameters, following 1EdTech's sorting specification
Example request:
`GET /ims/oneroster/rostering/v1p2/users?sort=lastName&orderBy=asc`

# Proprietary Extensions

This implementation includes proprietary extensions that extend beyond the official OneRoster 1.2 specification to provide additional functionality.

## Search Parameter

In addition to the standard `filter` parameter, this implementation provides a `search` query parameter for simplified free-text searching:
`GET /ims/oneroster/rostering/v1p2/users?search=john`
**Purpose**: The `search` parameter enables convenient text-based queries across multiple fields simultaneously, whereas the standard `filter` parameter requires specifying exact field names and operators:
`

# Search parameter - searches across multiple fields automatically

GET /ims/oneroster/rostering/v1p2/users?search=john

# Equivalent using standard filter parameter

GET /ims/oneroster/rostering/v1p2/users?filter=givenName~'john' OR familyName~'john'
`The`search` parameter performs case-insensitive partial matching across predefined fields for each endpoint, providing a more user-friendly querying experience.

## OneRoster 1.2 Standard Parameters

The official OneRoster 1.2 specification defines these standard parameters:

- `limit` - pagination limit
- `offset` - pagination offset
- `sort` - field to sort by
- `orderBy` - sort direction (asc/desc)
- `filter` - filtering expression
- `fields` - field selection

## Affected Endpoints

The proprietary `search` parameter is available on the following endpoints:
**Rostering API**:

- `GET /ims/oneroster/rostering/v1p2/academicSessions/`
- `GET /ims/oneroster/rostering/v1p2/classes/`
- `GET /ims/oneroster/rostering/v1p2/classes/{classSourcedId}/students`
- `GET /ims/oneroster/rostering/v1p2/classes/{classSourcedId}/teachers`
- `GET /ims/oneroster/rostering/v1p2/courses/`
- `GET /ims/oneroster/rostering/v1p2/courses/{courseSourcedId}/classes`
- `GET /ims/oneroster/rostering/v1p2/demographics/`
- `GET /ims/oneroster/rostering/v1p2/enrollments/`
- `GET /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes/{classSourcedId}/students`
- `GET /ims/oneroster/rostering/v1p2/users/`
  **Gradebook API**:
- `GET /ims/oneroster/gradebook/v1p2/assessmentLineItems/`
- `GET /ims/oneroster/gradebook/v1p2/assessmentResults/`
- `GET /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/students/{studentSourcedId}/results`
- `GET /ims/oneroster/gradebook/v1p2/results/`
  **Resources API**:
- `GET /ims/oneroster/resources/v1p2/resources/`

## Parameter Usage Guide

### Filter Parameter

The standard `filter` parameter provides precise control over queries using these operators:

- `=` - Exact match
- `!=` - Not equal
- `~` - Contains (case-insensitive)
- `>`, `>=`, `<`, `<=` - Comparison operators
- `@` - In list (comma-separated values)

### Logical Operators

Combine multiple conditions in filter expressions:

- `AND` - Both conditions must be true
- `OR` - Either condition must be true

### Usage Examples

`bash

# Simple text search across multiple fields

GET /users?search=john

# Equivalent precise filtering

GET /users?filter=givenName~'john' OR familyName~'john'

# Complex filtering with multiple conditions

GET /users?filter=status='active' AND givenName~'john'

# Advanced filtering with different operators

GET /users?filter=dateLastModified>'2023-01-01' AND status='active'
`

## Search Fields by Endpoint

Different endpoints search across these predefined fields:

- **Users**: `givenName`, `familyName`, `email`
- **Courses**: `title`, `courseCode`
- **Classes**: `title`
- **Organizations**: `name`

## Interoperability Notes

The `search` parameter is a proprietary extension specific to this implementation. Other OneRoster-compliant systems may only support the standard `filter` parameter. When building applications that need to work with multiple OneRoster providers, consider using the standard filtering approach.

## Additional Schema Fields

### AssessmentLineItem Extensions

The AssessmentLineItem schema includes two proprietary fields that extend curriculum mapping capabilities:

#### Component Field

- **Field**: `component`
- **Type**: Object reference (`{ sourcedId: string }`)
- **Purpose**: Direct association between assessment line items and course components, enabling enhanced curriculum mapping and learning pathway tracking.

#### ComponentResource Field

- **Field**: `componentResource`
- **Type**: Object reference (`{ sourcedId: string }`)
- **Purpose**: Direct association between assessment line items and specific learning resources, supporting detailed content-to-assessment relationships and adaptive learning features.
  **Example Usage**:

```json
{
  "sourcedId": "assessment-123",
  "title": "Chapter 5 Quiz",
  "component": { "sourcedId": "component-456" },
  "componentResource": { "sourcedId": "resource-789" }
}
```

## Affected Endpoints

### Schema Extensions Availability

The proprietary schema fields are available in:
**Gradebook API**:

- `GET /ims/oneroster/gradebook/v1p2/assessmentLineItems/` - Returns assessmentLineItems with `component` and `componentResource` fields
- `GET /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}` - Returns individual assessmentLineItem with extended fields
- `POST /ims/oneroster/gradebook/v1p2/assessmentLineItems/` - Accepts `component` and `componentResource` in request body
- `PUT /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}` - Accepts extended fields for updates

## Test Assignments

/powerpath/test-assignments
/powerpath/test-assignments/{id}
/powerpath/test-assignments/admin
/powerpath/test-assignments/bulk
/powerpath/test-assignments/import

## Placement

/powerpath/placement/:studentId
/powerpath/placement/getAllPlacementTests
/powerpath/placement/getCurrentLevel
/powerpath/placement/getNextPlacementTest
/powerpath/placement/getSubjectProgress
/powerpath/placement/resetUserPlacement

## Screening

/powerpath/screening/results/{userId}
/powerpath/screening/session/{userId}
/powerpath/screening/session/reset
/powerpath/screening/tests/assign
/powerpath/createExternalPlacementTest
/powerpath/createExternalTestOut
/powerpath/createInternalTest
/powerpath/importExternalTestAssignmentResults
/powerpath/makeExternalTestAssignment
/powerpath/testOut

## Lesson Plans

/powerpath/lessonPlans/
/powerpath/lessonPlans/{courseId}/{userId}
/powerpath/lessonPlans/{courseId}/deleteAll
/powerpath/lessonPlans/{lessonPlanId}/operations
/powerpath/lessonPlans/{lessonPlanId}/operations/sync
/powerpath/lessonPlans/{lessonPlanId}/recreate
/powerpath/lessonPlans/course/{courseId}/sync
/powerpath/lessonPlans/getCourseProgress/{courseId}/student/{studentId}
/powerpath/lessonPlans/startTestOut
/powerpath/lessonPlans/tree/{lessonPlanId}
/powerpath/lessonPlans/tree/{lessonPlanId}/structure
/powerpath/lessonPlans/updateStudentItemResponse

/powerpath/syllabus/{courseSourcedId}
/powerpath/createNewAttempt
/powerpath/finalStudentAssessmentResponse
/powerpath/getAssessmentProgress
/powerpath/getAttempts
/powerpath/getNextQuestion
/powerpath/resetAttempt
/powerpath/updateStudentQuestionResponse
