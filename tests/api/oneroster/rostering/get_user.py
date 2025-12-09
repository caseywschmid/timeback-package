from timeback import Timeback
from timeback.models.request import TimebackGetUserRequest, TimebackQueryParams


def main():
    client = Timeback()
    sourced_id = "20268c57-3828-4f4a-8144-2ef896681010"

    # Basic request without query params
    request = TimebackGetUserRequest(sourced_id=sourced_id)
    response = client.oneroster.rostering.get_user(request)
    if not response or not response.user:
        print("No user found")
        return

    print(response)

    # Example with fields query param
    query_params = TimebackQueryParams(fields=["sourcedId", "givenName", "familyName"])
    request_with_fields = TimebackGetUserRequest(
        sourced_id=sourced_id, query_params=query_params
    )
    response_min = client.oneroster.rostering.get_user(request_with_fields)
    print(
        f"Minimal user: {response_min.user.sourcedId}, {response_min.user.givenName}, {response_min.user.familyName}"
    )


if __name__ == "__main__":
    main()
