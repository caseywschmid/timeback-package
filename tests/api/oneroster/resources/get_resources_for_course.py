from timeback import Timeback
from timeback.models.request import TimebackGetResourcesForCourseRequest


def main():
    client = Timeback()
    request = TimebackGetResourcesForCourseRequest(course_sourced_id="<course-id>")
    response = client.oneroster.resources.get_resources_for_course(request)

    print(f"Resources for course: {response.totalCount}")
    for res in response.resources[:5]:
        print(f"  - {res.sourcedId}: {res.title}")


if __name__ == "__main__":
    main()

