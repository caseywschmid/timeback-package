"""API test for get_student_placement_data endpoint.

This script can be used to test the get_student_placement_data endpoint
against the live PowerPath API.

Usage:
    python -m tests.api.powerpath.get_student_placement_data
"""

from timeback import Timeback


def main():
    client = Timeback()

    # Replace with actual student ID
    student_id = "<student-sourced-id>"

    response = client.powerpath.get_student_placement_data(student_id)

    print(f"Student Placement Data for: {student_id}")
    print("=" * 60)

    for subject, data in response.items():
        print(f"\n{subject}:")
        print(f"  Starting Grade: {data.startingGrade}")
        print(f"  Current Grade: {data.currentGrade}")
        print(f"  Subject Grade Range: {data.subjectLowestGrade} - {data.subjectHighestGrade}")
        print(f"  Status: {data.status}")
        print(f"  Next Test ID: {data.nextTestId or 'N/A (completed)'}")

        if data.RIT.GROWTH:
            print(f"  RIT GROWTH: {data.RIT.GROWTH.score} (Grade {data.RIT.GROWTH.grade})")
        if data.RIT.SCREENING:
            print(f"  RIT SCREENING: {data.RIT.SCREENING.score} (Grade {data.RIT.SCREENING.grade})")

        if data.results:
            print(f"  Test Results ({len(data.results)}):")
            for result in data.results:
                score_str = f" - Score: {result.score}%" if result.score else ""
                print(f"    - {result.title}: {result.status.value}{score_str}")


if __name__ == "__main__":
    main()

