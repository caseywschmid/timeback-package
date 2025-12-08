from timeback import Timeback


def main():
    client = Timeback()
    sourced_id = "test-class-to-delete"  # Replace with actual class sourcedId

    # Delete class (soft delete - sets status to 'tobedeleted')
    result = client.oneroster.rostering.delete_class(sourced_id)
    print(f"Delete result: {result}")  # Should be None for 204 No Content
    print(f"Class {sourced_id} deleted successfully (status set to 'tobedeleted')")


if __name__ == "__main__":
    main()

