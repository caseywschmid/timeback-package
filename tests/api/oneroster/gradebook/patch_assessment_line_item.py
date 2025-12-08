from timeback import Timeback
from timeback.models.request import TimebackPatchAssessmentLineItemRequest, TimebackPatchAssessmentLineItemBody


def main():
    client = Timeback()
    sourced_id = "<assessment-line-item-id>"  # Replace with actual ID

    # Partial update - just update the title and description
    body = TimebackPatchAssessmentLineItemBody(
        title="Patched Quiz Title",
        description="Updated description via PATCH",
    )
    request = TimebackPatchAssessmentLineItemRequest(sourced_id=sourced_id, assessmentLineItem=body)
    response = client.oneroster.gradebook.patch_assessment_line_item(request)

    print(f"Patched: {response.assessmentLineItem.sourcedId}")
    print(f"  Title: {response.assessmentLineItem.title}")


if __name__ == "__main__":
    main()

