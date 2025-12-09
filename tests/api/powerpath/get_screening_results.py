"""API test for get_screening_results endpoint.

This script can be used to test the get_screening_results endpoint
against the live PowerPath API.

Usage:
    python -m tests.api.powerpath.get_screening_results
"""

from timeback import Timeback


def main():
    client = Timeback()

    # Replace with actual user sourcedId
    user_id = "<user-sourced-id>"

    response = client.powerpath.get_screening_results(user_id)

    print(f"Screening results for user: {user_id}")
    print("-" * 60)

    for subject, result in response.root.items():
        print(f"\n{subject}:")
        if result:
            print(f"  Grade: {result.grade}")
            print(f"  RIT Score: {result.ritScore}")
            print(f"  Test Name: {result.testName}")
            print(f"  Completed At: {result.completedAt}")
        else:
            print("  No screening test completed")


if __name__ == "__main__":
    main()

