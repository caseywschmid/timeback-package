## QTI API — Get Assessment Item

### GET /assessment-items/{identifier}

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Retrieve a specific assessment item including its question content, answer choices, interaction types, response processing rules, and scoring logic.

Path params:

- `identifier` (string, required): Unique identifier of the assessment item

Successful response (HTTP 200):

- Body: Assessment item object
- Key fields:
  - `identifier` (string): Unique identifier
  - `title` (string): Human-readable title
  - `type` (string): Interaction type (choice, text-entry, extended-text, etc.)
  - `qtiVersion` (string): QTI version (default: "3.0")
  - `timeDependent` (boolean): Whether timing affects scoring
  - `adaptive` (boolean): Whether item adapts to responses
  - `responseDeclarations` (array): Response variable definitions
  - `outcomeDeclarations` (array): Outcome variable definitions
  - `responseProcessing` (object): Scoring/feedback logic
  - `metadata` (object): Custom metadata (subject, grade, difficulty, etc.)
  - `rawXml` (string): Complete QTI XML representation

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 404: Not Found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback

client = Timeback()

# Get a specific assessment item
item = client.qti.get_assessment_item("item-001")

print(f"Identifier: {item.identifier}")
print(f"Title: {item.title}")
print(f"Type: {item.type}")
print(f"QTI Version: {item.qtiVersion}")

# Access response declarations
if item.responseDeclarations:
    for rd in item.responseDeclarations:
        print(f"Response: {rd.identifier}, Cardinality: {rd.cardinality}")

# Access metadata
if item.metadata:
    print(f"Subject: {item.metadata.get('subject')}")
    print(f"Difficulty: {item.metadata.get('difficulty')}")

# Access raw XML for production use
print(item.rawXml)
```

Notes:

- The `rawXml` field contains the complete QTI XML and is recommended for production use
- Assessment items are the core content units that can be referenced by test sections
- Supports both JSON and XML response formats based on the Accept header


