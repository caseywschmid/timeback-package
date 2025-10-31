from timeback import Timeback


def main():
    client = Timeback()
    sourced_id = "replace-with-real-user-sourced-id"
    result = client.oneroster.rostering.delete_user(sourced_id)
    print("Result:", result)


if __name__ == "__main__":
    main()


