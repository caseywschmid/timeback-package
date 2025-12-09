from timeback import Timeback
from timeback.models.request import TimebackCreateResourceRequest, TimebackCreateResourceBody
from timeback.enums import TimebackImportance


def main():
    client = Timeback()

    body = TimebackCreateResourceBody(
        title="Test Resource",
        vendorResourceId="vendor-test-123",
        importance=TimebackImportance.PRIMARY,
    )
    request = TimebackCreateResourceRequest(resource=body)
    response = client.oneroster.resources.create_resource(request)

    print(f"Created: {response.sourcedIdPairs.allocatedSourcedId}")


if __name__ == "__main__":
    main()

