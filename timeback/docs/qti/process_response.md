## QTI API — Process Response

### POST /assessment-items/{identifier}/process-response

- Method: POST
- Auth: OAuth2 Client Credentials (Bearer token)
- Description: Process a candidate's response to an assessment item. Validates the response against the item's response processing rules and returns the score and feedback.

Path params:

- `identifier` (string, required): Unique identifier of the assessment item

Request body:

- `identifier` (string, required): Assessment item identifier (should match path param)
- `response` (string | array, required): The candidate's response
  - String for single-value responses (choice, text-entry)
  - Array of strings for multiple-value responses (multiple choice, ordering)

Successful response (HTTP 200):

- Body: `{ "score": number, "feedback": { "identifier": string, "value": string } }`
- Key fields:
  - `score` (number): Numerical score between 0.0 and 1.0
    - 1.0 for correct answers
    - 0.0 for incorrect answers
    - Decimal value (0.0-1.0) for AI-graded extended text responses
  - `feedback.identifier` (string): Machine-readable feedback classification
    - Typically "correct" or "incorrect" for standard questions
    - Custom identifiers for complex feedback scenarios
  - `feedback.value` (string): Human-readable feedback message

Error responses:

- 400/422: Request/validation → raises `RequestError`
- 401: Unauthorized → raises `AuthError`
- 404: Not Found → raises `NotFoundError`
- 429: Too Many Requests → raises `RateLimitError`
- 5xx: Server errors → raises `ServerError`

Python usage:

```python
from timeback import Timeback
from timeback.models.request import TimebackProcessResponseRequest

client = Timeback()

# Single choice response
request = TimebackProcessResponseRequest(
    identifier="math-addition-001",
    response="B"  # The candidate selected option B
)
result = client.qti.process_response("math-addition-001", request)

print(f"Score: {result.score}")  # 1.0 for correct, 0.0 for incorrect
print(f"Feedback: {result.feedback.value}")
print(f"Feedback ID: {result.feedback.identifier}")

# Multiple choice response (when item allows multiple selections)
request_multi = TimebackProcessResponseRequest(
    identifier="multi-select-001",
    response=["A", "C"]  # Candidate selected options A and C
)
result_multi = client.qti.process_response("multi-select-001", request_multi)

# Text entry response
request_text = TimebackProcessResponseRequest(
    identifier="text-entry-001",
    response="Paris"  # Free-form text answer
)
result_text = client.qti.process_response("text-entry-001", request_text)

# Extended text (AI-graded) response
request_essay = TimebackProcessResponseRequest(
    identifier="essay-001",
    response="The French Revolution began in 1789 and fundamentally transformed..."
)
result_essay = client.qti.process_response("essay-001", request_essay)
print(f"AI Score: {result_essay.score}")  # Decimal between 0.0 and 1.0
print(f"AI Feedback: {result_essay.feedback.value}")  # Detailed rationale
```

Notes:

- The response format must match the item's expected response type
- For choice interactions, use the choice identifier (e.g., "A", "B", "C")
- For text-entry, the response is matched against the correct response declaration
- AI-graded extended text responses return partial credit scores and detailed feedback
- The feedback identifier can be used to look up modal feedback content in the item


