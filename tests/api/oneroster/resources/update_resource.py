from timeback import Timeback
from timeback.models.request import TimebackUpdateResourceRequest, TimebackUpdateResourceBody
from timeback.enums import TimebackImportance


def main():
    client = Timeback()

    body = TimebackUpdateResourceBody(
        title="Updated Resource",
        vendorResourceId="vendor-test-123",
        importance=TimebackImportance.PRIMARY,
    )
    request = TimebackUpdateResourceRequest(sourced_id="<resource-id>", resource=body)
    response = client.oneroster.resources.update_resource(request)

    print(f"Updated: {response.resource.title}")


if __name__ == "__main__":
    main()

