from timeback import Timeback
from timeback.models.request import TimebackGetAllClassesRequest, TimebackQueryParams


def main():
    client = Timeback()

    # Basic request without query params
    request = TimebackGetAllClassesRequest()
    response = client.oneroster.rostering.get_all_classes(request)
    if not response or not response.classes:
        print("No classes found")
        return

    print(f"Total classes: {response.total_count}")
    if response.classes:
        first_class = response.classes[0]
        print(f"First class: {first_class.sourcedId}, {first_class.title}")
        print(f"  Class Code: {first_class.classCode}")
        print(f"  Class Type: {first_class.classType}")
        print(f"  Location: {first_class.location}")
        print(f"  Course: {first_class.course.sourcedId}")
        print(f"  School: {first_class.org.sourcedId}")
        if first_class.terms:
            print(f"  Terms: {[term.sourcedId for term in first_class.terms]}")

    # Example with query params
    query_params = TimebackQueryParams(limit=10, offset=0, fields="sourcedId,title,classCode")
    request_with_params = TimebackGetAllClassesRequest(query_params=query_params)
    response_paginated = client.oneroster.rostering.get_all_classes(request_with_params)
    print(f"\nPaginated response: {len(response_paginated.classes)} classes on page {response_paginated.page_number}")


if __name__ == "__main__":
    main()

