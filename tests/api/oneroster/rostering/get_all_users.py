from timeback import Timeback


def main():
    client = Timeback()

    users = client.oneroster.rostering.get_all_users()
    if not users:
        print("No users found")
        return


if __name__ == "__main__":
    main()
