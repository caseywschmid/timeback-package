"""API test for final_student_assessment_response endpoint.

Usage:
    python -m tests.api.powerpath.final_student_assessment_response
"""

from timeback import Timeback
from timeback.models.request import TimebackFinalStudentAssessmentRequest


def main():
    client = Timeback()

    # Replace with actual IDs
    request = TimebackFinalStudentAssessmentRequest(
        student="<student-sourced-id>",
        lesson="<lesson-component-resource-id>",
    )

    print(f"Finalizing assessment for student: {request.student}")
    print(f"Lesson: {request.lesson}")
    print("-" * 60)

    response = client.powerpath.final_student_assessment_response(request)

    print(f"Lesson Type: {response.lessonType}")
    print(f"Finalized: {response.finalized}")
    print(f"Attempt: {response.attempt}")


if __name__ == "__main__":
    main()

