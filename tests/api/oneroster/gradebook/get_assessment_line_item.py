from timeback import Timeback
from timeback.models.request import TimebackGetAssessmentLineItemRequest


def main():
    client = Timeback()
    sourced_id = "<assessment-line-item-id>"  # Replace with actual ID

    request = TimebackGetAssessmentLineItemRequest(sourced_id=sourced_id)
    response = client.oneroster.gradebook.get_assessment_line_item(request)

    ali = response.assessmentLineItem
    print(f"Assessment Line Item: {ali.sourcedId}")
    print(f"  Title: {ali.title}")
    print(f"  Assign Date: {ali.assignDate}")
    print(f"  Due Date: {ali.dueDate}")
    print(f"  Status: {ali.status}")


if __name__ == "__main__":
    main()

