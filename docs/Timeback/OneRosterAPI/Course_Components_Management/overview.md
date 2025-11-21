# Course Components Management

This section covers the OneRoster API endpoints for managing course components.

## Endpoints

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
