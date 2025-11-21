# Users Management

## Endpoints

### `/ims/oneroster/rostering/v1p2/users/`

**GET** - `getAllUsers`
- **Summary**: Get all Users
- **Description**: To get all Users on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

**POST** - `createUser`
- **Summary**: Create a new User
- **Description**: To create a new User on the service provider. The responding system must return the set of sourcedIds that have been allocated to the newly created user record.
- **Parameters**: Request body with user object

### `/ims/oneroster/rostering/v1p2/users/{sourcedId}`

**GET** - `getUser`
- **Summary**: Get a specific User
- **Description**: To get a specific User on the service provider.
- **Parameters**: sourcedId (path), fields

**PUT** - `updateUser`
- **Summary**: Update an existing User
- **Description**: To update an existing User on the service provider. The sourcedId for the record to be updated is supplied by the requesting system.
- **Parameters**: sourcedId (path), Request body with user object

**DELETE** - `deleteUser`
- **Summary**: Delete a User
- **Description**: Perform a soft delete on a specific User on the service provider. This operation changes the status of the User to 'tobedeleted'.
- **Parameters**: sourcedId (path)

### `/ims/oneroster/rostering/v1p2/users/{sourcedId}/demographics`

**GET** - `getUserWithDemographics`
- **Summary**: Get a specific User with demographics
- **Description**: To get a specific User with demographics on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'User not found.'
- **Parameters**: sourcedId (path), fields

### `/ims/oneroster/rostering/v1p2/users/{userId}/agentFor`

**GET** - `getAgentFor`
- **Summary**: Get users this user is an agent for
- **Description**: Get users this user is an agent for (eg. parents getting the children list)
- **Parameters**: userId (path)

### `/ims/oneroster/rostering/v1p2/users/{userId}/agents`

**GET** - `getAgents`
- **Summary**: Get agents for a user
- **Description**: Get agents for a user
- **Parameters**: userId (path)

**POST** - `addAgent`
- **Summary**: Add an agent for a user
- **Description**: Add an agent for a user
- **Parameters**: userId (path), Request body with agentSourcedId

### `/ims/oneroster/rostering/v1p2/users/{userId}/agents/{agentSourcedId}`

**DELETE** - `deleteAgent`
- **Summary**: Delete an agent for a user
- **Description**: Delete an agent for a user
- **Parameters**: userId (path), agentSourcedId (path)

### `/ims/oneroster/rostering/v1p2/users/{userId}/credentials`

**POST** - `registerStudentCredentials`
- **Summary**: Register student credentials for third-party applications
- **Description**: Register student credentials for third-party applications
- **Parameters**: userId (path), Request body with applicationName and credentials

### `/ims/oneroster/rostering/v1p2/users/{userId}/credentials/{credentialId}/decrypt`

**POST** - `decryptCredential`
- **Summary**: Decrypt a user credential
- **Description**: Decrypt and return the password for a specific user credential.
- **Parameters**: userId (path), credentialId (path)

### `/ims/oneroster/rostering/v1p2/users/{userSourcedId}/classes`

**GET** - `getClassesForUser`
- **Summary**: Get Classes for a User
- **Description**: To get the set of Classes a User is enrolled in.
- **Parameters**: userSourcedId (path), fields, limit, offset, sort, orderBy, filter, search
