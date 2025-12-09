# Grading Periods Management

## Endpoints

### `/ims/oneroster/rostering/v1p2/gradingPeriods/`

**GET** - `getAllGradingPeriods`
- **Summary**: Get all Grading Periods
- **Description**: To get all Grading Periods on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

**POST** - `createGradingPeriod`
- **Summary**: Create a new Grading Period
- **Description**: To create a new Grading Period. The responding system must return the set of sourcedIds that have been allocated to the newly created gradingPeriod record.
- **Parameters**: Request body with academicSession object

### `/ims/oneroster/rostering/v1p2/terms/{termSourcedId}/gradingPeriods`

**GET** - `getGradingPeriodsForTerm`
- **Summary**: Get Grading Periods for a Term
- **Description**: To get the set of Grading Periods related to a specific Term. If the specified Term cannot be identified within the service provider, the api will return a 404 error code and message 'Term not found.'
- **Parameters**: termSourcedId (path), fields, limit, offset, sort, orderBy, filter, search

**POST** - `createGradingPeriodForTerm`
- **Summary**: Create a new Grading Period for a Term
- **Description**: To create a new Grading Period for a Term. A Grading Period is a type of Academic Session. The responding system must return the set of sourcedIds that have been allocated to the newly created academicSession record.
- **Parameters**: termSourcedId (path), Request body with academicSession object

### `/ims/oneroster/rostering/v1p2/gradingPeriods/{sourcedId}`

**GET** - `getGradingPeriod`
- **Summary**: Get a specific Grading Period
- **Description**: Get a specific Grading Period on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'Grading period not found.'
- **Parameters**: sourcedId (path), fields

**PUT** - `updateGradingPeriod`
- **Summary**: Update a Grading Period
- **Description**: To update an existing Grading Period. The sourcedId for the record to be updated is supplied by the requesting system.
- **Parameters**: sourcedId (path), Request body with academicSession object

**DELETE** - `deleteGradingPeriod`
- **Summary**: Delete a Grading Period
- **Description**: Perform a soft delete on a specific Grading Period on the service provider. This operation changes the status of the Grading Period to 'tobedeleted'.
- **Parameters**: sourcedId (path)
