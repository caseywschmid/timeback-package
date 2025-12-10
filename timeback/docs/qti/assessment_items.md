# QTI API — Assessment Item Endpoints

Assessment items are the core content units in QTI that contain questions, answer choices, and scoring logic.

## Endpoints

### GET /assessment-items — Search Assessment Items

Search and filter assessment items with advanced filtering capabilities.

Query params:
- `query` (string, optional): Fuzzy search on title and identifier
- `page` (integer, default 1): Page number (1-indexed)
- `limit` (integer, default 10): Items per page
- `sort` (enum: `title`, `identifier`, `type`, `createdAt`, `updatedAt`)
- `order` (enum: `asc`, `desc`, default `desc`)
- `filter` (string): Advanced filter expression (e.g., `type='choice'`)

Response (HTTP 200):
- `items`: Array of assessment items
- `total`, `page`, `pages`, `limit`, `sort`, `order`

```python
from timeback import Timeback
from timeback.models.request import TimebackSearchAssessmentItemsRequest

client = Timeback()

# Basic search
response = client.qti.search_assessment_items()

# Search with filter
request = TimebackSearchAssessmentItemsRequest(
    query="math",
    filter="type='choice'"
)
response = client.qti.search_assessment_items(request)
```

---

### GET /assessment-items/{identifier} — Get Assessment Item

Retrieve a specific assessment item with complete content.

Path params:
- `identifier` (string, required): Assessment item identifier

Response (HTTP 200): Complete assessment item object

```python
item = client.qti.get_assessment_item("item-001")
print(f"Title: {item.title}, Type: {item.type}")
```

---

### POST /assessment-items — Create Assessment Item

Create a new QTI 3.0 assessment item, preferably from XML.

Request body:
- `format` (string, required): `"xml"` (recommended) or `"json"`
- `xml` (string): QTI 3.0 XML content (when format="xml")
- `metadata` (object, optional): Custom metadata

Response (HTTP 201): Created assessment item

```python
from timeback.models.request import TimebackCreateAssessmentItemRequest

xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<qti-assessment-item
  xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
  identifier="my-item-1"
  title="Math Question"
  adaptive="false"
  time-dependent="false">
  <!-- QTI content -->
</qti-assessment-item>'''

request = TimebackCreateAssessmentItemRequest(
    format="xml",
    xml=xml_content,
    metadata={"subject": "Math", "grade": "5", "difficulty": "medium"}
)
item = client.qti.create_assessment_item(request)
```

---

### PUT /assessment-items/{identifier} — Update Assessment Item

Update an existing assessment item's content and configuration.

Path params:
- `identifier` (string, required): Assessment item identifier

Request body:
- `format` (string): `"xml"` (recommended) or `"json"`
- `xml` (string): Updated QTI 3.0 XML content
- `metadata` (object, optional): Updated metadata

Response (HTTP 200): Updated assessment item

```python
from timeback.models.request import TimebackUpdateAssessmentItemRequest

request = TimebackUpdateAssessmentItemRequest(
    format="xml",
    xml=updated_xml_content,
    metadata={"difficulty": "hard"}
)
item = client.qti.update_assessment_item("item-001", request)
```

---

### DELETE /assessment-items/{identifier} — Delete Assessment Item

Permanently delete an assessment item. Cannot be undone.

Path params:
- `identifier` (string, required): Assessment item identifier

Response (HTTP 204): No content

```python
client.qti.delete_assessment_item("item-001")
```

**Warning**: Assessment tests referencing this item may be affected.

---

## Assessment Item Types

- `choice`: Multiple choice
- `text-entry`: Short text input
- `extended-text`: Long-form text (essay)
- `inline-choice`: Dropdown selection
- `match`: Matching pairs
- `order`: Ordering/sequencing
- `associate`: Association mapping
- `select-point`: Point selection on image
- `graphic-order`: Ordering on graphic
- `graphic-associate`: Association on graphic
- `graphic-gap-match`: Gap matching on graphic
- `hotspot`: Clickable regions
- `hottext`: Clickable text segments
- `slider`: Numeric slider
- `drawing`: Drawing canvas
- `media`: Media-based interaction
- `upload`: File upload

## Metadata Fields

Common metadata fields:
- `subject`: Subject area (Math, Science, etc.)
- `grade`: Grade level (-1 to 13, where -1 is Pre-K)
- `difficulty`: `easy`, `medium`, `hard`
- `learningObjectiveSet`: Array of learning objectives

## Error Responses

- 400/422: Request/validation error → `RequestError`
- 401: Unauthorized → `AuthError`
- 404: Not found → `NotFoundError`
- 429: Rate limit → `RateLimitError`
- 5xx: Server error → `ServerError`

