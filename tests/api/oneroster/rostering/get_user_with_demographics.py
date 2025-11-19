from timeback import Timeback
from timeback.models.request import TimebackGetUserRequest, TimebackQueryParams


def main():
    client = Timeback()
    sourced_id = "77823ff2-6d52-4cf9-ab4a-111011006736"

    # Basic request without query params
    request = TimebackGetUserRequest(sourced_id=sourced_id)
    response = client.oneroster.rostering.get_user_with_demographics(request)
    if not response or not response.user:
        print("No user found")
        return

    print(response.user.sourcedId, response.user.givenName, response.user.familyName)

    # Example with fields query param
    query_params = TimebackQueryParams(fields=["sourcedId", "givenName", "familyName"])
    request_with_fields = TimebackGetUserRequest(sourced_id=sourced_id, query_params=query_params)
    response_min = client.oneroster.rostering.get_user_with_demographics(request_with_fields)
    print(f"Minimal user: {response_min.user.sourcedId}, {response_min.user.givenName}, {response_min.user.familyName}")


if __name__ == "__main__":
    main()

