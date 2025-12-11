"""API test for get_all_questions endpoint.

This script tests the get_all_questions endpoint against the QTI API.
Run with: python -m tests.api.qti.get_all_questions

Requires environment variables:
- TIMEBACK_CLIENT_ID
- TIMEBACK_CLIENT_SECRET
- TIMEBACK_ENVIRONMENT (production or staging)
"""

from timeback import Timeback
from timeback.models.request import TimebackSearchAssessmentTestsRequest


def main():
    """Test the get_all_questions endpoint."""
    client = Timeback()

    print("=" * 60)
    print("Testing get_all_questions endpoint")
    print("=" * 60)

    # First, find an assessment test to query
    print("\n1. Finding an assessment test with questions...")
    search_response = client.qti.search_assessment_tests(
        TimebackSearchAssessmentTestsRequest(limit=5)
    )
    
    if not search_response.items:
        print("   No assessment tests found. Create one first.")
        return

    # Use the first test
    test = search_response.items[0]
    print(f"   Using test: {test.identifier} - {test.title}")

    # Get all questions
    print("\n2. Getting all questions from the test:")
    try:
        result = client.qti.get_all_questions(test.identifier)
        
        print(f"   Test: {result.title}")
        print(f"   Total questions: {result.total_questions}")
        
        if result.questions:
            print(f"\n   Questions:")
            for i, q in enumerate(result.questions[:5], 1):
                ref = q.reference
                print(f"   {i}. {q.question.title if q.question else 'N/A'}")
                print(f"      - Part: {ref.test_part}, Section: {ref.section}")
                if q.question:
                    print(f"      - Type: {q.question.type}")
            
            if len(result.questions) > 5:
                print(f"   ... and {len(result.questions) - 5} more questions")
        else:
            print("   No questions found in this test.")
    except Exception as e:
        print(f"   Error: {e}")

    print("\n" + "=" * 60)
    print("get_all_questions test completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

