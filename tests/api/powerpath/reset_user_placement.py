"""API test for reset_user_placement endpoint.

This script can be used to test the reset_user_placement endpoint
against the live PowerPath API.

**WARNING**: This operation cannot be undone. Use with caution.

Usage:
    python -m tests.api.powerpath.reset_user_placement
"""

from timeback import Timeback
from timeback.models.request import TimebackResetUserPlacementRequest
from timeback.enums import TimebackSubject


def main():
    client = Timeback()

    # Example: Reset placement for a student and subject
    # Replace with actual student ID
    request = TimebackResetUserPlacementRequest(
        student="<student-sourced-id>",  # Replace with actual student ID
        subject=TimebackSubject.MATH,  # Or any other subject
    )

    print("WARNING: This operation cannot be undone!")
    print("-" * 60)
    print(f"Student: {request.student}")
    print(f"Subject: {request.subject.value}")
    print("-" * 60)

    # Uncomment to execute (be careful!)
    # response = client.powerpath.reset_user_placement(request)
    # print(f"Success: {response.success}")
    # print(f"Placement Results Deleted: {response.placementResultsDeleted}")
    # print(f"Onboarding Reset: {response.onboardingReset}")

    print("\nTo execute, uncomment the client call above.")


if __name__ == "__main__":
    main()

