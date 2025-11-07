from timeback import Timeback


def main():
    client = Timeback()
    sourced_id = "523cd9f6-a5f9-430b-bab5-6f3561e470fc"
    result = client.oneroster.rostering.delete_user(sourced_id)
    print("Result:", result)


if __name__ == "__main__":
    main()

    # {"sourcedId": "6ef4b990-3087-4a00-a1cc-419b9b37075d"},
    # {"sourcedId": "ce324226-2954-457c-b925-adfd2b253dd0"},
    # {"sourcedId": "7e32d070-b083-4d77-95bf-fc4bdb054fde"},
    # {"sourcedId": "227d6dbc-367f-4883-a7ee-22aa484f52da"},
    # {"sourcedId": "523cd9f6-a5f9-430b-bab5-6f3561e470fc"}
