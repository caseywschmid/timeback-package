"""API test for create_internal_test endpoint.

This script can be used to test the create_internal_test endpoint
against the live PowerPath API.

Usage:
    python -m tests.api.powerpath.create_internal_test
"""

from timeback import Timeback
from timeback.models.request import (
    TimebackCreateInternalQtiTestRequest,
    TimebackCreateInternalAssessmentBankTestRequest,
    TimebackQtiTestConfig,
    TimebackAssessmentBankConfig,
    TimebackAssessmentBankResource,
)


def main():
    client = Timeback()

    # Example 1: Create a QTI test
    print("Creating QTI internal test...")
    qti_request = TimebackCreateInternalQtiTestRequest(
        courseId="<course-sourced-id>",  # Replace with actual course ID
        lessonType="quiz",
        lessonTitle="Chapter 1 Quiz",
        qti=TimebackQtiTestConfig(
            url="https://qti.example.com/test.xml",  # Replace with actual QTI URL
            title="Chapter 1 Assessment",
        ),
    )

    # Uncomment to run:
    # qti_response = client.powerpath.create_internal_test(qti_request)
    # print(f"QTI Test created!")
    # print(f"  Lesson ID: {qti_response.lessonId}")
    # print(f"  Resource ID: {qti_response.resourceId}")

    # Example 2: Create an Assessment Bank test
    print("\nCreating Assessment Bank internal test...")
    bank_request = TimebackCreateInternalAssessmentBankTestRequest(
        courseId="<course-sourced-id>",  # Replace with actual course ID
        lessonType="placement",
        grades=["5", "6"],
        assessmentBank=TimebackAssessmentBankConfig(
            resources=[
                TimebackAssessmentBankResource(
                    url="https://qti.example.com/test1.xml",
                    title="Placement Test Part 1",
                ),
                TimebackAssessmentBankResource(
                    url="https://qti.example.com/test2.xml",
                    title="Placement Test Part 2",
                ),
            ]
        ),
    )

    # Uncomment to run:
    # bank_response = client.powerpath.create_internal_test(bank_request)
    # print(f"Assessment Bank Test created!")
    # print(f"  Lesson ID: {bank_response.lessonId}")
    # print(f"  Resource ID: {bank_response.resourceId}")
    # print(f"  Child Resource IDs: {bank_response.childResourceIds}")

    print("\nTo run these tests, uncomment the client calls above and provide real values.")


if __name__ == "__main__":
    main()

