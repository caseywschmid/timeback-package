# Enrollments Management

## Endpoints

### `/ims/oneroster/rostering/v1p2/enrollments/`

**GET** - `getAllEnrollments`
- **Summary**: Get all Enrollments
- **Description**: To get all Enrollments on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

**POST** - `createEnrollment`
- **Summary**: Create a new Enrollment
- **Description**: To create a new Enrollment. The responding system must return the set of sourcedIds that have been allocated to the newly created enrollment record.
- **Parameters**: Request body with enrollment object

### `/ims/oneroster/rostering/v1p2/enrollments/{sourcedId}`

**GET** - `getEnrollment`
- **Summary**: Get a specific Enrollment
- **Description**: Get a specific Enrollment on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'Enrollment not found.'
- **Parameters**: sourcedId (path), fields

**PUT** - `updateEnrollment`
- **Summary**: Update an Enrollment
- **Description**: To update an existing Enrollment. The sourcedId for the record to be updated is supplied by the requesting system.
- **Parameters**: sourcedId (path), Request body with enrollment object

**PATCH** - `partiallyUpdateEnrollment`
- **Summary**: Partially Update an Enrollment
- **Description**: To partially update an existing Enrollment with metadata merging support. The sourcedId for the record to be updated is supplied by the requesting system. Metadata will be merged with existing values.
- **Parameters**: sourcedId (path), Request body with enrollment object

**DELETE** - `deleteEnrollment`
- **Summary**: Delete an Enrollment
- **Description**: Perform a soft delete on a specific Enrollment on the service provider. This operation changes the status of the Enrollment to 'tobedeleted'.
- **Parameters**: sourcedId (path)

### `/ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes/{classSourcedId}/enrollments`

**GET** - `getEnrollmentsForClassInSchool`
- **Summary**: Get Enrollments for a specific Class in a School
- **Description**: To get all Enrollments for a Class in a School on the service provider. If the specified school and/or class cannot be identified within the service provider, the api will return a 404 error code and message 'School or class not found.'
- **Parameters**: schoolSourcedId (path), classSourcedId (path), fields, limit, offset, sort, orderBy, filter, search

### `/ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/enrollments`

**GET** - `getEnrollmentsForSchool`
- **Summary**: Get all Enrollments for a School
- **Description**: To get all Enrollments for a School on the service provider. If the specified school cannot be identified within the service provider, the api will return a 404 error code and message 'School not found.'
- **Parameters**: schoolSourcedId (path), fields, limit, offset, sort, orderBy, filter, search
