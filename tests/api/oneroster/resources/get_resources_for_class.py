from timeback import Timeback
from timeback.models.request import TimebackGetResourcesForClassRequest


def main():
    client = Timeback()
    request = TimebackGetResourcesForClassRequest(class_sourced_id="<class-id>")
    response = client.oneroster.resources.get_resources_for_class(request)

    print(f"Resources for class: {response.totalCount}")
    for res in response.resources[:5]:
        print(f"  - {res.sourcedId}: {res.title}")


if __name__ == "__main__":
    main()

