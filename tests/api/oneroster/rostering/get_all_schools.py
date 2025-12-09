from timeback import Timeback
from timeback.models.request import TimebackGetAllSchoolsRequest, TimebackQueryParams


def main():
    client = Timeback()

    # Basic request without query params
    request = TimebackGetAllSchoolsRequest()
    response = client.oneroster.rostering.get_all_schools(request)
    if not response or not response.orgs:
        print("No schools found")
        return

    print(f"Total schools: {response.total_count}")
    if response.orgs:
        print(f"First school: {response.orgs[0].sourcedId}, {response.orgs[0].name}")

    # Example with query params
    query_params = TimebackQueryParams(limit=10, offset=0)
    request_with_params = TimebackGetAllSchoolsRequest(query_params=query_params)
    response_paginated = client.oneroster.rostering.get_all_schools(request_with_params)
    print(f"Paginated response: {len(response_paginated.orgs)} schools on page {response_paginated.page_number}")


if __name__ == "__main__":
    main()

