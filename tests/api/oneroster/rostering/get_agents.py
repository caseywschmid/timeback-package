from timeback import Timeback


def main():
    client = Timeback()
    user_id = "3bc7037e-c871-449f-be2d-7fcdcf377512"  # replace with a real user id when testing

    result = client.oneroster.rostering.get_agents(user_id)
    if not result or not result.agents:
        print("No agents found")
        return

    print(f"Found {len(result.agents)} agents")
    for user in result.agents:
        print(f"  {user.sourcedId}: {user.givenName} {user.familyName}")


if __name__ == "__main__":
    main()


