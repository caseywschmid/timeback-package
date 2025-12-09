# Organizations Management

## Endpoints

### `/ims/oneroster/rostering/v1p2/orgs/`

**GET** - `getAllOrgs`
- **Summary**: Get all Organizations
- **Description**: To get all Organizations on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

**POST** - `createOrg`
- **Summary**: Create an Organization
- **Description**: To create a new Organization. The responding system must return the set of sourcedIds that have been allocated to the newly created org record.
- **Parameters**: Request body with org object

### `/ims/oneroster/rostering/v1p2/orgs/{sourcedId}`

**GET** - `getOrg`
- **Summary**: Get a specific Organization
- **Description**: Get a specific Organization on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'Organization not found.'
- **Parameters**: sourcedId (path), fields

**PUT** - `updateOrg`
- **Summary**: Update an Organization
- **Description**: To update an existing Organization. The sourcedId for the record to be updated is supplied by the requesting system.
- **Parameters**: sourcedId (path), Request body with org object

**DELETE** - `deleteOrg`
- **Summary**: Delete an Organization
- **Description**: Perform a soft delete on a specific Organization on the service provider. This operation changes the status of the Organization to 'tobedeleted'.
- **Parameters**: sourcedId (path)
