# One Roster Endpoints

## Academic Sessions Management

### Description

This enables the management of academic sessions i.e. periods of academic activity such as terms, semesters, grading periods, and school years. Academic sessions can have hierarchical relationships (e.g., a school year containing terms, terms containing grading periods).

### Endpoints

- /ims/oneroster/rostering/v1p2/academicSessions/
- /ims/oneroster/rostering/v1p2/academicSessions/{sourcedId}

## Assessment Line Items Management

### Description

This enables the management of the assessment line items i.e. line items that are used to store results about tests/assessments and where these test/assessments are not aligned to a class.

### Endpoints

- /ims/oneroster/gradebook/v1p2/assessmentLineItems/
- /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}

## Assessment Results Management

### Description

This enables the management of the assessment results i.e. results that are used to store scores for tests/assessments and where these test/assessments are not aligned to a class.

### Endpoints

- /ims/oneroster/gradebook/v1p2/assessmentResults/
- /ims/oneroster/gradebook/v1p2/assessmentResults/{sourcedId}

## Categories Management

### Description

This enables the management of Categories i.e. collections of LineItems.

### Endpoints

- /ims/oneroster/gradebook/v1p2/categories/
- /ims/oneroster/gradebook/v1p2/categories/{sourcedId}

## Classes Management

### Description

This enables the management of Classes i.e. scheduled learning of courses, with respect to scoreScales. For this service this is the collection of operations that provide gradebook data in the context of a class identifier.

### Endpoints

- /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/academicSessions/{academicSessionSourcedId}/results
- /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/lineItems
- /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/lineItems/{lineItemSourcedId}/results
- /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/students/{studentSourcedId}/results
- /ims/oneroster/gradebook/v1p2/classes/{sourcedId}/categories
- /ims/oneroster/gradebook/v1p2/classes/{sourcedId}/lineItems
- /ims/oneroster/gradebook/v1p2/classes/{sourcedId}/results
- /ims/oneroster/gradebook/v1p2/classes/{sourcedId}/scoreScales
- /ims/oneroster/rostering/v1p2/classes/
- /ims/oneroster/rostering/v1p2/classes/{sourcedId}
- /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes
- /ims/oneroster/rostering/v1p2/users/{userSourcedId}/classes
- /ims/oneroster/rostering/v1p2/terms/{termSourcedId}/classes
- /ims/oneroster/rostering/v1p2/classes/{classSourcedId}/teachers
- /ims/oneroster/rostering/v1p2/teachers/{teacherSourcedId}/classes
- /ims/oneroster/rostering/v1p2/classes/{classSourcedId}/students
- /ims/oneroster/rostering/v1p2/students/{studentSourcedId}/classes

## Course Component Resources Management

### Description

This enables the management of Course Component Resources i.e. resources for a course component.

### Endpoints

- /ims/oneroster/rostering/v1p2/courses/component-resources
- /ims/oneroster/rostering/v1p2/courses/component-resources/{sourcedId}

## Course Components Management

### Description

This enables the management of Course Components i.e. components of a course.

### Endpoints

- /ims/oneroster/rostering/v1p2/courses/components
- /ims/oneroster/rostering/v1p2/courses/components/{sourcedId}

## Courses Management

### Description

This enables the management of Courses i.e. programme of study.

### Endpoints

- /ims/oneroster/rostering/v1p2/courses/
- /ims/oneroster/rostering/v1p2/courses/{courseSourcedId}/classes
- /ims/oneroster/rostering/v1p2/courses/{sourcedId}
- /ims/oneroster/rostering/v1p2/courses/component-resources
- /ims/oneroster/rostering/v1p2/courses/component-resources/{sourcedId}
- /ims/oneroster/rostering/v1p2/courses/components
- /ims/oneroster/rostering/v1p2/courses/components/{sourcedId}
- /ims/oneroster/rostering/v1p2/courses/structure
- /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/courses

## Demographics Management

### Description

This enables the management of demographics information (each assigned to a specific user). The sourcedIds for the user and the demographics records should be the same.

### Endpoints

- /ims/oneroster/rostering/v1p2/demographics/
- /ims/oneroster/rostering/v1p2/demographics/{sourcedId}

## Enrollments Management

### Description

This enables the management of the enrollments of users (teachers, students, etc.) on classes supplied by schools.

### Endpoints

- /ims/oneroster/rostering/v1p2/enrollments/
- /ims/oneroster/rostering/v1p2/enrollments/{sourcedId}
- /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes/{classSourcedId}/enrollments
- /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/enrollments

## Grading Periods Management

### Description

This enables the management of grading periods i.e. specific academic sessions.

### Endpoints

- /ims/oneroster/rostering/v1p2/gradingPeriods/
- /ims/oneroster/rostering/v1p2/gradingPeriods/{sourcedId}
- /ims/oneroster/rostering/v1p2/terms/{termSourcedId}/gradingPeriods

## Line Items Management

### Description

This enables the management of lineItems i.e. the set of results for the assessment of some activity.

### Endpoints

- /ims/oneroster/gradebook/v1p2/lineItems/
- /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}
- /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}/results
- /ims/oneroster/gradebook/v1p2/schools/{sourcedId}/lineItems

## Organizations Management

### Description

This enables the management of orgs i.e. an organization involved in the learning in some form or other.

### Endpoints

- /ims/oneroster/rostering/v1p2/orgs/
- /ims/oneroster/rostering/v1p2/orgs/{sourcedId}

## Resources Management

### Description

This enables the management of resources

### Endpoints

- /ims/oneroster/resources/v1p2/resources/
- /ims/oneroster/resources/v1p2/resources/{sourcedId}
- /ims/oneroster/resources/v1p2/resources/classes/{classSourcedId}/resources
- /ims/oneroster/resources/v1p2/resources/courses/{courseSourcedId}/resources
- /ims/oneroster/resources/v1p2/resources/export/{sourceId}
- /ims/oneroster/resources/v1p2/resources/users/{userSourcedId}/resources

## Results Management

### Description

This enables the management of results i.e. the score allocated to a learner from the assessent of a learning activity. Results are collected as a set of 'lineItems'.

### Endpoints

- /ims/oneroster/gradebook/v1p2/results/
- /ims/oneroster/gradebook/v1p2/results/{sourcedId}

## Schools Management

### Description

This enables the management of information about schools with respect to scoreScales. A school is a type of 'org'. For this service this is the collection of operations that provide gradebook data in the context of a school identifier.

### Endpoints

- /ims/oneroster/rostering/v1p2/schools/
- /ims/oneroster/rostering/v1p2/schools/{sourcedId}
- /ims/oneroster/gradebook/v1p2/schools/{sourcedId}/lineItems
- /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/terms
- /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes/{classSourcedId}/teachers
- /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/teachers
- /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes/{classSourcedId}/students
- /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/students
- /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes/{classSourcedId}/enrollments
- /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/enrollments
- /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/courses

## Score Scales Management

### Description

This enables the management of scoreScales i.e. the set of scales for the results and lineItems.

### Endpoints

- /ims/oneroster/gradebook/v1p2/scoreScales/
- /ims/oneroster/gradebook/v1p2/scoreScales/{sourcedId}
- /ims/oneroster/gradebook/v1p2/schools/{sourcedId}/scoreScales

## Students Management

### Description

This enables the management of information about students (a student is a type of 'user').

### Endpoints

- /ims/oneroster/rostering/v1p2/classes/{classSourcedId}/students
- /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes/{classSourcedId}/students
- /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/students
- /ims/oneroster/rostering/v1p2/students/
- /ims/oneroster/rostering/v1p2/students/{sourcedId}
- /ims/oneroster/rostering/v1p2/students/{studentSourcedId}/classes

## Teachers Management

### Description

This enables the management of information about teachers (a teacher is a type of 'user').

### Endpoints

- /ims/oneroster/rostering/v1p2/classes/{classSourcedId}/teachers
- /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes/{classSourcedId}/teachers
- /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/teachers
- /ims/oneroster/rostering/v1p2/teachers/
- /ims/oneroster/rostering/v1p2/teachers/{sourcedId}
- /ims/oneroster/rostering/v1p2/teachers/{teacherSourcedId}/classes

## Terms Management

### Description

This enables the management of information about terms (a term is a type of 'academicSession').

### Endpoints

- /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/terms
- /ims/oneroster/rostering/v1p2/terms/
- /ims/oneroster/rostering/v1p2/terms/{sourcedId}
- /ims/oneroster/rostering/v1p2/terms/{termSourcedId}/classes
- /ims/oneroster/rostering/v1p2/terms/{termSourcedId}/gradingPeriods

## Users Management

### Description

This enables the management of information about users (including students and teachers).

### Endpoints

- /ims/oneroster/rostering/v1p2/users/
- /ims/oneroster/rostering/v1p2/users/{sourcedId}
- /ims/oneroster/rostering/v1p2/users/{sourcedId}/demographics
- /ims/oneroster/rostering/v1p2/users/{userId}/agentFor
- /ims/oneroster/rostering/v1p2/users/{userId}/agents
- /ims/oneroster/rostering/v1p2/users/{userId}/agents/{agentSourcedId}
- /ims/oneroster/rostering/v1p2/users/{userId}/credentials
- /ims/oneroster/rostering/v1p2/users/{userId}/credentials/{credentialId}/decrypt
- /ims/oneroster/rostering/v1p2/users/{userSourcedId}/classes












