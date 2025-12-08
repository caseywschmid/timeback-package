from timeback import Timeback
from timeback.models.request import TimebackGetResourcesForUserRequest


def main():
    client = Timeback()
    request = TimebackGetResourcesForUserRequest(user_sourced_id="<user-id>")
    response = client.oneroster.resources.get_resources_for_user(request)

    print(f"Resources for user: {response.totalCount}")
    for res in response.resources[:5]:
        print(f"  - {res.sourcedId}: {res.title}")


if __name__ == "__main__":
    main()

