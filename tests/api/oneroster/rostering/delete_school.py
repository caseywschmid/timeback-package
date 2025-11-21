from timeback import Timeback


def main():
    client = Timeback()
    sourced_id = "test-school-001"  # Replace with actual school sourcedId
    result = client.oneroster.rostering.delete_school(sourced_id)
    print("Result:", result)


if __name__ == "__main__":
    main()

