"""API test for update_metadata endpoint.

This script tests the update_metadata endpoint against the QTI API.
Run with: python -m tests.api.qti.update_metadata

Requires environment variables:
- TIMEBACK_CLIENT_ID
- TIMEBACK_CLIENT_SECRET
- TIMEBACK_ENVIRONMENT (production or staging)
"""

from timeback import Timeback
from timeback.models.request import TimebackUpdateAssessmentItemMetadataRequest


SAMPLE_QTI_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<qti-assessment-item
  xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
  identifier="metadata-test-item"
  title="Metadata Test Item"
  adaptive="false"
  time-dependent="false">
  <qti-response-declaration identifier="RESPONSE" cardinality="single" base-type="identifier">
    <qti-correct-response>
      <qti-value>B</qti-value>
    </qti-correct-response>
  </qti-response-declaration>
  <qti-item-body>
    <qti-choice-interaction response-identifier="RESPONSE" max-choices="1">
      <qti-prompt>What is 2 + 2?</qti-prompt>
      <qti-simple-choice identifier="A">3</qti-simple-choice>
      <qti-simple-choice identifier="B">4</qti-simple-choice>
    </qti-choice-interaction>
  </qti-item-body>
</qti-assessment-item>'''


def main():
    """Test the update_metadata endpoint."""
    client = Timeback()

    print("=" * 60)
    print("Testing update_metadata endpoint")
    print("=" * 60)

    # Update metadata
    print("\n1. Update metadata for an assessment item:")
    request = TimebackUpdateAssessmentItemMetadataRequest(
        format="xml",
        xml=SAMPLE_QTI_XML,
        metadata={
            "subject": "Math",
            "grade": "5",
            "difficulty": "medium"
        }
    )
    
    try:
        result = client.qti.update_metadata(request)
        print(f"   Updated: {result.identifier}")
        print(f"   Title: {result.title}")
        if result.metadata:
            print(f"   Metadata: {result.metadata}")
    except Exception as e:
        print(f"   Error: {e}")

    print("\n" + "=" * 60)
    print("update_metadata test completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

