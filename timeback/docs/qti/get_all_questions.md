## QTI API — Get All Questions

### GET /assessment-tests/{identifier}/questions

- Method: GET
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Retrieve all assessment items (questions) that are referenced by an assessment test, along with their structural context (test part and section). This endpoint aggregates items from all sections across all test parts.

Path params:

- `identifier` (string, required): Unique identifier of the assessment test

Successful response (HTTP 200):

- Body: `{ "assessmentTest": string, "title": string, "totalQuestions": number, "questions": [...] }`
- Key fields:
  - `assessmentTest` (string): Identifier of the assessment test
  - `title` (string): Title of the assessment test
  - `totalQuestions` (number): Total number of questions
  - `questions` (array): List of questions with reference and item data

Question object fields:

- `reference` (object): Location info for the item
  - `identifier` (string): Unique identifier for the item reference
  - `href` (string): URL reference to the assessment item
  - `testPart` (string): Test part identifier where this item is located
  - `section` (string): Section identifier where this item is located
- `question` (object): The actual assessment item data (same as GET /assessment-items/{identifier})

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

# Get all questions from an assessment test
response = client.qti.get_all_questions("test-001")

print(f"Test: {response.title}")
print(f"Total questions: {response.total_questions}")

# Iterate through questions
for q in response.questions:
    ref = q.reference
    item = q.question
    
    print(f"Question: {item.title}")
    print(f"  Type: {item.type}")
    print(f"  Location: {ref.test_part} / {ref.section}")

# Group questions by test part
from collections import defaultdict
by_part = defaultdict(list)
for q in response.questions:
    by_part[q.reference.test_part].append(q)

for part, questions in by_part.items():
    print(f"Part {part}: {len(questions)} questions")

# Group questions by section
by_section = defaultdict(list)
for q in response.questions:
    key = f"{q.reference.test_part}/{q.reference.section}"
    by_section[key].append(q)

for section, questions in by_section.items():
    print(f"Section {section}: {len(questions)} questions")
```

Notes:

- This endpoint provides a flat list of all questions with their structural context
- Use this to understand the full content of an assessment test
- The `question` field contains the complete assessment item data
- Use `reference.testPart` and `reference.section` to understand the test structure
- Questions are returned in their structural order within the test


