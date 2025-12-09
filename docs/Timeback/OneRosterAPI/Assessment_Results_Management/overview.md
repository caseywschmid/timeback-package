# Assessment Results Management

## Endpoints

### `/ims/oneroster/gradebook/v1p2/assessmentResults/`

**GET** - `getAllAssessmentResults`
- **Summary**: Get all Assessment Results
- **Description**: Get all of the Assessment Results on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

**POST** - `createAssessmentResult`
- **Summary**: Create an Assessment Result
- **Description**: To create an Assessment Result. The responding system must return the set of sourcedIds that have been allocated to the newly created assessmentResult record. An Assessment Line Item sourcedId and Student sourcedId MUST be provided when creating an assessmentResult.
- **Parameters**: Request body with assessmentResult object

### `/ims/oneroster/gradebook/v1p2/assessmentResults/{sourcedId}`

**GET** - `getAssessmentResult`
- **Summary**: Get an Assessment Result
- **Description**: Get a specific Assessment Result on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'Assessment result not found.'
- **Parameters**: sourcedId (path), fields

**PUT** - `putAssessmentResult`
- **Summary**: Update or Create an Assessment Result
- **Description**: To update an existing Assessment Result or create a new one if it doesn't exist. The sourcedId for the record is supplied by the requesting system.
- **Parameters**: sourcedId (path), Request body with assessmentResult object

**PATCH** - `patchAssessmentResult`
- **Summary**: Partially Update an Assessment Result
- **Description**: To partially update an existing Assessment Result with metadata merging support.
- **Parameters**: sourcedId (path), Request body with assessmentResult object

**DELETE** - `deleteAssessmentResult`
- **Summary**: Delete an Assessment Result
- **Description**: Perform a soft delete on a specific Assessment Result on the service provider. This operation changes the status of the Assessment Result to 'tobedeleted'.
- **Parameters**: sourcedId (path)
