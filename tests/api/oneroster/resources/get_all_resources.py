from timeback import Timeback
from timeback.models.request import TimebackGetAllResourcesRequest, TimebackQueryParams


def main():
    client = Timeback()

    request = TimebackGetAllResourcesRequest()
    response = client.oneroster.resources.get_all_resources(request)

    print(f"Total resources: {response.totalCount}")
    for res in response.resources[:5]:
        print(f"  - {res.sourcedId}: {res.title}")


if __name__ == "__main__":
    main()

