from timeback import Timeback
from timeback.models.request import TimebackCreateAssessmentLineItemRequest, TimebackCreateAssessmentLineItemBody
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


def main():
    client = Timeback()

    body = TimebackCreateAssessmentLineItemBody(
        title="Test Quiz",
        assignDate="2024-01-01",
        dueDate="2024-01-15",
        class_=TimebackSourcedIdReference(sourcedId="<class-id>"),
        school=TimebackSourcedIdReference(sourcedId="<school-id>"),
        category=TimebackSourcedIdReference(sourcedId="<category-id>"),
        description="A test quiz for demonstration",
        resultValueMin=0.0,
        resultValueMax=100.0,
    )
    request = TimebackCreateAssessmentLineItemRequest(assessmentLineItem=body)
    response = client.oneroster.gradebook.create_assessment_line_item(request)

    print(f"Created assessment line item:")
    print(f"  Supplied ID: {response.sourcedIdPairs.suppliedSourcedId}")
    print(f"  Allocated ID: {response.sourcedIdPairs.allocatedSourcedId}")


if __name__ == "__main__":
    main()

