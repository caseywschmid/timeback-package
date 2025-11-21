# Line Items Management

## Endpoints

### `/ims/oneroster/gradebook/v1p2/lineItems/`

**GET** - `getAllLineItems`
- **Summary**: Get all Line Items
- **Description**: Get all of the Line Items on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

**POST** - `createLineItem`
- **Summary**: Create a Line Item
- **Description**: To create a new Line Item. The responding system must return the set of sourcedIds that have been allocated to the newly created Line Item records.
- **Parameters**: Request body with lineItem object

### `/ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}`

**GET** - `getLineItem`
- **Summary**: Get a Line Item
- **Description**: Get a specific Line Item on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'Line item not found.'
- **Parameters**: sourcedId (path), fields

**PUT** - `putLineItem`
- **Summary**: Update or Create a Line Item
- **Description**: To update an existing Line Item or create a new one if it doesn't exist. The sourcedId for the record is supplied by the requesting system.
- **Parameters**: sourcedId (path), Request body with lineItem object

**DELETE** - `deleteLineItem`
- **Summary**: Delete a Line Item
- **Description**: Perform a soft delete on a specific Line Item on the service provider. This operation changes the status of the Line Item to 'tobedeleted'.
- **Parameters**: sourcedId (path)

### `/ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}/results`

**POST** - `createResultForLineItem`
- **Summary**: Create a Result for a Line Item
- **Description**: To create a new result for a specific Line Item. The responding system must return the set of sourcedIds that have been allocated to the newly created result records. If the corresponding record cannot be located, the api will return a 404 error code and message 'Line item not found.'
- **Parameters**: sourcedId (path), Request body with results array

### `/ims/oneroster/gradebook/v1p2/schools/{sourcedId}/lineItems`

**GET** - `getLineItemsForSchool`
- **Summary**: Get Line Items for a School
- **Description**: Get the set of lineItems on the service provider for a specific school. If the corresponding record cannot be located, the api will return a 404 error code and message 'School not found.'
- **Parameters**: sourcedId (path), fields, limit, offset, sort, orderBy, filter, search

**POST** - `createLineItemsForSchool`
- **Summary**: Create Line Items for a School
- **Description**: To create a set of lineItems for a specific school. The responding system must return the set of sourcedIds that have been allocated to the newly created lineItem records. If the corresponding record cannot be located, the api will return a 404 error code and message 'School not found.'
- **Parameters**: sourcedId (path), Request body with lineItems array
