"""QTI endpoints.

Each endpoint file in this directory handles a single API call to the QTI API.
QTI uses a dedicated base URL: https://qti.alpha-1edtech.ai/api (production)

Structure:
- Stimuli endpoints: search_stimuli, create_stimulus, get_stimulus, update_stimulus, delete_stimulus
- Assessment Item endpoints: search_assessment_items, create_assessment_item, get_assessment_item, etc.
- Assessment Test endpoints: search_assessment_tests, create_assessment_test, get_assessment_test, etc.
- Test Part endpoints: search_test_parts, create_test_part, get_test_part, etc.
- Section endpoints: search_sections, create_section, get_section, etc.
- Feedback endpoints: create_question_feedback, create_lesson_feedback, get_feedback_by_lesson_id, etc.
- Validation endpoints: validate_xml, validate_batch
"""

