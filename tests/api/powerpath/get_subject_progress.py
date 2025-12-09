"""API test for get_subject_progress endpoint.

This script can be used to test the get_subject_progress endpoint
against the live PowerPath API.

Usage:
    python -m tests.api.powerpath.get_subject_progress
"""

from timeback import Timeback
from timeback.models.request import TimebackGetSubjectProgressRequest
from timeback.enums import TimebackSubject


def main():
    client = Timeback()

    # Example: Get subject progress for a student in Reading
    # Replace with actual student sourcedId
    request = TimebackGetSubjectProgressRequest(
        student="<student-sourced-id>",  # Replace with actual student ID
        subject=TimebackSubject.READING,
    )

    response = client.powerpath.get_subject_progress(request)

    print(f"Total courses in subject: {len(response.progress)}")
    print("-" * 60)

    for item in response.progress:
        course = item.course
        print(f"\nCourse: {course.title} ({course.sourcedId})")
        print(f"  Enrolled: {item.inEnrolled}")
        print(f"  Progress: {item.completedLessons}/{item.totalLessons} lessons")
        print(f"  XP: {item.totalXpEarned}/{item.totalAttainableXp}")
        print(f"  Test-out used: {item.hasUsedTestOut}")
        if item.testOutLessonId:
            print(f"  Test-out lesson: {item.testOutLessonId}")


if __name__ == "__main__":
    main()

