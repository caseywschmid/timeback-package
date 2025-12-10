"""QTI service for the QTI API.

This service provides methods for managing QTI (Question and Test Interoperability) content:
- Stimuli: Shared content/passages used across multiple assessment items
- Assessment Items: Individual questions/tasks with response processing
- Assessment Tests: Complete tests containing test parts, sections, and items
- Test Parts: Major divisions within an assessment test
- Sections: Groupings of items within test parts
- Feedback: Question and lesson feedback management
- Validation: XML validation for QTI content

QTI uses a dedicated base URL separate from OneRoster:
- Production: https://qti.alpha-1edtech.ai/api
- Staging: https://qti-staging.alpha-1edtech.ai/api

Used by:
- timeback/client.py - instantiated and exposed as client.qti
"""

from typing import Optional

from timeback.http import HttpClient
from timeback.models.request import (
    TimebackSearchStimuliRequest,
    TimebackCreateStimulusRequest,
    TimebackUpdateStimulusRequest,
    TimebackSearchAssessmentItemsRequest,
    TimebackCreateAssessmentItemRequest,
    TimebackUpdateAssessmentItemRequest,
    TimebackProcessResponseRequest,
)
from timeback.models.response import (
    TimebackSearchStimuliResponse,
    TimebackCreateStimulusResponse,
    TimebackGetStimulusResponse,
    TimebackUpdateStimulusResponse,
    TimebackSearchAssessmentItemsResponse,
    TimebackGetAssessmentItemResponse,
    TimebackCreateAssessmentItemResponse,
    TimebackUpdateAssessmentItemResponse,
    TimebackProcessResponseResponse,
)
from timeback.services.qti.endpoints import search_stimuli as search_stimuli_endpoint
from timeback.services.qti.endpoints import create_stimulus as create_stimulus_endpoint
from timeback.services.qti.endpoints import get_stimulus as get_stimulus_endpoint
from timeback.services.qti.endpoints import update_stimulus as update_stimulus_endpoint
from timeback.services.qti.endpoints import delete_stimulus as delete_stimulus_endpoint
from timeback.services.qti.endpoints import search_assessment_items as search_assessment_items_endpoint
from timeback.services.qti.endpoints import get_assessment_item as get_assessment_item_endpoint
from timeback.services.qti.endpoints import create_assessment_item as create_assessment_item_endpoint
from timeback.services.qti.endpoints import update_assessment_item as update_assessment_item_endpoint
from timeback.services.qti.endpoints import delete_assessment_item as delete_assessment_item_endpoint
from timeback.services.qti.endpoints import process_response as process_response_endpoint


class QTIService:
    """QTI service methods.

    This service handles all QTI API interactions for managing question and test
    interoperability content following the IMS QTI specification.

    Usage:
        client = Timeback()
        
        # Stimuli
        stimuli = client.qti.search_stimuli(request)
        stimulus = client.qti.get_stimulus(request)
        
        # Assessment Items
        items = client.qti.search_assessment_items(request)
        item = client.qti.get_assessment_item(request)
        
        # Assessment Tests
        tests = client.qti.search_assessment_tests(request)
        test = client.qti.get_assessment_test(request)
        
        # Validation
        result = client.qti.validate_xml(request)
    """

    def __init__(self, http: HttpClient):
        """Initialize QTIService with an HTTP client.

        Args:
            http: The HttpClient instance configured for the QTI API base URL.
                  QTI uses a dedicated base URL (qti.alpha-1edtech.ai/api).
        """
        self._http = http

    # ==========================================================================
    # STIMULI ENDPOINTS
    # ==========================================================================
    # Endpoints for managing stimuli (shared content/passages for assessment items).
    # Base path: /stimuli
    # ==========================================================================

    def search_stimuli(
        self,
        request: Optional[TimebackSearchStimuliRequest] = None
    ) -> TimebackSearchStimuliResponse:
        """Search and filter QTI stimuli.
        
        GET /stimuli
        
        Retrieves a paginated list of stimuli with optional filtering.
        Supports fuzzy text search across title and identifier fields.
        
        Args:
            request: Optional search parameters including query, pagination, and sorting.
                     If not provided, returns first page with default settings.
        
        Returns:
            TimebackSearchStimuliResponse containing paginated stimuli list
        """
        return search_stimuli_endpoint(self._http, request)

    def create_stimulus(
        self,
        request: TimebackCreateStimulusRequest
    ) -> TimebackCreateStimulusResponse:
        """Create a new QTI stimulus.
        
        POST /stimuli
        
        Creates a new stimulus on the service provider. Stimuli can be
        referenced by assessment items and provide shared content/passages.
        
        Args:
            request: Stimulus data including identifier, title, and content.
                     See TimebackCreateStimulusRequest for all available fields.
        
        Returns:
            TimebackCreateStimulusResponse containing the created stimulus
        """
        return create_stimulus_endpoint(self._http, request)

    def get_stimulus(self, identifier: str) -> TimebackGetStimulusResponse:
        """Get a specific QTI stimulus by identifier.
        
        GET /stimuli/{identifier}
        
        Retrieves a single stimulus with its complete content.
        
        Args:
            identifier: Unique identifier of the stimulus to retrieve
        
        Returns:
            TimebackGetStimulusResponse containing the complete stimulus data
        """
        return get_stimulus_endpoint(self._http, identifier)

    def update_stimulus(
        self,
        request: TimebackUpdateStimulusRequest
    ) -> TimebackUpdateStimulusResponse:
        """Update an existing QTI stimulus.
        
        PUT /stimuli/{identifier}
        
        Updates a stimulus on the service provider with new content.
        
        Args:
            request: Stimulus update data including identifier, title, and content.
                     See TimebackUpdateStimulusRequest for all available fields.
        
        Returns:
            TimebackUpdateStimulusResponse containing the updated stimulus
        """
        return update_stimulus_endpoint(self._http, request)

    def delete_stimulus(self, identifier: str) -> None:
        """Delete a QTI stimulus.
        
        DELETE /stimuli/{identifier}
        
        Permanently deletes a stimulus from the service provider. This operation
        cannot be undone.
        
        Args:
            identifier: Unique identifier of the stimulus to delete
        
        Warning:
            Assessment items referencing this stimulus may be affected.
        """
        return delete_stimulus_endpoint(self._http, identifier)

    # ==========================================================================
    # ASSESSMENT ITEM ENDPOINTS
    # ==========================================================================
    # Endpoints for managing assessment items (individual questions/tasks).
    # Base path: /assessment-items
    #
    # TODO: Implement the following endpoints:
    # - update_metadata: PUT /assessment-items/metadata (batch metadata update)
    # ==========================================================================

    def search_assessment_items(
        self,
        request: Optional[TimebackSearchAssessmentItemsRequest] = None
    ) -> TimebackSearchAssessmentItemsResponse:
        """Search and filter QTI assessment items.
        
        GET /assessment-items
        
        Retrieves a paginated list of assessment items with optional filtering.
        Supports fuzzy text search and advanced filtering by type.
        
        Args:
            request: Optional search parameters including query, pagination, sorting,
                     and filter. If not provided, returns first page with defaults.
        
        Returns:
            TimebackSearchAssessmentItemsResponse containing paginated items list
        """
        return search_assessment_items_endpoint(self._http, request)

    def get_assessment_item(self, identifier: str) -> TimebackGetAssessmentItemResponse:
        """Get a specific QTI assessment item by identifier.
        
        GET /assessment-items/{identifier}
        
        Retrieves a complete assessment item including its question content,
        answer choices, interaction types, response processing rules, and scoring logic.
        
        Args:
            identifier: Unique identifier of the assessment item to retrieve
        
        Returns:
            TimebackGetAssessmentItemResponse containing the complete assessment item
        """
        return get_assessment_item_endpoint(self._http, identifier)

    def create_assessment_item(
        self,
        request: TimebackCreateAssessmentItemRequest
    ) -> TimebackCreateAssessmentItemResponse:
        """Create a new QTI assessment item.
        
        POST /assessment-items
        
        Creates a new assessment item on the service provider. The recommended
        approach is to send format='xml' with QTI XML content that validates
        against IMS QTI XSDs.
        
        Args:
            request: Assessment item data including format, xml/content, and metadata.
                     See TimebackCreateAssessmentItemRequest for all available fields.
        
        Returns:
            TimebackCreateAssessmentItemResponse containing the created item
        """
        return create_assessment_item_endpoint(self._http, request)

    def update_assessment_item(
        self,
        identifier: str,
        request: TimebackUpdateAssessmentItemRequest
    ) -> TimebackUpdateAssessmentItemResponse:
        """Update an existing QTI assessment item.
        
        PUT /assessment-items/{identifier}
        
        Updates an assessment item including its question content, interactions,
        response processing, and scoring logic. This operation regenerates the
        QTI XML structure and validates all content.
        
        Args:
            identifier: Unique identifier of the assessment item to update
            request: Assessment item update data including format, xml/content, and metadata.
                     See TimebackUpdateAssessmentItemRequest for all available fields.
        
        Returns:
            TimebackUpdateAssessmentItemResponse containing the updated item
        """
        return update_assessment_item_endpoint(self._http, identifier, request)

    def delete_assessment_item(self, identifier: str) -> None:
        """Delete a QTI assessment item.
        
        DELETE /assessment-items/{identifier}
        
        Permanently deletes an assessment item from the service provider.
        This operation cannot be undone.
        
        Args:
            identifier: Unique identifier of the assessment item to delete
        
        Warning:
            Assessment tests that reference this item may be affected.
            The item references in test sections will need to be updated separately.
        """
        return delete_assessment_item_endpoint(self._http, identifier)

    def process_response(
        self,
        identifier: str,
        request: TimebackProcessResponseRequest
    ) -> TimebackProcessResponseResponse:
        """Process a candidate's response to an assessment item.
        
        POST /assessment-items/{identifier}/process-response
        
        Validates the response against the item's response processing rules
        and returns the score and feedback.
        
        Args:
            identifier: Unique identifier of the assessment item
            request: Request containing the item identifier and candidate's response.
                     See TimebackProcessResponseRequest for details.
        
        Returns:
            TimebackProcessResponseResponse containing:
                - score: Numerical score (0.0-1.0)
                - feedback: Structured feedback with identifier and message
        """
        return process_response_endpoint(self._http, identifier, request)

    # ==========================================================================
    # ASSESSMENT TEST ENDPOINTS
    # ==========================================================================
    # Endpoints for managing assessment tests (complete tests with structure).
    # Base path: /assessment-tests
    #
    # TODO: Implement the following endpoints:
    # - search_assessment_tests: GET /assessment-tests
    # - create_assessment_test: POST /assessment-tests
    # - get_assessment_test: GET /assessment-tests/{identifier}
    # - update_assessment_test: PUT /assessment-tests/{identifier}
    # - delete_assessment_test: DELETE /assessment-tests/{identifier}
    # - get_all_questions: GET /assessment-tests/{identifier}/questions
    # - update_assessment_test_metadata: PUT /assessment-tests/{identifier}/metadata
    # ==========================================================================

    # ==========================================================================
    # TEST PART ENDPOINTS
    # ==========================================================================
    # Endpoints for managing test parts (major divisions within assessment tests).
    # Base path: /assessment-tests/{assessmentTestIdentifier}/test-parts
    #
    # TODO: Implement the following endpoints:
    # - search_test_parts: GET /assessment-tests/{assessmentTestIdentifier}/test-parts
    # - create_test_part: POST /assessment-tests/{assessmentTestIdentifier}/test-parts
    # - get_test_part: GET /assessment-tests/{assessmentTestIdentifier}/test-parts/{identifier}
    # - update_test_part: PUT /assessment-tests/{assessmentTestIdentifier}/test-parts/{identifier}
    # - delete_test_part: DELETE /assessment-tests/{assessmentTestIdentifier}/test-parts/{identifier}
    # ==========================================================================

    # ==========================================================================
    # SECTION ENDPOINTS
    # ==========================================================================
    # Endpoints for managing sections (groupings of items within test parts).
    # Base path: /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections
    #
    # TODO: Implement the following endpoints:
    # - search_sections: GET .../sections
    # - create_section: POST .../sections
    # - get_section: GET .../sections/{identifier}
    # - update_section: PUT .../sections/{identifier}
    # - delete_section: DELETE .../sections/{identifier}
    # - add_assessment_item: POST .../sections/{identifier}/items
    # - remove_assessment_item: DELETE .../sections/{identifier}/items/{itemIdentifier}
    # - update_assessment_item_order: PUT .../sections/{identifier}/items/order
    # ==========================================================================

    # ==========================================================================
    # FEEDBACK ENDPOINTS
    # ==========================================================================
    # Endpoints for managing question and lesson feedback.
    # Base paths: /question, /lesson, /{id}
    #
    # TODO: Implement the following endpoints:
    # - create_question_feedback: POST /question
    # - create_lesson_feedback: POST /lesson
    # - get_feedback_by_lesson_id: GET /lesson/{lessonId}
    # - delete_feedback: DELETE /{id}
    # ==========================================================================

    # ==========================================================================
    # VALIDATION ENDPOINTS
    # ==========================================================================
    # Endpoints for validating QTI XML content.
    # Base path: /validate
    #
    # TODO: Implement the following endpoints:
    # - validate_xml: POST /validate
    # - validate_batch: POST /validate/batch
    # ==========================================================================

