from timeback import Timeback


def main():
    client = Timeback()
    user_id = "3bc7037e-c871-449f-be2d-7fcdcf377512"

    result = client.oneroster.rostering.get_agent_for(user_id)
    if not result or not result.users:
        print("No users found")
        return

    print(f"Found {len(result.users)} users")
    for user in result.users:
        print(f"  {user.sourcedId}: {user.givenName} {user.familyName}")


if __name__ == "__main__":
    main()

