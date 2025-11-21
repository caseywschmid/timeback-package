# Course Component Resources Management

This section covers the OneRoster API endpoints for managing course component resources.

## Endpoints

### `/ims/oneroster/rostering/v1p2/courses/component-resources`

**GET** - `getAllComponentResources`
- **Summary**: Get all Component Resources
- **Description**: To get all Component Resources on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

**POST** - `createComponentResource`
- **Summary**: Create Component Resource
- **Description**: To create a new Component Resource. The responding system must return the set of sourcedIds that have been allocated to the newly created componentResource record.
- **Parameters**: componentResource (request body)

### `/ims/oneroster/rostering/v1p2/courses/component-resources/{sourcedId}`

**GET** - `getComponentResource`
- **Summary**: Get a specific Component Resource
- **Description**: Get a specific Component Resource on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'Component Resource not found.'
- **Parameters**: sourcedId (path), fields

**PUT** - `putComponentResource`
- **Summary**: Update a Component Resource
- **Description**: To update an existing Component Resource. The sourcedId for the record to be updated is supplied by the requesting system.
- **Parameters**: sourcedId (path), componentResource (request body)

**DELETE** - `deleteComponentResource`
- **Summary**: Delete a Component Resource
- **Description**: Perform a soft delete on a specific Component Resource on the service provider. This operation changes the status of the Component Resource to 'tobedeleted'.
- **Parameters**: sourcedId (path)
