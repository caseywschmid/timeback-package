# Resources Management

## Endpoints

### `/ims/oneroster/resources/v1p2/resources/`

**GET** - `getAllResources`
- **Summary**: Get all Resources
- **Description**: To get a collection of resources that exist on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

**POST** - `createResource`
- **Summary**: Create a new Resource
- **Description**: To create a new resource. The responding system must return the set of sourcedIds that have been allocated to the newly created resource record.
- **Parameters**: Request body with resource object

### `/ims/oneroster/resources/v1p2/resources/{sourcedId}`

**GET** - `getResource`
- **Summary**: Get a specific Resource
- **Description**: To get a specific resource by sourcedId. If the corresponding record cannot be located, the api will return a 404 error code and message 'Resource not found.'
- **Parameters**: sourcedId (path), fields

**PUT** - `updateResource`
- **Summary**: Update an existing Resource
- **Description**: To update an existing resource. The sourcedId for the record to be updated is supplied by the requesting system.
- **Parameters**: sourcedId (path), Request body with resource object

**DELETE** - `deleteResource`
- **Summary**: Delete a resource
- **Description**: Perform a soft delete on a specific resource. This operation changes the status of the resource to 'tobedeleted'.
- **Parameters**: sourcedId (path)

### `/ims/oneroster/resources/v1p2/resources/classes/{classSourcedId}/resources`

**GET** - `getResourcesForClass`
- **Summary**: Get resources for a class
- **Description**: To get the collection of resources available to a specific class. If the corresponding record cannot be located, the api will return a 404 error code and message 'Class not found.'
- **Parameters**: classSourcedId (path), fields, limit, offset, sort, orderBy, filter, search

### `/ims/oneroster/resources/v1p2/resources/courses/{courseSourcedId}/resources`

**GET** - `getResourcesForCourse`
- **Summary**: Get resources for a course
- **Description**: To get the collection of resources assigned to a specific course. If the corresponding record cannot be located, the api will return a 404 error code and message 'Course not found.'
- **Parameters**: courseSourcedId (path), fields, limit, offset, sort, orderBy, filter, search

### `/ims/oneroster/resources/v1p2/resources/export/{sourceId}`

**POST** - `exportResourceToCommonCartridge`
- **Summary**: Export Resource to Common Cartridge
- **Description**: Export a resource to Common Cartridge (.imscc) format for import into LMS systems.
- **Parameters**: sourceId (path)

### `/ims/oneroster/resources/v1p2/resources/users/{userSourcedId}/resources`

**GET** - `getResourcesForUser`
- **Summary**: Get resources for a user
- **Description**: To get the collection of resources available to a specific user. If the corresponding record cannot be located, the api will return a 404 error code and message 'User not found.'
- **Parameters**: userSourcedId (path), fields, limit, offset, sort, orderBy, filter, search
