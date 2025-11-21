from timeback import Timeback
from timeback.models.request import TimebackDeleteResultRequest


def main():
    client = Timeback()
    sourced_id = "result-123-456"

    # Create the request
    print(f"Deleting result: {sourced_id}")
    request = TimebackDeleteResultRequest(sourced_id=sourced_id)

    # Call the API
    client.oneroster.gradebook.delete_result(request)

    print(f"Result Deleted Successfully!")


if __name__ == "__main__":
    main()

