"""API test for assessment item endpoints.

This script tests all assessment item CRUD endpoints against the QTI API.
Run with: python -m tests.api.qti.assessment_items

Requires environment variables:
- TIMEBACK_CLIENT_ID
- TIMEBACK_CLIENT_SECRET
- TIMEBACK_ENVIRONMENT (production or staging)
"""

from timeback import Timeback
from timeback.models.request import (
    TimebackSearchAssessmentItemsRequest,
    TimebackCreateAssessmentItemRequest,
    TimebackUpdateAssessmentItemRequest,
)
from timeback.enums import TimebackQTIAssessmentItemSortField, TimebackSortOrder


SAMPLE_QTI_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<qti-assessment-item
  xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  identifier="api-test-item-{unique_id}"
  title="API Test Question"
  adaptive="false"
  time-dependent="false">
  <qti-response-declaration identifier="RESPONSE" cardinality="single" base-type="identifier">
    <qti-correct-response>
      <qti-value>B</qti-value>
    </qti-correct-response>
  </qti-response-declaration>
  <qti-outcome-declaration identifier="SCORE" cardinality="single" base-type="float"/>
  <qti-item-body>
    <qti-choice-interaction response-identifier="RESPONSE" max-choices="1">
      <qti-prompt>What is 2 + 2?</qti-prompt>
      <qti-simple-choice identifier="A">3</qti-simple-choice>
      <qti-simple-choice identifier="B">4</qti-simple-choice>
      <qti-simple-choice identifier="C">5</qti-simple-choice>
    </qti-choice-interaction>
  </qti-item-body>
  <qti-response-processing template="match_correct"/>
</qti-assessment-item>'''


UPDATED_QTI_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<qti-assessment-item
  xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  identifier="api-test-item-{unique_id}"
  title="Updated API Test Question"
  adaptive="false"
  time-dependent="false">
  <qti-response-declaration identifier="RESPONSE" cardinality="single" base-type="identifier">
    <qti-correct-response>
      <qti-value>C</qti-value>
    </qti-correct-response>
  </qti-response-declaration>
  <qti-outcome-declaration identifier="SCORE" cardinality="single" base-type="float"/>
  <qti-item-body>
    <qti-choice-interaction response-identifier="RESPONSE" max-choices="1">
      <qti-prompt>What is 3 + 3?</qti-prompt>
      <qti-simple-choice identifier="A">5</qti-simple-choice>
      <qti-simple-choice identifier="B">7</qti-simple-choice>
      <qti-simple-choice identifier="C">6</qti-simple-choice>
    </qti-choice-interaction>
  </qti-item-body>
  <qti-response-processing template="match_correct"/>
</qti-assessment-item>'''


def main():
    """Test the assessment item CRUD endpoints."""
    import time
    
    client = Timeback()
    unique_id = str(int(time.time()))
    created_identifier = None

    print("=" * 60)
    print("Testing Assessment Item Endpoints")
    print("=" * 60)

    try:
        # 1. Search for assessment items
        print("\n1. Search assessment items:")
        search_request = TimebackSearchAssessmentItemsRequest(limit=5)
        search_response = client.qti.search_assessment_items(search_request)
        print(f"   Total items: {search_response.total}")
        print(f"   Items on page: {len(search_response.items)}")
        
        if search_response.items:
            first_item = search_response.items[0]
            print(f"   First item: {first_item.identifier} - {first_item.title}")

        # 2. Create a new assessment item
        print("\n2. Create assessment item:")
        xml_content = SAMPLE_QTI_XML.format(unique_id=unique_id)
        create_request = TimebackCreateAssessmentItemRequest(
            format="xml",
            xml=xml_content,
            metadata={"subject": "Math", "grade": "5", "difficulty": "medium"}
        )
        created_item = client.qti.create_assessment_item(create_request)
        created_identifier = created_item.identifier
        print(f"   Created: {created_item.identifier}")
        print(f"   Title: {created_item.title}")
        print(f"   Type: {created_item.type}")

        # 3. Get the created assessment item
        print("\n3. Get assessment item:")
        fetched_item = client.qti.get_assessment_item(created_identifier)
        print(f"   Identifier: {fetched_item.identifier}")
        print(f"   Title: {fetched_item.title}")
        print(f"   Type: {fetched_item.type}")
        print(f"   QTI Version: {fetched_item.qtiVersion}")
        if fetched_item.metadata:
            print(f"   Metadata: {fetched_item.metadata}")

        # 4. Update the assessment item
        print("\n4. Update assessment item:")
        updated_xml = UPDATED_QTI_XML.format(unique_id=unique_id)
        update_request = TimebackUpdateAssessmentItemRequest(
            format="xml",
            xml=updated_xml,
            metadata={"subject": "Math", "grade": "6", "difficulty": "hard"}
        )
        updated_item = client.qti.update_assessment_item(created_identifier, update_request)
        print(f"   Updated title: {updated_item.title}")
        if updated_item.metadata:
            print(f"   Updated metadata: {updated_item.metadata}")

        # 5. Verify the update
        print("\n5. Verify update:")
        verified_item = client.qti.get_assessment_item(created_identifier)
        print(f"   Title after update: {verified_item.title}")

        # 6. Delete the assessment item
        print("\n6. Delete assessment item:")
        client.qti.delete_assessment_item(created_identifier)
        print(f"   Deleted: {created_identifier}")
        created_identifier = None  # Mark as deleted

    except Exception as e:
        print(f"\nError: {e}")
        raise
    finally:
        # Cleanup: Delete the assessment item if it was created but not deleted
        if created_identifier:
            print(f"\n   Cleanup: Deleting {created_identifier}")
            try:
                client.qti.delete_assessment_item(created_identifier)
            except Exception:
                pass

    print("\n" + "=" * 60)
    print("Assessment Item tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

