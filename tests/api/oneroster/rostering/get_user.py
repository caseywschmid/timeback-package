from timeback import Timeback


def main():
    client = Timeback()
    sourced_id = "3bc7037e-c871-449f-be2d-7fcdcf377512"

    user = client.oneroster.rostering.get_user(sourced_id)
    if not user:
        print("No user found")
        return

    print(user.sourcedId, user.givenName, user.familyName)


if __name__ == "__main__":
    main()
