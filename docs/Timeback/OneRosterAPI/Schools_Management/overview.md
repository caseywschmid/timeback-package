# Schools Management

## Endpoints

### `/ims/oneroster/rostering/v1p2/schools/`

**GET** - `getAllSchools`
- **Summary**: Get all Schools
- **Description**: To get all Schools on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

**POST** - `createSchool`
- **Summary**: Create a new School
- **Description**: To create a new School. The responding system must return the set of sourcedIds that have been allocated to the newly created school record.
- **Parameters**: Request body with org object

### `/ims/oneroster/rostering/v1p2/schools/{sourcedId}`

**GET** - `getSchool`
- **Summary**: Get a specific School
- **Description**: Get a specific School on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'School not found.'
- **Parameters**: sourcedId (path), fields

**PUT** - `updateSchool`
- **Summary**: Update a School
- **Description**: To update an existing School. The sourcedId for the record to be updated is supplied by the requesting system.
- **Parameters**: sourcedId (path), Request body with org object

**DELETE** - `deleteSchool`
- **Summary**: Delete a School
- **Description**: Perform a soft delete on a specific School on the service provider. This operation changes the status of the School to 'tobedeleted'.
- **Parameters**: sourcedId (path)

### `/ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes/{classSourcedId}/teachers`

**GET** - `getTeachersForClassInSchool`
- **Summary**: Get Teachers for a specific Class in a School
- **Description**: To get all Teachers for a Class in a School on the service provider. If the specified school and/or class cannot be identified within the service provider, the api will return a 404 error code and message 'School or class not found.'
- **Parameters**: schoolSourcedId (path), classSourcedId (path), fields, limit, offset, sort, orderBy, filter, search

### `/ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/teachers`

**GET** - `getTeachersForSchool`
- **Summary**: Get all teachers for a school
- **Description**: To get all Teachers for a School on the service provider. If the specified school cannot be identified within the service provider, the api will return a 404 error code and message 'School not found.'
- **Parameters**: schoolSourcedId (path), fields, limit, offset, sort, orderBy, filter, search

### `/ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes/{classSourcedId}/students`

**GET** - `getStudentsForClassInSchool`
- **Summary**: Get Students for a specific Class in a School
- **Description**: To get all Students for a Class in a School on the service provider. If the specified school and/or class cannot be identified within the service provider, the api will return a 404 error code and message 'School or class not found.'
- **Parameters**: schoolSourcedId (path), classSourcedId (path), fields, limit, offset, sort, orderBy, filter, search

### `/ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/courses`

**GET** - `getCoursesForSchool`
- **Summary**: Get all Courses for a School
- **Description**: To get all Courses for a School on the service provider. If the specified school cannot be identified within the service provider, the api will return a 404 error code and message 'School not found.'
- **Parameters**: schoolSourcedId (path), fields, limit, offset, sort, orderBy, filter, search
