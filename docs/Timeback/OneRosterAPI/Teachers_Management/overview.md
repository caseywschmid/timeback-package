# Teachers Management

## Endpoints

### `/ims/oneroster/rostering/v1p2/teachers/`

**GET** - `getAllTeachers`
- **Summary**: Get all Teachers
- **Description**: To get all Teachers on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

### `/ims/oneroster/rostering/v1p2/classes/{classSourcedId}/teachers`

**GET** - `getTeachersForClass`
- **Summary**: Get teachers for a Class
- **Description**: To get all teachers assigned to a specific Class. If the corresponding record cannot be located, the api will return a 404 error code and message 'Class not found.'
- **Parameters**: classSourcedId (path), fields, limit, offset, sort, orderBy, filter, search

**POST** - `addTeacherToClass`
- **Summary**: Add a teacher to a Class
- **Description**: Enrolls a teacher to a specific Class. The responding system must return the set of sourcedIds that have been allocated to the newly created enrollment record.
- **Parameters**: classSourcedId (path), Request body with enrollment object

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

### `/ims/oneroster/rostering/v1p2/teachers/{sourcedId}`

**GET** - `getTeacher`
- **Summary**: Get a specific Teacher
- **Description**: To get a specific Teacher on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'Teacher not found.'
- **Parameters**: sourcedId (path), fields


### `/ims/oneroster/rostering/v1p2/teachers/{teacherSourcedId}/classes`

**GET** - `getClassesForTeacher`
- **Summary**: Get Classes for a Teacher
- **Description**: To get the set of Classes a Teacher is enrolled in. If the specified teacher cannot be identified within the service provider, the api will return a 404 error code and message 'Teacher not found.'
- **Parameters**: teacherSourcedId (path), fields, limit, offset, sort, orderBy, filter, search
