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

from .search_stimuli import search_stimuli
from .create_stimulus import create_stimulus
from .get_stimulus import get_stimulus
from .update_stimulus import update_stimulus
from .delete_stimulus import delete_stimulus
from .search_assessment_items import search_assessment_items
from .get_assessment_item import get_assessment_item
from .create_assessment_item import create_assessment_item
from .update_assessment_item import update_assessment_item
from .delete_assessment_item import delete_assessment_item
from .process_response import process_response
from .search_assessment_tests import search_assessment_tests
from .get_assessment_test import get_assessment_test
from .create_assessment_test import create_assessment_test
from .update_assessment_test import update_assessment_test
from .delete_assessment_test import delete_assessment_test
from .update_metadata import update_metadata

__all__ = [
    # Stimuli
    "search_stimuli",
    "create_stimulus",
    "get_stimulus",
    "update_stimulus",
    "delete_stimulus",
    # Assessment Items
    "search_assessment_items",
    "get_assessment_item",
    "create_assessment_item",
    "update_assessment_item",
    "delete_assessment_item",
    "process_response",
    # Assessment Tests
    "search_assessment_tests",
    "get_assessment_test",
    "create_assessment_test",
    "update_assessment_test",
    "delete_assessment_test",
    "update_metadata",
]

