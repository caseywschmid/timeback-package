# Terms Management

## Endpoints

### `/ims/oneroster/rostering/v1p2/terms/`

**GET** - `getAllTerms`
- **Summary**: Get all Terms
- **Description**: To get all Terms on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search


### `/ims/oneroster/rostering/v1p2/terms/{sourcedId}`

**GET** - `getTerm`
- **Summary**: Get a specific Term
- **Description**: To get a specific Term on the service provider.
- **Parameters**: sourcedId (path), fields


### `/ims/oneroster/rostering/v1p2/terms/{termSourcedId}/classes`

**GET** - `getClassesForTerm`
- **Summary**: Get Classes for a Term
- **Description**: To get the set of Classes related to a specific Term. If the specified term cannot be identified within the service provider, the api will return a 404 error code and message 'Term not found.'
- **Parameters**: termSourcedId (path), fields, limit, offset, sort, orderBy, filter, search


