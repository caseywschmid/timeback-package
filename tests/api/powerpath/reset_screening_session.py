"""API test for reset_screening_session endpoint.

This script can be used to test the reset_screening_session endpoint
against the live PowerPath API.

Usage:
    python -m tests.api.powerpath.reset_screening_session
"""

from timeback import Timeback


def main():
    client = Timeback()

    # Replace with actual user ID
    user_id = "<user-sourced-id>"

    print(f"Resetting screening session for user: {user_id}")
    print("-" * 60)

    # Uncomment to execute
    # client.powerpath.reset_screening_session(user_id)
    # print("Session reset successfully (204 No Content)")

    print("\nTo execute, uncomment the client call above.")


if __name__ == "__main__":
    main()

