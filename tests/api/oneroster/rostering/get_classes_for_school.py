from timeback import Timeback
from timeback.models.request import TimebackGetClassesForSchoolRequest, TimebackQueryParams


def main():
    client = Timeback()
    school_sourced_id = "test-school-001"  # Replace with actual school sourcedId

    # Basic request without query params
    request = TimebackGetClassesForSchoolRequest(school_sourced_id=school_sourced_id)
    response = client.oneroster.rostering.get_classes_for_school(request)
    
    print(f"Total classes for school: {response.total_count}")
    print(f"Page {response.page_number} of {response.page_count}")
    
    for cls in response.classes:
        print(f"  - {cls.sourcedId}: {cls.title}")

    # Example with pagination and filtering
    query_params = TimebackQueryParams(
        limit=10,
        offset=0,
        filter="status='active'",
        sort="title",
        order_by="asc",
    )
    request_with_params = TimebackGetClassesForSchoolRequest(
        school_sourced_id=school_sourced_id,
        query_params=query_params,
    )
    response_filtered = client.oneroster.rostering.get_classes_for_school(request_with_params)
    print(f"\nFiltered classes: {len(response_filtered.classes)} of {response_filtered.total_count}")


if __name__ == "__main__":
    main()

