"""API test for sync_course_lesson_plans endpoint.

**WARNING**: This will sync ALL lesson plans for a course.

Usage:
    python -m tests.api.powerpath.sync_course_lesson_plans
"""

from timeback import Timeback


def main():
    client = Timeback()

    # Replace with actual course ID
    course_id = "<course-sourced-id>"

    print("WARNING: This will sync ALL lesson plans for the course!")
    print("-" * 60)
    print(f"Course ID: {course_id}")
    print("-" * 60)

    # Uncomment to execute
    # response = client.powerpath.sync_course_lesson_plans(course_id)
    # print(f"Lesson plans affected: {len(response.lessonPlansAffected)}")
    # for lp_id in response.lessonPlansAffected:
    #     print(f"  - {lp_id}")

    print("\nTo execute, uncomment the client call above.")


if __name__ == "__main__":
    main()

