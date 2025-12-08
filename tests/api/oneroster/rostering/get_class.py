from timeback import Timeback
from timeback.models.request import TimebackGetClassRequest, TimebackQueryParams


def main():
    client = Timeback()
    sourced_id = "test-class-001"  # Replace with actual class sourcedId

    # Basic request without query params
    request = TimebackGetClassRequest(sourced_id=sourced_id)
    response = client.oneroster.rostering.get_class(request)
    if not response or not response.class_:
        print("No class found")
        return

    print(f"Class: {response.class_.sourcedId}, {response.class_.title}")
    print(f"Course: {response.class_.course.sourcedId}")
    print(f"Organization: {response.class_.org.sourcedId}")
    print(f"Terms: {[t.sourcedId for t in response.class_.terms]}")

    # Example with fields query param
    query_params = TimebackQueryParams(fields=["sourcedId", "title", "classCode"])
    request_with_fields = TimebackGetClassRequest(sourced_id=sourced_id, query_params=query_params)
    response_min = client.oneroster.rostering.get_class(request_with_fields)
    print(f"Minimal class: {response_min.class_.sourcedId}, {response_min.class_.title}")


if __name__ == "__main__":
    main()

