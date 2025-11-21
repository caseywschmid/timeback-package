# Classes Management

## Endpoints

### `/ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/academicSessions/{academicSessionSourcedId}/results`

**POST** - `postResultsForAcademicSessionForClass`
- **Summary**: Create Results for an Academic Session for a Class
- **Description**: To create a set of results for a specific academic session and specific class. The responding system must return the set of sourcedIds that have been allocated to the newly created result records. If the corresponding record cannot be located, the api will return a 404 error code and message 'Class or academic session not found.'
- **Parameters**: classSourcedId (path), academicSessionSourcedId (path), Request body with results array

### `/ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/lineItems`

**POST** - `postLineItemsForClass`
- **Summary**: Create Line Items for a Class
- **Description**: To create a set of lineItems for a specific class. The responding system must return the set of sourcedIds that have been allocated to the newly created lineItem records. If the corresponding record cannot be located, the api will return a 404 error code and message 'Class not found.'
- **Parameters**: classSourcedId (path), Request body with lineItems array

### `/ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/lineItems/{lineItemSourcedId}/results`

**GET** - `getResultsForLineItemForClass`
- **Summary**: Get Results for a Line Item for a Class
- **Description**: Get the set of results on the service provider for a specific lineItem and for a specific class. If the corresponding record cannot be located, the api will return a 404 error code and message 'Class or line item not found.'
- **Parameters**: classSourcedId (path), lineItemSourcedId (path), fields, limit, offset, sort, orderBy, filter, search

### `/ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/students/{studentSourcedId}/results`

**GET** - `getResultsForStudentForClass`
- **Summary**: Get Results for a Student for a Class
- **Description**: Get the set of results on the service provider for a specific student and for a specific class. If the corresponding record cannot be located, the api will return a 404 error code and message 'Class or student not found.'
- **Parameters**: classSourcedId (path), studentSourcedId (path), fields, limit, offset, sort, orderBy, filter, search

### `/ims/oneroster/gradebook/v1p2/classes/{sourcedId}/categories`

**GET** - `getCategoriesForClass`
- **Summary**: Get Categories for a Class
- **Description**: Get the set of categories on the service provider for a specific class. If the corresponding record cannot be located, the api will return a 404 error code and message 'Class not found.'
- **Parameters**: sourcedId (path), fields, limit, offset, sort, orderBy, filter, search

### `/ims/oneroster/gradebook/v1p2/classes/{sourcedId}/lineItems`

**GET** - `getLineItemsForClass`
- **Summary**: Get Line Items for a Class
- **Description**: Get the set of lineItems on the service provider for a specific class. If the corresponding record cannot be located, the api will return a 404 error code and message 'Class not found.'
- **Parameters**: sourcedId (path), fields, limit, offset, sort, orderBy, filter, search

### `/ims/oneroster/gradebook/v1p2/classes/{sourcedId}/results`

**GET** - `getResultsForClass`
- **Summary**: Get Results for a Class
- **Description**: Get the set of results on the service provider for a specific class. If the corresponding record cannot be located, the api will return a 404 error code and message 'Class not found.'
- **Parameters**: sourcedId (path), fields, limit, offset, sort, orderBy, filter, search

### `/ims/oneroster/gradebook/v1p2/classes/{sourcedId}/scoreScales`

**GET** - `getScoreScalesForClass`
- **Summary**: Get Score Scales for a Class
- **Description**: Get the set of scoreScales on the service provider for a specific class. If the corresponding record cannot be located, the api will return a 404 error code and message 'Class not found.'
- **Parameters**: sourcedId (path), fields, limit, offset, sort, orderBy, filter, search

### `/ims/oneroster/rostering/v1p2/classes/`

**GET** - `getAllClasses`
- **Summary**: Get all Classes
- **Description**: To get all Classes on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

**POST** - `createClass`
- **Summary**: Create a new Class
- **Description**: To create a new Class. The responding system must return the set of sourcedIds that have been allocated to the newly created class record.
- **Parameters**: Request body with class object

### `/ims/oneroster/rostering/v1p2/classes/{sourcedId}`

**GET** - `getClass`
- **Summary**: Get a specific class
- **Description**: Get a specific Class on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'Class not found.'
- **Parameters**: sourcedId (path), fields

**PUT** - `updateClass`
- **Summary**: Update a Class
- **Description**: To update an existing Class. The sourcedId for the record to be updated is supplied by the requesting system.
- **Parameters**: sourcedId (path), Request body with class object

**DELETE** - `deleteClass`
- **Summary**: Delete a Class
- **Description**: Perform a soft delete on a specific Class on the service provider. This operation changes the status of the Class to 'tobedeleted'.
- **Parameters**: sourcedId (path)

### `/ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes`

**GET** - `getClassesForSchool`
- **Summary**: Get all Classes for a School
- **Description**: To get all Classes for a School on the service provider. If the specified school cannot be identified within the service provider, the api will return a 404 error code and message 'School not found.'
- **Parameters**: schoolSourcedId (path), fields, limit, offset, sort, orderBy, filter, search

### `/ims/oneroster/rostering/v1p2/classes/{classSourcedId}/teachers`

**GET** - `getTeachersForClass`
- **Summary**: Get teachers for a Class
- **Description**: To get all teachers assigned to a specific Class. If the corresponding record cannot be located, the api will return a 404 error code and message 'Class not found.'
- **Parameters**: classSourcedId (path), fields, limit, offset, sort, orderBy, filter, search

**POST** - `addTeacherToClass`
- **Summary**: Add a teacher to a Class
- **Description**: Enrolls a teacher to a specific Class. The responding system must return the set of sourcedIds that have been allocated to the newly created enrollment record.
- **Parameters**: classSourcedId (path), Request body with enrollment object

### `/ims/oneroster/rostering/v1p2/classes/{classSourcedId}/students`

**GET** - `getStudentsForClass`
- **Summary**: Get students for a Class
- **Description**: To get all students enrolled in a specific Class. If the corresponding record cannot be located, the api will return a 404 error code and message 'Class not found.'
- **Parameters**: classSourcedId (path), fields, limit, offset, sort, orderBy, filter, search

**POST** - `addStudentToClass`
- **Summary**: Add a student to a Class
- **Description**: Enrolls a student in a specific Class. The responding system must return the set of sourcedIds that have been allocated to the newly created enrollment record.
- **Parameters**: classSourcedId (path), Request body with enrollment object
