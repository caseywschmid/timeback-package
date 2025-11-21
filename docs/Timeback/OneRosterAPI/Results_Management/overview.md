# Results Management

## Endpoints

### `/ims/oneroster/gradebook/v1p2/results/`

**GET** - `getAllResults`
- **Summary**: Get all Results
- **Description**: Get all of the results on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

**POST** - `createResult`
- **Summary**: Create a Result
- **Description**: To create a new result. The request body must include a `result` object with the following required fields: `lineItem` (with sourcedId), `student` (with sourcedId), `scoreStatus`, and `scoreDate`. The responding system must return the set of sourcedIds that have been allocated to the newly created result records.
- **Parameters**: Request body with result object

### `/ims/oneroster/gradebook/v1p2/results/{sourcedId}`

**GET** - `getResult`
- **Summary**: Get a Result
- **Description**: Get a specific result on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'Result not found.'
- **Parameters**: sourcedId (path), fields

**PUT** - `putResult`
- **Summary**: Update or Create a Result
- **Description**: To update an existing result or create a new one if it doesn't exist. The sourcedId for the record is supplied by the requesting system.
- **Parameters**: sourcedId (path), Request body with result object

**DELETE** - `deleteResult`
- **Summary**: Delete a Result
- **Description**: Perform a soft delete on a specific Result on the service provider. This operation changes the status of the Result to 'tobedeleted'.
- **Parameters**: sourcedId (path)
