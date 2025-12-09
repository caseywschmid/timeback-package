# Academic Sessions Management

This section covers the OneRoster API endpoints for managing academic sessions.

## Endpoints

### `/ims/oneroster/rostering/v1p2/academicSessions/`

**GET** - `getAllAcademicSessions`
- **Summary**: Get all Academic Sessions
- **Description**: To get all Academic Sessions on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

**POST** - `postAcademicSession`
- **Summary**: Create an Academic Session
- **Description**: To create a new academic session. The responding system must return the set of sourcedIds that have been allocated to the newly created academicSession record.
- **Parameters**: academicSession (request body)

### `/ims/oneroster/rostering/v1p2/academicSessions/{sourcedId}`

**GET** - `getAcademicSession`
- **Summary**: Get a specific Academic Session
- **Description**: Get a specific Academic Session on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'Academic session not found.'
- **Parameters**: sourcedId (path), fields

**PUT** - `putAcademicSession`
- **Summary**: Update an Academic Session
- **Description**: To update an existing Academic Session. The sourcedId for the record to be updated is supplied by the requesting system.
- **Parameters**: sourcedId (path), academicSession (request body)

**DELETE** - `deleteAcademicSession`
- **Summary**: Delete an Academic Session
- **Description**: Perform a soft delete on a specific Academic Session on the service provider. This operation changes the status of the Academic Session to 'tobedeleted'.
- **Parameters**: sourcedId (path)
