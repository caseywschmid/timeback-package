# Get All Grading Periods

Fetch a paginated list of grading periods from the OneRoster API.

## Endpoint

`GET /ims/oneroster/rostering/v1p2/gradingPeriods`

## Usage

```python
from timeback import Timeback
from timeback.models.request import TimebackGetAllGradingPeriodsRequest, TimebackQueryParams

client = Timeback()

# Basic usage
request = TimebackGetAllGradingPeriodsRequest()
response = client.oneroster.rostering.get_all_grading_periods(request)

# With pagination and filtering
request = TimebackGetAllGradingPeriodsRequest(
    query_params=TimebackQueryParams(
        limit=50,
        offset=0,
        filter="status='active'"
    )
)
response = client.oneroster.rostering.get_all_grading_periods(request)

# Access results
for grading_period in response.academicSessions:
    print(f"{grading_period.title}: {grading_period.startDate} - {grading_period.endDate}")
```

## Response

Returns `TimebackGetAllTermsResponse` containing:

- `academicSessions`: List of `TimebackAcademicSession` objects (grading periods are a type of academic session)
- `totalCount`: Total number of grading periods
- `pageCount`: Total number of pages
- `pageNumber`: Current page number
- `offset`: Current offset
- `limit`: Current limit

## Notes

Grading periods are a type of academic session with `type` = "gradingPeriod". The response uses the same model as terms since both are academic sessions.

