from timeback import Timeback


def main():
    client = Timeback()
    sourced_id = "test-category-to-delete"  # Replace with actual category sourcedId

    # Delete the category (soft delete - sets status to 'tobedeleted')
    result = client.oneroster.gradebook.delete_category(sourced_id)
    
    if result is None:
        print(f"Category {sourced_id} deleted successfully (204 No Content)")
    else:
        print(f"Category deleted with response: {result}")


if __name__ == "__main__":
    main()

