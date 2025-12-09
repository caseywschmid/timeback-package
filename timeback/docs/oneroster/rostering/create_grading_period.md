# Create Grading Period

Create a new grading period in the OneRoster API.

## Endpoint

`POST /ims/oneroster/rostering/v1p2/gradingPeriods`

## Usage

```python
from timeback import Timeback
from timeback.models.request import TimebackCreateGradingPeriodRequest
from timeback.models.timeback_academic_session import TimebackAcademicSession
from timeback.enums import TimebackAcademicSessionType
from timeback.models.timeback_org_ref import TimebackOrgRef

client = Timeback()

session = TimebackAcademicSession(
    title="Q1 2024",
    type=TimebackAcademicSessionType.GRADING_PERIOD,
    startDate="2024-08-01",
    endDate="2024-10-15",
    schoolYear=2024,
    org=TimebackOrgRef(sourcedId="school-001"),
)

request = TimebackCreateGradingPeriodRequest(academic_session=session)
response = client.oneroster.rostering.create_grading_period(request)

print(f"Created: {response.sourcedIdPairs.allocatedSourcedId}")
```

## Request

`TimebackCreateGradingPeriodRequest` containing:

- `academic_session`: A `TimebackAcademicSession` with `type` set to `gradingPeriod`

## Response

Returns `TimebackCreateGradingPeriodResponse` containing:

- `sourcedIdPairs`: Mapping from supplied to allocated sourcedId

