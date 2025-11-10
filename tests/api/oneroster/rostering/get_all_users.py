from timeback import Timeback
from timeback.models.request import TimebackGetAllUsersRequest, TimebackQueryParams


def main():
    client = Timeback()

    # Basic request without query params
    request = TimebackGetAllUsersRequest()
    response = client.oneroster.rostering.get_all_users(request)
    if not response or not response.users:
        print("No users found")
        return

    print(f"Total users: {response.totalCount}")
    if response.users:
        print(f"First user: {response.users[0].sourcedId}, {response.users[0].givenName}, {response.users[0].familyName}")

    # Example with query params
    query_params = TimebackQueryParams(limit=10, offset=0)
    request_with_params = TimebackGetAllUsersRequest(query_params=query_params)
    response_paginated = client.oneroster.rostering.get_all_users(request_with_params)
    print(f"Paginated response: {len(response_paginated.users)} users on page {response_paginated.pageNumber}")


if __name__ == "__main__":
    main()
