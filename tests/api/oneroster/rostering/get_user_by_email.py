from argparse import ArgumentParser
from timeback import Timeback


def main():
    parser = ArgumentParser(description="Get user by email")
    parser.add_argument("email", help="Email address to search for")
    args = parser.parse_args()

    client = Timeback()

    # Use filter for exact email match
    users_response = client.oneroster.rostering.get_all_users(
        filter=f"email='{args.email}'"
    )

    if not users_response or not users_response.users:
        print("No user found with that email")
        return

    # Print the first matching user (in case multiple exist)
    user = users_response.users[0]
    print(f"Found user: {user.sourcedId}")
    print(f"  Name: {user.givenName} {user.familyName}")
    print(f"  Email: {user.email}")
    print(f"  User: {user.model_dump_json(indent=2)}")
    if len(users_response.users) > 1:
        print(f"  Note: {len(users_response.users)} users found with this email")


if __name__ == "__main__":
    main()
