from timeback import Timeback
from timeback.models.request import TimebackGetAssessmentResultRequest, TimebackQueryParams


def main():
    client = Timeback()
    sourced_id = "test-assessment-result-001"  # Replace with actual assessment result sourcedId

    # Basic request without query params
    request = TimebackGetAssessmentResultRequest(sourced_id=sourced_id)
    response = client.oneroster.gradebook.get_assessment_result(request)

    print(f"Assessment Result: {response.assessmentResult.sourcedId}")
    print(f"  Score: {response.assessmentResult.score}")
    print(f"  Score Status: {response.assessmentResult.scoreStatus}")
    print(f"  Score Date: {response.assessmentResult.scoreDate}")
    print(f"  Student: {response.assessmentResult.student.sourcedId}")

    # Example with fields query param
    query_params = TimebackQueryParams(fields=["sourcedId", "score", "scoreStatus"])
    request_with_fields = TimebackGetAssessmentResultRequest(
        sourced_id=sourced_id,
        query_params=query_params
    )
    response_min = client.oneroster.gradebook.get_assessment_result(request_with_fields)
    print(f"\nMinimal: {response_min.assessmentResult.sourcedId}, score={response_min.assessmentResult.score}")


if __name__ == "__main__":
    main()

