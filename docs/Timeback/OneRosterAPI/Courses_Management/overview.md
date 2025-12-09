# Courses Management

This section covers the OneRoster API endpoints for managing courses.

## Endpoints

### `/ims/oneroster/rostering/v1p2/courses/`

**GET** - `getAllCourses`
- **Summary**: Get All Courses
- **Description**: To get all Courses on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

**POST** - `createCourse`
- **Summary**: Create a Course
- **Description**: To create a new Course. The responding system must return the set of sourcedIds that have been allocated to the newly created course record.
- **Parameters**: course (request body)

### `/ims/oneroster/rostering/v1p2/courses/{courseSourcedId}/classes`

**GET** - `getClassesForCourse`
- **Summary**: Get Classes for a Course
- **Description**: To get all Classes associated with a specific Course. If the corresponding record cannot be located, the api will return a 404 error code and message 'Course not found.'
- **Parameters**: courseSourcedId (path), fields, limit, offset, sort, orderBy, filter, search

### `/ims/oneroster/rostering/v1p2/courses/{sourcedId}`

**GET** - `getCourse`
- **Summary**: Get a specific Course
- **Description**: Get a specific Course on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'Course not found.'
- **Parameters**: sourcedId (path), fields

**PUT** - `putCourse`
- **Summary**: Update a Course
- **Description**: To update an existing Course. The sourcedId for the record to be updated is supplied by the requesting system.
- **Parameters**: sourcedId (path), course (request body)

**DELETE** - `deleteCourse`
- **Summary**: Delete a Course
- **Description**: Perform a soft delete on a specific Course on the service provider. This operation changes the status of the Course to 'tobedeleted'.
- **Parameters**: sourcedId (path)

### `/ims/oneroster/rostering/v1p2/courses/component-resources`

**GET** - `getAllComponentResources`
- **Summary**: Get all Component Resources
- **Description**: To get all Component Resources on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

**POST** - `createComponentResource`
- **Summary**: Create Component Resource
- **Description**: To create a new Component Resource. The responding system must return the set of sourcedIds that have been allocated to the newly created componentResource record.
- **Parameters**: componentResource (request body)

### `/ims/oneroster/rostering/v1p2/courses/component-resources/{sourcedId}`

**GET** - `getComponentResource`
- **Summary**: Get a specific Component Resource
- **Description**: Get a specific Component Resource on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'Component Resource not found.'
- **Parameters**: sourcedId (path), fields

**PUT** - `putComponentResource`
- **Summary**: Update a Component Resource
- **Description**: To update an existing Component Resource. The sourcedId for the record to be updated is supplied by the requesting system.
- **Parameters**: sourcedId (path), componentResource (request body)

**DELETE** - `deleteComponentResource`
- **Summary**: Delete a Component Resource
- **Description**: Perform a soft delete on a specific Component Resource on the service provider. This operation changes the status of the Component Resource to 'tobedeleted'.
- **Parameters**: sourcedId (path)

### `/ims/oneroster/rostering/v1p2/courses/components`

**GET** - `getAllCourseComponents`
- **Summary**: Get all Course Components
- **Description**: To get all Course Components on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

**POST** - `createCourseComponent`
- **Summary**: Create Course Component
- **Description**: Used when creating a new course component or module
- **Parameters**: courseComponent (request body)

### `/ims/oneroster/rostering/v1p2/courses/components/{sourcedId}`

**GET** - `getCourseComponent`
- **Summary**: Get a specific Course Component
- **Description**: Get a specific Course Component on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'Course Component not found.'
- **Parameters**: sourcedId (path), fields

**PUT** - `putCourseComponent`
- **Summary**: Update a Course Component
- **Description**: To update an existing Course Component. The sourcedId for the record to be updated is supplied by the requesting system.
- **Parameters**: sourcedId (path), courseComponent (request body)

**DELETE** - `deleteCourseComponent`
- **Summary**: Delete a Course Component
- **Description**: Perform a soft delete on a specific Course Component on the service provider. This operation changes the status of the Course Component to 'tobedeleted'.
- **Parameters**: sourcedId (path)

### `/ims/oneroster/rostering/v1p2/courses/structure`

**POST** - `createCourseStructure`
- **Summary**: Create Course Structure from QTI Tests
- **Description**: Create a course structure from QTI tests
- **Parameters**: courseStructure (request body), course (request body)

### `/ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/courses`

**GET** - `getCoursesForSchool`
- **Summary**: Get all Courses for a School
- **Description**: To get all Courses for a School on the service provider. If the specified school cannot be identified within the service provider, the api will return a 404 error code and message 'School not found.'
- **Parameters**: schoolSourcedId (path), fields, limit, offset, sort, orderBy, filter, search
