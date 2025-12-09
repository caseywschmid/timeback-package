"""API test for create_lesson_plan endpoint.

This script can be used to test the create_lesson_plan endpoint
against the live PowerPath API.

Usage:
    python -m tests.api.powerpath.create_lesson_plan
"""

from timeback import Timeback
from timeback.models.request import TimebackCreateLessonPlanRequest


def main():
    client = Timeback()

    # Replace with actual IDs
    request = TimebackCreateLessonPlanRequest(
        course_id="<course-sourced-id>",
        user_id="<student-sourced-id>",
        # class_id="<class-sourced-id>",  # Optional
    )

    print(f"Creating lesson plan...")
    print(f"Course: {request.course_id}")
    print(f"Student: {request.user_id}")
    print("-" * 60)

    response = client.powerpath.create_lesson_plan(request)

    print(f"Lesson Plan ID: {response.lessonPlanId}")


if __name__ == "__main__":
    main()

