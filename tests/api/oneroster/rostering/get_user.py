from timeback import Timeback


def main():
    client = Timeback()
    sourced_id = "31129aea-12b2-4e9e-a6e5-f5c8b712d674"

    user = client.oneroster.rostering.get_user(sourced_id)
    if not user:
        print("No user found")
        return

    print(user.sourcedId, user.givenName, user.familyName)


if __name__ == "__main__":
    main()
