# Assessment Line Items Management

## Endpoints

### `/ims/oneroster/gradebook/v1p2/assessmentLineItems/`

**GET** - `getAllAssessmentLineItems`
- **Summary**: Get all Assessment Line Items
- **Description**: Get all of the Assessment Line Items on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

**POST** - `createAssessmentLineItem`
- **Summary**: Create an Assessment Line Item
- **Description**: To create an Assessment Line Item. The responding system must return the set of sourcedIds that have been allocated to the newly created assessmentLineItem record. A 'title' MUST be provided when creating an assessmentLineItem.
- **Parameters**: Request body with assessmentLineItem object

### `/ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}`

**GET** - `getAssessmentLineItem`
- **Summary**: Get an Assessment Line Item
- **Description**: Get a specific Assessment Line Item on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'Assessment line item not found.'
- **Parameters**: sourcedId (path), fields

**PUT** - `putAssessmentLineItem`
- **Summary**: Update or Create an Assessment Line Item
- **Description**: To update an existing Assessment Line Item or create a new one if it doesn't exist. The sourcedId for the record is supplied by the requesting system.
- **Parameters**: sourcedId (path), Request body with assessmentLineItem object

**PATCH** - `patchAssessmentLineItem`
- **Summary**: Partially Update an Assessment Line Item
- **Description**: To partially update an existing Assessment Line Item with metadata merging support.
- **Parameters**: sourcedId (path), Request body with assessmentLineItem object

**DELETE** - `deleteAssessmentLineItem`
- **Summary**: Delete an Assessment Line Item
- **Description**: Perform a soft delete on a specific Assessment Line Item on the service provider. This operation changes the status of the Assessment Line Item to 'tobedeleted'.
- **Parameters**: sourcedId (path)
