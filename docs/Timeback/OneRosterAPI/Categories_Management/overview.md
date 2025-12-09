# Categories Management

## Endpoints

### `/ims/oneroster/gradebook/v1p2/categories/`

**GET** - `getAllCategories`
- **Summary**: Get all Categories
- **Description**: Get all of the Line Item Categories on the service provider.
- **Parameters**: fields, limit, offset, sort, orderBy, filter, search

**POST** - `createCategory`
- **Summary**: Create a Category
- **Description**: To create a new Category. The responding system must return the set of sourcedIds that have been allocated to the newly created category record. A 'title' MUST be provided when creating a category.
- **Parameters**: Request body with category object

### `/ims/oneroster/gradebook/v1p2/categories/{sourcedId}`

**GET** - `getCategory`
- **Summary**: Get a Category
- **Description**: Get a specific category on the service provider. If the corresponding record cannot be located, the api will return a 404 error code and message 'Category not found.'
- **Parameters**: sourcedId (path), fields

**PUT** - `putCategory`
- **Summary**: Update or Create a Category
- **Description**: To update an existing Category or create a new one if it doesn't exist. The sourcedId for the record is supplied by the requesting system.
- **Parameters**: sourcedId (path), Request body with category object

**DELETE** - `deleteCategory`
- **Summary**: Delete a Category
- **Description**: Perform a soft delete on a specific Category on the service provider. This operation changes the status of the Category to 'tobedeleted'.
- **Parameters**: sourcedId (path)
