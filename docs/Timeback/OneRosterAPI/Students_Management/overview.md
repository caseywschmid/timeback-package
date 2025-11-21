# Students Management

## Endpoints

### `/ims/oneroster/rostering/v1p2/students/`

**GET** - `getAllStudents`
- **Summary**: Get all Students
- **Description**: To get all Students on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

### `/ims/oneroster/rostering/v1p2/students/{sourcedId}`

**GET** - `getStudent`
- **Summary**: Get a specific Student
- **Description**: To get a specific Student on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'Student not found.'
- **Parameters**: sourcedId (path), fields


### `/ims/oneroster/rostering/v1p2/students/{studentSourcedId}/classes`

**GET** - `getClassesForStudent`
- **Summary**: Get Classes for a Student
- **Description**: To get the set of Classes related to a specific Student. If the specified student cannot be identified within the service provider, the api will return a 404 error code and message 'Student not found.'
- **Parameters**: studentSourcedId (path), fields, limit, offset, sort, orderBy, filter, search


