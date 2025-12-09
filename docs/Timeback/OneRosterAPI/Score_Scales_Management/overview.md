# Score Scales Management

## Endpoints

### `/ims/oneroster/gradebook/v1p2/scoreScales/`

**GET** - `getAllScoreScales`
- **Summary**: Get all Score Scales
- **Description**: Get all of the ScoreScales on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

**POST** - `createScoreScale`
- **Summary**: Create a Score Scale
- **Description**: To create a new scoreScale. The responding system must return the set of sourcedIds that have been allocated to the newly created scoreScale records.
- **Parameters**: Request body with scoreScale object

### `/ims/oneroster/gradebook/v1p2/scoreScales/{sourcedId}`

**GET** - `getScoreScale`
- **Summary**: Get a Score Scale
- **Description**: Get a specific scoreScale on the service provider.
- **Parameters**: sourcedId (path), fields

**PUT** - `putScoreScale`
- **Summary**: Update or Create a Score Scale
- **Description**: To update an existing scoreScale or create a new one if it doesn't exist. The sourcedId for the record is supplied by the requesting system.
- **Parameters**: sourcedId (path), Request body with scoreScale object

**DELETE** - `deleteScoreScale`
- **Summary**: Delete a Score Scale
- **Description**: Perform a soft delete on a specific Score Scale on the service provider. This operation changes the status of the Score Scale to 'tobedeleted'.
- **Parameters**: sourcedId (path)

### `/ims/oneroster/gradebook/v1p2/schools/{sourcedId}/scoreScales`

**GET** - `getScoreScalesForSchool`
- **Summary**: Get Score Scales for a School
- **Description**: Get the set of scoreScales on the service provider for a specific school. If the corresponding record cannot be located, the api will return a 404 error code and message 'School not found.'
- **Parameters**: sourcedId (path), fields, limit, offset, sort, orderBy, filter, search
