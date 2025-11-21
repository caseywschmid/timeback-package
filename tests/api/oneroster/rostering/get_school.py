from timeback import Timeback
from timeback.models.request import TimebackGetSchoolRequest, TimebackQueryParams


def main():
    client = Timeback()
    sourced_id = "test-school-001"  # Replace with actual school sourcedId

    # Basic request without query params
    request = TimebackGetSchoolRequest(sourced_id=sourced_id)
    response = client.oneroster.rostering.get_school(request)
    if not response or not response.org:
        print("No school found")
        return

    print(f"School: {response.org.sourcedId}, {response.org.name}, {response.org.type}")

    # Example with fields query param
    query_params = TimebackQueryParams(fields=["sourcedId", "name", "type"])
    request_with_fields = TimebackGetSchoolRequest(sourced_id=sourced_id, query_params=query_params)
    response_min = client.oneroster.rostering.get_school(request_with_fields)
    print(f"Minimal school: {response_min.org.sourcedId}, {response_min.org.name}")


if __name__ == "__main__":
    main()

