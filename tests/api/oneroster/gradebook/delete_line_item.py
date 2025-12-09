from timeback import Timeback
from timeback.models.request import TimebackDeleteLineItemRequest


def main():
    client = Timeback()
    sourced_id = "line-item-123-456"

    # Create the request
    print(f"Deleting line item: {sourced_id}")
    request = TimebackDeleteLineItemRequest(sourced_id=sourced_id)

    # Call the API
    resp = client.oneroster.gradebook.delete_line_item(request)

    if resp is None:
        print(f"Line Item Deleted Successfully!")
        print(f"Line item {sourced_id} has been soft deleted (status set to 'tobedeleted')")
    else:
        print(f"Response: {resp}")


if __name__ == "__main__":
    main()

