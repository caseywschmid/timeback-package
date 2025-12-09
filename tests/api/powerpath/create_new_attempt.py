"""API test for create_new_attempt endpoint.

Usage:
    python -m tests.api.powerpath.create_new_attempt
"""

from timeback import Timeback
from timeback.models.request import TimebackCreateNewAttemptRequest


def main():
    client = Timeback()

    # Replace with actual IDs
    request = TimebackCreateNewAttemptRequest(
        student="<student-sourced-id>",
        lesson="<lesson-component-resource-id>",
    )

    print(f"Creating new attempt for student: {request.student}")
    print(f"Lesson: {request.lesson}")
    print("-" * 60)

    response = client.powerpath.create_new_attempt(request)

    print(f"Attempt #: {response.attempt.attempt}")
    print(f"Score: {response.attempt.score}")
    print(f"Status: {response.attempt.scoreStatus}")
    print(f"Started: {response.attempt.startedAt}")


if __name__ == "__main__":
    main()

