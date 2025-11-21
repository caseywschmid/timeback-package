from timeback import Timeback
from timeback.models.request import (
    TimebackGetResultsForStudentForClassRequest,
    TimebackQueryParams,
)


def main():
    client = Timeback()
    class_sourced_id = "class-123"
    student_sourced_id = "student-456"

    # Example 1: Get results for a student and class with default parameters
    print(f"Getting results for class: {class_sourced_id} and student: {student_sourced_id}")
    request = TimebackGetResultsForStudentForClassRequest(
        class_sourced_id=class_sourced_id,
        student_sourced_id=student_sourced_id
    )
    resp = client.oneroster.gradebook.get_results_for_student_for_class(request)

    print(f"Total Results: {resp.total_count}")
    print(f"Page {resp.page_number} of {resp.page_count}")
    print(f"Showing {len(resp.results)} results")
    print()

    for result in resp.results:
        print(f"- Result {result.sourcedId}")
        print(f"  Student: {result.student.sourcedId}")
        print(f"  Line Item: {result.lineItem.sourcedId}")
        print(f"  Class: {result.class_.sourcedId if result.class_ else 'N/A'}")
        print(f"  Score Status: {result.scoreStatus}")
        print(f"  Score Date: {result.scoreDate}")
        if result.score is not None:
            print(f"  Score: {result.score}")
        if result.textScore:
            print(f"  Text Score: {result.textScore}")
        if result.comment:
            print(f"  Comment: {result.comment}")
        print()

    # Example 2: Get results with query parameters
    print("\n--- With Query Parameters ---")
    query_params = TimebackQueryParams(limit=10, offset=0, fields="sourcedId,scoreStatus,score")
    request_with_params = TimebackGetResultsForStudentForClassRequest(
        class_sourced_id=class_sourced_id,
        student_sourced_id=student_sourced_id,
        query_params=query_params
    )
    resp_filtered = client.oneroster.gradebook.get_results_for_student_for_class(request_with_params)

    print(f"Filtered Results: {len(resp_filtered.results)} results")


if __name__ == "__main__":
    main()

