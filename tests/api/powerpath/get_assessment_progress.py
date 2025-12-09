"""API test for get_assessment_progress endpoint.

Usage:
    python -m tests.api.powerpath.get_assessment_progress
"""

from timeback import Timeback


def main():
    client = Timeback()

    # Replace with actual IDs
    student_id = "<student-sourced-id>"
    lesson_id = "<lesson-component-resource-id>"

    print(f"Getting assessment progress for student: {student_id}")
    print(f"Lesson: {lesson_id}")
    print("-" * 60)

    response = client.powerpath.get_assessment_progress(student_id, lesson_id)

    print(f"Lesson Type: {response.lessonType}")
    print(f"Attempt: {response.attempt}")
    print(f"Score: {response.score}")
    print(f"Accuracy: {response.accuracy}")
    print(f"Questions: {response.correctQuestions}/{response.totalQuestions}")


if __name__ == "__main__":
    main()

