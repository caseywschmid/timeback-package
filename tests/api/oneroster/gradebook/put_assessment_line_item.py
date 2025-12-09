from timeback import Timeback
from timeback.models.request import TimebackPutAssessmentLineItemRequest, TimebackPutAssessmentLineItemBody
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


def main():
    client = Timeback()
    sourced_id = "<assessment-line-item-id>"  # Replace with actual ID

    body = TimebackPutAssessmentLineItemBody(
        sourcedId=sourced_id,
        title="Updated Quiz Title",
        assignDate="2024-01-01",
        dueDate="2024-01-20",
        class_=TimebackSourcedIdReference(sourcedId="<class-id>"),
        school=TimebackSourcedIdReference(sourcedId="<school-id>"),
        category=TimebackSourcedIdReference(sourcedId="<category-id>"),
    )
    request = TimebackPutAssessmentLineItemRequest(sourced_id=sourced_id, assessmentLineItem=body)
    response = client.oneroster.gradebook.put_assessment_line_item(request)

    print(f"Updated: {response.assessmentLineItem.sourcedId}")
    print(f"  Title: {response.assessmentLineItem.title}")


if __name__ == "__main__":
    main()

