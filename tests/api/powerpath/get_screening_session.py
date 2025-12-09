"""API test for get_screening_session endpoint.

This script can be used to test the get_screening_session endpoint
against the live PowerPath API.

Usage:
    python -m tests.api.powerpath.get_screening_session
"""

from timeback import Timeback


def main():
    client = Timeback()

    # Replace with actual user sourcedId
    user_id = "<user-sourced-id>"

    response = client.powerpath.get_screening_session(user_id)

    print(f"Screening session for user: {user_id}")
    print("-" * 60)
    print(f"NWEA Student ID: {response.nweaStudentId}")
    print(f"Name: {response.name}")
    print(f"Session Status: {response.status}")
    print(f"Test Session ID: {response.testSessionId}")
    print(f"PIN: {response.pin}")
    print(f"Password: {response.password}")
    print(f"Proctor ID: {response.proctorId}")
    print(f"Term ID: {response.termId}")
    print(f"Created On: {response.createdOn}")
    print()
    print("Assignment:")
    print(f"  Assigned Test Key: {response.assignment.assignedTestKey}")
    print(f"  Status: {response.assignment.status}")
    print(f"  NWEA Status: {response.assignment.nweaStatus}")


if __name__ == "__main__":
    main()

