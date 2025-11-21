# Demographics Management

This section covers the OneRoster API endpoints for managing demographic information.

## Endpoints

### `/ims/oneroster/rostering/v1p2/demographics/`

**GET** - `getAllDemographics`
- **Summary**: Get all Demographic records
- **Description**: To get all Demographic records on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

**POST** - `postDemographics`
- **Summary**: Create a new Demographic record
- **Description**: To create a new Demographic record. The responding system must return the set of sourcedIds that have been allocated to the newly created demographic record.
- **Parameters**: demographics (request body)

### `/ims/oneroster/rostering/v1p2/demographics/{sourcedId}`

**GET** - `getDemographics`
- **Summary**: Get a specific Demographic record
- **Description**: Get a specific Demographic record on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'Demographics record not found.'
- **Parameters**: sourcedId (path), fields

**PUT** - `putDemographics`
- **Summary**: Update a Demographic record
- **Description**: To update an existing Demographic record. The sourcedId for the record to be updated is supplied by the requesting system.
- **Parameters**: sourcedId (path), demographics (request body)

**DELETE** - `deleteDemographics`
- **Summary**: Delete a Demographic record
- **Description**: Perform a soft delete on a specific Demographic record on the service provider. This operation changes the status of the Demographic record to 'tobedeleted'.
- **Parameters**: sourcedId (path)
