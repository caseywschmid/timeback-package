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
    TimebackSearchAssessmentTestsRequest,
    TimebackCreateAssessmentTestRequest,
    TimebackUpdateAssessmentTestRequest,
    TimebackUpdateAssessmentItemMetadataRequest,
    TimebackUpdateAssessmentTestMetadataRequest,
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
    TimebackSearchAssessmentTestsResponse,
    TimebackGetAssessmentTestResponse,
    TimebackCreateAssessmentTestResponse,
    TimebackUpdateAssessmentTestResponse,
    TimebackUpdateAssessmentItemMetadataResponse,
    TimebackGetAllQuestionsResponse,
    TimebackUpdateAssessmentTestMetadataResponse,
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
from timeback.services.qti.endpoints import update_metadata as update_metadata_endpoint
from timeback.services.qti.endpoints import search_assessment_tests as search_assessment_tests_endpoint
from timeback.services.qti.endpoints import get_assessment_test as get_assessment_test_endpoint
from timeback.services.qti.endpoints import create_assessment_test as create_assessment_test_endpoint
from timeback.services.qti.endpoints import update_assessment_test as update_assessment_test_endpoint
from timeback.services.qti.endpoints import delete_assessment_test as delete_assessment_test_endpoint
from timeback.services.qti.endpoints import get_all_questions as get_all_questions_endpoint
from timeback.services.qti.endpoints import update_assessment_test_metadata as update_assessment_test_metadata_endpoint


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

    def update_metadata(
        self,
        request: TimebackUpdateAssessmentItemMetadataRequest
    ) -> TimebackUpdateAssessmentItemMetadataResponse:
        """Update metadata for assessment items.
        
        POST /assessment-items/metadata
        
        This operation is used to update metadata for assessment items,
        such as resetting the human approved status.
        
        Args:
            request: Request containing format, xml content, and metadata to update.
                     See TimebackUpdateAssessmentItemMetadataRequest for details.
        
        Returns:
            TimebackUpdateAssessmentItemMetadataResponse containing the updated item
        """
        return update_metadata_endpoint(self._http, request)

    # ==========================================================================
    # ASSESSMENT TEST ENDPOINTS
    # ==========================================================================
    # Endpoints for managing assessment tests (complete tests with structure).
    # Base path: /assessment-tests
    # ==========================================================================

    def search_assessment_tests(
        self,
        request: Optional[TimebackSearchAssessmentTestsRequest] = None
    ) -> TimebackSearchAssessmentTestsResponse:
        """Search and filter QTI assessment tests.
        
        GET /assessment-tests
        
        Retrieves a paginated list of assessment tests with optional filtering.
        Supports fuzzy text search, navigation mode, and submission mode filtering.
        
        Args:
            request: Optional search parameters including query, pagination, sorting,
                     navigation_mode, submission_mode, and filter.
                     If not provided, returns first page with defaults.
        
        Returns:
            TimebackSearchAssessmentTestsResponse containing paginated tests list
        """
        return search_assessment_tests_endpoint(self._http, request)

    def get_assessment_test(self, identifier: str) -> TimebackGetAssessmentTestResponse:
        """Get a specific QTI assessment test by identifier.
        
        GET /assessment-tests/{identifier}
        
        Retrieves a complete assessment test including all its test parts,
        sections, and assessment item references.
        
        Args:
            identifier: Unique identifier of the assessment test to retrieve
        
        Returns:
            TimebackGetAssessmentTestResponse containing the complete test
        """
        return get_assessment_test_endpoint(self._http, identifier)

    def create_assessment_test(
        self,
        request: TimebackCreateAssessmentTestRequest
    ) -> TimebackCreateAssessmentTestResponse:
        """Create a new QTI assessment test.
        
        POST /assessment-tests
        
        Creates a new assessment test on the service provider.
        The recommended approach is to send format='xml' with QTI XML content.
        
        Args:
            request: Assessment test data including format, xml/content, and metadata.
                     See TimebackCreateAssessmentTestRequest for all available fields.
        
        Returns:
            TimebackCreateAssessmentTestResponse containing the created test
        """
        return create_assessment_test_endpoint(self._http, request)

    def update_assessment_test(
        self,
        identifier: str,
        request: TimebackUpdateAssessmentTestRequest
    ) -> TimebackUpdateAssessmentTestResponse:
        """Update an existing QTI assessment test.
        
        PUT /assessment-tests/{identifier}
        
        Updates an entire assessment test by replacing its complete structure.
        This operation updates the test including its test parts, sections, and
        item references.
        
        Args:
            identifier: Unique identifier of the assessment test to update
            request: Assessment test update data including format, xml/content, and metadata.
                     See TimebackUpdateAssessmentTestRequest for all available fields.
        
        Returns:
            TimebackUpdateAssessmentTestResponse containing the updated test
        """
        return update_assessment_test_endpoint(self._http, identifier, request)

    def delete_assessment_test(self, identifier: str) -> None:
        """Delete a QTI assessment test.
        
        DELETE /assessment-tests/{identifier}
        
        Permanently deletes an assessment test and all its associated data
        including test parts, sections, and item references. This operation
        cannot be undone. The actual assessment items are NOT deleted.
        
        Args:
            identifier: Unique identifier of the assessment test to delete
        
        Warning:
            This operation cannot be undone.
        """
        return delete_assessment_test_endpoint(self._http, identifier)

    def get_all_questions(self, identifier: str) -> TimebackGetAllQuestionsResponse:
        """Get all assessment items referenced by an assessment test.
        
        GET /assessment-tests/{identifier}/questions
        
        Retrieves all assessment items (questions) that are referenced by
        an assessment test, along with their structural context (test part
        and section).
        
        Args:
            identifier: Unique identifier of the assessment test
        
        Returns:
            TimebackGetAllQuestionsResponse containing:
                - assessment_test: Test identifier
                - title: Test title
                - total_questions: Total count of questions
                - questions: List of questions with reference info and item data
        """
        return get_all_questions_endpoint(self._http, identifier)

    def update_assessment_test_metadata(
        self,
        identifier: str,
        request: TimebackUpdateAssessmentTestMetadataRequest
    ) -> TimebackUpdateAssessmentTestMetadataResponse:
        """Update only the metadata fields of an assessment test.
        
        PUT /assessment-tests/{identifier}/metadata
        
        This is a lightweight operation for administrative changes to metadata
        properties without affecting the test structure, test parts, sections,
        or assessment items.
        
        Args:
            identifier: Unique identifier of the assessment test to update
            request: Request containing metadata to update.
                     See TimebackUpdateAssessmentTestMetadataRequest for details.
        
        Returns:
            TimebackUpdateAssessmentTestMetadataResponse containing the updated test
        """
        return update_assessment_test_metadata_endpoint(self._http, identifier, request)

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

