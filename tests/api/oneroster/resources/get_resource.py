from timeback import Timeback
from timeback.models.request import TimebackGetResourceRequest


def main():
    client = Timeback()
    request = TimebackGetResourceRequest(sourced_id="<resource-id>")
    response = client.oneroster.resources.get_resource(request)

    print(f"Resource: {response.resource.sourcedId}")
    print(f"  Title: {response.resource.title}")


if __name__ == "__main__":
    main()

