from timeback import Timeback
from timeback.models.request import TimebackDeleteScoreScaleRequest


def main():
    client = Timeback()
    sourced_id = "scale-123-456"

    # Create the request
    print(f"Deleting score scale: {sourced_id}")
    request = TimebackDeleteScoreScaleRequest(sourced_id=sourced_id)

    # Call the API
    client.oneroster.gradebook.delete_score_scale(request)

    print(f"Score Scale Deleted Successfully!")


if __name__ == "__main__":
    main()
