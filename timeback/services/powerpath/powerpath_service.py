"""PowerPath service for the PowerPath API.

This service provides methods for:
- Placement testing (get_all_placement_tests, get_current_level, get_next_placement_test, etc.)
- Screening (get_results, get_session, assign_test)
- Lesson plans (create_lesson_plan, get_tree, get_operations, sync_operations, etc.)
- Adaptive assessments (create_new_attempt, get_next_question, update_student_question_response, etc.)
- Syllabus retrieval (get_course_syllabus)

All endpoints use the base path: /powerpath/...

Used by:
- timeback/client.py - instantiated and exposed as client.powerpath
"""

from timeback.http import HttpClient
from typing import Optional, Union
from timeback.models.request import (
    TimebackGetAllPlacementTestsRequest,
    TimebackGetCurrentLevelRequest,
    TimebackGetNextPlacementTestRequest,
    TimebackGetSubjectProgressRequest,
    TimebackAssignScreeningTestRequest,
    TimebackCreateExternalPlacementTestRequest,
    TimebackCreateExternalTestOutRequest,
    TimebackCreateInternalQtiTestRequest,
    TimebackCreateInternalAssessmentBankTestRequest,
    TimebackImportExternalTestAssignmentResultsRequest,
    TimebackMakeExternalTestAssignmentRequest,
    TimebackGetTestOutRequest,
    TimebackResetUserPlacementRequest,
    TimebackCreateLessonPlanRequest,
    TimebackStartTestOutRequest,
    TimebackGetTreeRequest,
    TimebackStoreOperationRequest,
    TimebackUpdateStudentItemResponseRequest,
    TimebackCreateNewAttemptRequest,
    TimebackFinalStudentAssessmentRequest,
    TimebackResetAttemptRequest,
    TimebackUpdateStudentQuestionResponseRequest,
)
from timeback.models.response import (
    TimebackGetAllPlacementTestsResponse,
    TimebackGetCurrentLevelResponse,
    TimebackGetNextPlacementTestResponse,
    TimebackGetSubjectProgressResponse,
    TimebackGetScreeningResultsResponse,
    TimebackCreateExternalTestResponse,
    TimebackCreateInternalTestResponse,
    TimebackImportExternalTestAssignmentResultsResponse,
    TimebackMakeExternalTestAssignmentResponse,
    TimebackGetTestOutResponse,
    TimebackResetUserPlacementResponse,
    TimebackCreateLessonPlanResponse,
    TimebackStartTestOutResponse,
    TimebackGetOperationsResponse,
    TimebackStoreOperationResponse,
    TimebackSyncOperationsResponse,
    TimebackSyncCourseLessonPlansResponse,
    TimebackCourseProgressResponse,
    TimebackLessonPlanStructureResponse,
    TimebackUpdateStudentItemResponseResponse,
    TimebackSyllabusResponse,
    TimebackCreateNewAttemptResponse,
    TimebackFinalStudentAssessmentResponse,
    TimebackAssessmentProgressResponse,
    TimebackGetAttemptsResponse,
    TimebackNextQuestionResponse,
    TimebackResetAttemptResponse,
    TimebackUpdateStudentQuestionResponseResponse,
)
from timeback.models import TimebackScreeningSession, LessonPlan
from timeback.services.powerpath.endpoints.get_all_placement_tests import (
    get_all_placement_tests as get_all_placement_tests_endpoint,
)
from timeback.services.powerpath.endpoints.get_current_level import (
    get_current_level as get_current_level_endpoint,
)
from timeback.services.powerpath.endpoints.get_next_placement_test import (
    get_next_placement_test as get_next_placement_test_endpoint,
)
from timeback.services.powerpath.endpoints.get_subject_progress import (
    get_subject_progress as get_subject_progress_endpoint,
)
from timeback.services.powerpath.endpoints.get_screening_results import (
    get_screening_results as get_screening_results_endpoint,
)
from timeback.services.powerpath.endpoints.get_screening_session import (
    get_screening_session as get_screening_session_endpoint,
)
from timeback.services.powerpath.endpoints.assign_screening_test import (
    assign_screening_test as assign_screening_test_endpoint,
)
from timeback.services.powerpath.endpoints.create_external_placement_test import (
    create_external_placement_test as create_external_placement_test_endpoint,
)
from timeback.services.powerpath.endpoints.create_external_test_out import (
    create_external_test_out as create_external_test_out_endpoint,
)
from timeback.services.powerpath.endpoints.create_internal_test import (
    create_internal_test as create_internal_test_endpoint,
)
from timeback.services.powerpath.endpoints.import_external_test_assignment_results import (
    import_external_test_assignment_results as import_external_test_assignment_results_endpoint,
)
from timeback.services.powerpath.endpoints.make_external_test_assignment import (
    make_external_test_assignment as make_external_test_assignment_endpoint,
)
from timeback.services.powerpath.endpoints.get_test_out import (
    get_test_out as get_test_out_endpoint,
)
from timeback.services.powerpath.endpoints.reset_user_placement import (
    reset_user_placement as reset_user_placement_endpoint,
)
from timeback.services.powerpath.endpoints.get_student_placement_data import (
    get_student_placement_data as get_student_placement_data_endpoint,
    StudentPlacementDataResponse,
)
from timeback.services.powerpath.endpoints.reset_screening_session import (
    reset_screening_session as reset_screening_session_endpoint,
)
from timeback.services.powerpath.endpoints.create_lesson_plan import (
    create_lesson_plan as create_lesson_plan_endpoint,
)
from timeback.services.powerpath.endpoints.start_test_out import (
    start_test_out as start_test_out_endpoint,
)
from timeback.services.powerpath.endpoints.get_tree import (
    get_tree as get_tree_endpoint,
)
from timeback.services.powerpath.endpoints.delete_lesson_plans_by_course_id import (
    delete_lesson_plans_by_course_id as delete_lesson_plans_by_course_id_endpoint,
)
from timeback.services.powerpath.endpoints.store_operation import (
    store_operation as store_operation_endpoint,
)
from timeback.services.powerpath.endpoints.get_operations import (
    get_operations as get_operations_endpoint,
)
from timeback.services.powerpath.endpoints.sync_operations import (
    sync_operations as sync_operations_endpoint,
)
from timeback.services.powerpath.endpoints.recreate_lesson_plan import (
    recreate_lesson_plan as recreate_lesson_plan_endpoint,
)
from timeback.services.powerpath.endpoints.sync_course_lesson_plans import (
    sync_course_lesson_plans as sync_course_lesson_plans_endpoint,
)
from timeback.services.powerpath.endpoints.get_course_progress import (
    get_course_progress as get_course_progress_endpoint,
)
from timeback.services.powerpath.endpoints.get_lesson_plan import (
    get_lesson_plan as get_lesson_plan_endpoint,
)
from timeback.services.powerpath.endpoints.get_lesson_plan_structure import (
    get_lesson_plan_structure as get_lesson_plan_structure_endpoint,
)
from timeback.services.powerpath.endpoints.update_student_item_response import (
    update_student_item_response as update_student_item_response_endpoint,
)
from timeback.services.powerpath.endpoints.get_course_syllabus import (
    get_course_syllabus as get_course_syllabus_endpoint,
)
from timeback.services.powerpath.endpoints.create_new_attempt import (
    create_new_attempt as create_new_attempt_endpoint,
)
from timeback.services.powerpath.endpoints.final_student_assessment_response import (
    final_student_assessment_response as final_student_assessment_response_endpoint,
)
from timeback.services.powerpath.endpoints.get_assessment_progress import (
    get_assessment_progress as get_assessment_progress_endpoint,
)
from timeback.services.powerpath.endpoints.get_attempts import (
    get_attempts as get_attempts_endpoint,
)
from timeback.services.powerpath.endpoints.get_next_question import (
    get_next_question as get_next_question_endpoint,
)
from timeback.services.powerpath.endpoints.reset_attempt import (
    reset_attempt as reset_attempt_endpoint,
)
from timeback.services.powerpath.endpoints.update_student_question_response import (
    update_student_question_response as update_student_question_response_endpoint,
)


class PowerPathService:
    """PowerPath service methods.

    This service handles all PowerPath API interactions including placement testing,
    screening, lesson plans, and adaptive assessments.

    Usage:
        client = Timeback()
        # Placement
        tests = client.powerpath.get_all_placement_tests(request)
        level = client.powerpath.get_current_level(request)
        
        # Lesson Plans
        plan = client.powerpath.get_lesson_plan(request)
        progress = client.powerpath.get_course_progress(request)
        
        # Assessments
        attempt = client.powerpath.create_new_attempt(request)
        question = client.powerpath.get_next_question(request)
    """

    def __init__(self, http: HttpClient):
        """Initialize PowerPathService with an HTTP client.

        Args:
            http: The HttpClient instance configured for the API base URL.
                  PowerPath uses the same base URL as OneRoster (api.alpha-1edtech.ai).
        """
        self._http = http

    # ==========================================================================
    # PLACEMENT ENDPOINTS
    # ==========================================================================
    # Endpoints for managing placement tests and tracking student progress.
    # Base path: /powerpath/placement/...
    # ==========================================================================

    def get_all_placement_tests(
        self, request: TimebackGetAllPlacementTestsRequest
    ) -> TimebackGetAllPlacementTestsResponse:
        """Get all placement tests for a student and subject.

        Returns all placement tests for a subject, including available results for each.
        A 'Lesson' (placement test) in this context is a ComponentResource object which
        has a Resource object with metadata.lessonType = "placement" associated with it.

        Args:
            request: Request containing student sourcedId and subject

        Returns:
            TimebackGetAllPlacementTestsResponse containing list of placement tests
        """
        return get_all_placement_tests_endpoint(self._http, request)

    def get_current_level(
        self, request: TimebackGetCurrentLevelRequest
    ) -> TimebackGetCurrentLevelResponse:
        """Get the current level of a student in a placement process.

        Returns the current level determined by the last completed placement test's
        grade level, starting from the lowest grade level available for the subject.
        As the student completes placement tests and attains scores >= 90, their 
        level updates to the next level available for the subject.

        Also returns the 'onboarded' boolean indicating if the student completed
        the onboarding process for the subject.

        Args:
            request: Request containing student sourcedId and subject

        Returns:
            TimebackGetCurrentLevelResponse containing gradeLevel, onboarded status,
            and availableTests count
        """
        return get_current_level_endpoint(self._http, request)

    def get_next_placement_test(
        self, request: TimebackGetNextPlacementTestRequest
    ) -> TimebackGetNextPlacementTestResponse:
        """Get the next placement test for a student in a subject.

        Returns the next placement test the student should take:
        - If the student has completed all tests, lesson will be null and exhaustedTests = true.
        - If the student hasn't started, returns the first placement test.
        - If the student scored < 90 on last test, returns null (onboarded = true).
        - If the student scored >= 90, returns the next available test.

        Args:
            request: Request containing student sourcedId and subject

        Returns:
            TimebackGetNextPlacementTestResponse containing next test info, 
            onboarded status, exhaustedTests flag, and availableTests count
        """
        return get_next_placement_test_endpoint(self._http, request)

    def get_subject_progress(
        self, request: TimebackGetSubjectProgressRequest
    ) -> TimebackGetSubjectProgressResponse:
        """Get the progress a student has made in a subject.

        Returns progress information for each course in the subject, including:
        - Enrollment status
        - Completed lessons count
        - Total lessons count
        - XP earned and attainable
        - Test-out usage

        Args:
            request: Request containing student sourcedId and subject

        Returns:
            TimebackGetSubjectProgressResponse containing progress for each course
        """
        return get_subject_progress_endpoint(self._http, request)

    def reset_user_placement(
        self, request: TimebackResetUserPlacementRequest
    ) -> TimebackResetUserPlacementResponse:
        """Reset user placement progress for a subject.

        Resets a user's placement progress for a specific subject by:
        - Soft deleting all placement assessment results for that subject
        - Resetting user onboarding state to "in_progress"

        This operation is restricted to administrators only and cannot be undone.

        Args:
            request: Request containing student sourcedId and subject

        Returns:
            TimebackResetUserPlacementResponse with success status, deleted count, and reset flag
        """
        return reset_user_placement_endpoint(self._http, request)

    def get_student_placement_data(self, student_id: str) -> StudentPlacementDataResponse:
        """Get comprehensive placement data for a student.

        Returns placement data for all subjects including:
        - Starting and current grade levels
        - RIT scores (GROWTH and SCREENING)
        - Test results with status and scores
        - Next test ID for each subject

        Args:
            student_id: The sourcedId of the student

        Returns:
            Dictionary with subject names as keys and TimebackSubjectPlacementData as values.
            Subjects include: Reading, Language, Vocabulary, Social Studies, Writing, 
            Science, FastMath, Math
        """
        return get_student_placement_data_endpoint(self._http, student_id)

    # ==========================================================================
    # SCREENING ENDPOINTS
    # ==========================================================================
    # Endpoints for managing screening tests and sessions.
    # Base path: /powerpath/screening/...
    # ==========================================================================

    def get_screening_results(self, user_id: str) -> TimebackGetScreeningResultsResponse:
        """Get screening test results for a user.

        Returns screening results across all subjects. Each subject maps to either
        a result object containing grade, ritScore, testName, and completedAt, 
        or null if no screening test has been completed for that subject.

        Args:
            user_id: The sourcedId of the user to get screening results for

        Returns:
            TimebackGetScreeningResultsResponse - a dict mapping subject names to 
            screening results (or null)
        """
        return get_screening_results_endpoint(self._http, user_id)

    def get_screening_session(self, user_id: str) -> TimebackScreeningSession:
        """Get the screening session for a user.

        Returns session information including NWEA credentials, session status,
        and assignment details needed to start or continue a screening test.

        Args:
            user_id: The sourcedId of the user to get the session for

        Returns:
            TimebackScreeningSession containing credentials, status, and assignment info
        """
        return get_screening_session_endpoint(self._http, user_id)

    def assign_screening_test(
        self, request: TimebackAssignScreeningTestRequest
    ) -> TimebackScreeningSession:
        """Assign a screening test to a user.

        Assigns a screening test for a specific subject to a user. Returns the
        updated screening session with assignment details.

        Args:
            request: Request containing userId and subject (Math, Reading, Language, or Science)

        Returns:
            TimebackScreeningSession containing updated session with assignment info
        """
        return assign_screening_test_endpoint(self._http, request)

    def reset_screening_session(self, user_id: str) -> None:
        """Reset screening session for a user.

        Resets the screening session allowing the user to restart screening tests.

        Args:
            user_id: The sourcedId of the user whose session to reset

        Returns:
            None (HTTP 204 - no content)
        """
        return reset_screening_session_endpoint(self._http, user_id)

    # ==========================================================================
    # EXTERNAL TEST ENDPOINTS
    # ==========================================================================
    # Endpoints for managing external tests and test assignments.
    # Base path: /powerpath/...
    # ==========================================================================

    def create_external_placement_test(
        self, request: TimebackCreateExternalPlacementTestRequest
    ) -> TimebackCreateExternalTestResponse:
        """Create an external placement test for a course.

        Creates or updates a ComponentResource to act as a Placement Test lesson in a course.
        This allows integrating with external test-taking platforms (like Edulastic).

        The endpoint creates or updates:
        - A CourseComponent for the course to hold the Placement Test lesson
        - A Resource with lessonType = "placement" and the external service details
        - A ComponentResource acting as the Placement Test lesson

        Args:
            request: Request containing courseId, toolProvider, grades, and optional metadata

        Returns:
            TimebackCreateExternalTestResponse containing lessonId, courseComponentId, resourceId
        """
        return create_external_placement_test_endpoint(self._http, request)

    def create_external_test_out(
        self, request: TimebackCreateExternalTestOutRequest
    ) -> TimebackCreateExternalTestResponse:
        """Create an external test-out lesson for a course.

        **DEPRECATED**: This endpoint is deprecated. Use start_test_out() instead.
        
        Migration flow:
        1. Check availability: get_course_progress(courseId, studentId)
        2. Start test-out: start_test_out(courseId, studentId)
        3. Launch test: make_external_test_assignment(...)

        Creates or updates a ComponentResource to act as a TestOut lesson.

        Args:
            request: Request containing courseId, toolProvider, grades, xp, and optional metadata

        Returns:
            TimebackCreateExternalTestResponse containing lessonId, courseComponentId, resourceId
        """
        return create_external_test_out_endpoint(self._http, request)

    def create_internal_test(
        self,
        request: Union[TimebackCreateInternalQtiTestRequest, TimebackCreateInternalAssessmentBankTestRequest],
    ) -> TimebackCreateInternalTestResponse:
        """Create an internal test lesson for a course.

        Supports two test types:
        - QTI (testType="qti"): Creates a single QTI resource
        - Assessment Bank (testType="assessment-bank"): Creates multiple QTI resources in a bank

        For test-out and placement lessons, this updates existing tests of the same type.
        For other lesson types (quiz, unit-test, pp-100), it creates new lessons.

        Args:
            request: Request containing courseId, lessonType, testType, and QTI/assessment-bank config

        Returns:
            TimebackCreateInternalTestResponse containing lessonId, courseComponentId, resourceId
        """
        return create_internal_test_endpoint(self._http, request)

    def import_external_test_assignment_results(
        self, request: TimebackImportExternalTestAssignmentResultsRequest
    ) -> TimebackImportExternalTestAssignmentResultsResponse:
        """Import results from an external test assignment.

        Retrieves and stores the results of an external test assignment.
        Applies to 'test-out', 'placement', and 'unit-test' lessons.

        The behavior varies by tool provider:
        - For "edulastic": Imports results when all questions answered and grade is "GRADED"
        - For "mastery-track": Imports results when scoreStatus is "fully graded"

        May trigger automatic course enrollment if the lesson is a placement test or test-out.

        Args:
            request: Request containing student sourcedId, lesson sourcedId, and optional applicationName

        Returns:
            TimebackImportExternalTestAssignmentResultsResponse with finalized status, credentials, etc.
        """
        return import_external_test_assignment_results_endpoint(self._http, request)

    def make_external_test_assignment(
        self, request: TimebackMakeExternalTestAssignmentRequest
    ) -> TimebackMakeExternalTestAssignmentResponse:
        """Make an external test assignment for a student.

        Assigns an external test to a student and returns credentials and URLs
        needed to take the test. Applies to 'test-out', 'placement', and 'unit-test' lessons.

        The behavior varies by tool provider:
        - For "edulastic": Authenticates student, assigns test, returns credentials and IDs
        - For "mastery-track": Authenticates student, assigns test, waits for result write-back

        Args:
            request: Request containing student, lesson, and optional test configuration

        Returns:
            TimebackMakeExternalTestAssignmentResponse with credentials, test URL, and IDs
        """
        return make_external_test_assignment_endpoint(self._http, request)

    def get_test_out(
        self, request: TimebackGetTestOutRequest
    ) -> TimebackGetTestOutResponse:
        """Get test-out information for a student and course.

        **DEPRECATED**: This endpoint is deprecated. Use get_course_progress() instead.
        The response includes a `testOut` field with comprehensive status information.

        Returns the testOut lesson reference and status for a student and course.

        Args:
            request: Request containing student and course sourcedIds

        Returns:
            TimebackGetTestOutResponse with lesson info, finalized status, and credentials
        """
        return get_test_out_endpoint(self._http, request)

    # ==========================================================================
    # LESSON PLAN ENDPOINTS
    # ==========================================================================
    # Endpoints for managing lesson plans, operations, and course progress.
    # Base path: /powerpath/lessonPlans/...
    # ==========================================================================

    def create_lesson_plan(
        self, request: TimebackCreateLessonPlanRequest
    ) -> TimebackCreateLessonPlanResponse:
        """Create a new lesson plan for a course and student.

        If a lesson plan already exists for the course/student, returns the
        existing lesson plan ID.

        Args:
            request: Request containing courseId, userId, and optional classId

        Returns:
            TimebackCreateLessonPlanResponse containing the lesson plan ID
        """
        return create_lesson_plan_endpoint(self._http, request)

    def start_test_out(
        self, request: TimebackStartTestOutRequest
    ) -> TimebackStartTestOutResponse:
        """Start a test-out assignment for a student.

        Creates an on-demand test-out assignment. After calling this, use
        make_external_test_assignment to start the test with the provider.

        Eligibility requirements:
        - Course must have a supported subject+grade combination
        - Student must be actively enrolled in a course with that subject+grade
        - Student must not have a completed or failed test-out

        Args:
            request: Request containing courseId and studentId

        Returns:
            TimebackStartTestOutResponse with assignmentId, lessonId, resourceId, status
        """
        return start_test_out_endpoint(self._http, request)

    def get_tree(self, request: TimebackGetTreeRequest) -> LessonPlan:
        """Get the lesson plan tree for a course and student.

        Returns the complete lesson plan tree including all components,
        resources, and nested structure.

        Args:
            request: Request containing courseId and userId

        Returns:
            LessonPlan object with the complete tree structure
        """
        return get_tree_endpoint(self._http, request)

    def delete_lesson_plans_by_course_id(self, course_id: str) -> None:
        """Delete all lesson plans for a course.

        This is a destructive operation that removes all lesson plans
        associated with the specified course.

        Args:
            course_id: The sourcedId of the course

        Returns:
            None (HTTP 204 - no content)
        """
        return delete_lesson_plans_by_course_id_endpoint(self._http, course_id)

    def store_operation(
        self, request: TimebackStoreOperationRequest
    ) -> TimebackStoreOperationResponse:
        """Store an operation on a lesson plan.

        Available operation types:
        - set-skipped: Show/hide content for the student
        - move-item-before/after: Reorder content
        - move-item-to-start/end: Move to beginning/end
        - add-custom-resource: Add additional resources
        - change-item-parent: Move to different sections

        Args:
            request: Request containing lessonPlanId, operation, and optional reason

        Returns:
            TimebackStoreOperationResponse with success status and operationId
        """
        return store_operation_endpoint(self._http, request)

    def get_operations(self, lesson_plan_id: str) -> TimebackGetOperationsResponse:
        """Get all operations for a lesson plan.

        Returns operations in chronological order for audit trails,
        history tracking, and debugging.

        Args:
            lesson_plan_id: The ID of the lesson plan

        Returns:
            TimebackGetOperationsResponse containing list of operations
        """
        return get_operations_endpoint(self._http, lesson_plan_id)

    def sync_operations(self, lesson_plan_id: str) -> TimebackSyncOperationsResponse:
        """Sync pending operations for a lesson plan.

        Applies operations that haven't been applied yet to update
        the lesson plan structure.

        Args:
            lesson_plan_id: The ID of the lesson plan

        Returns:
            TimebackSyncOperationsResponse with success status and operation results
        """
        return sync_operations_endpoint(self._http, lesson_plan_id)

    def recreate_lesson_plan(self, lesson_plan_id: str) -> TimebackSyncOperationsResponse:
        """Recreate a lesson plan from scratch.

        Use when a lesson plan becomes corrupted or out of sync.
        Deletes all items, rebuilds from course structure, and applies
        all operations from the log.

        Args:
            lesson_plan_id: The ID of the lesson plan

        Returns:
            TimebackSyncOperationsResponse with success status and operation results
        """
        return recreate_lesson_plan_endpoint(self._http, lesson_plan_id)

    def sync_course_lesson_plans(
        self, course_id: str
    ) -> TimebackSyncCourseLessonPlansResponse:
        """Sync all lesson plans for a course.

        Use after making structural changes to a base course to ensure
        all students have the latest content. Maintains personalizations.

        Args:
            course_id: The sourcedId of the course

        Returns:
            TimebackSyncCourseLessonPlansResponse with list of affected lesson plan IDs
        """
        return sync_course_lesson_plans_endpoint(self._http, course_id)

    def get_course_progress(
        self,
        course_id: str,
        student_id: str,
        lesson_id: Optional[str] = None,
    ) -> TimebackCourseProgressResponse:
        """Get course progress for a student.

        Returns assessment line items for the course and student,
        including test-out status.

        Args:
            course_id: The sourcedId of the course
            student_id: The sourcedId of the student
            lesson_id: Optional component resource ID to filter by lesson

        Returns:
            TimebackCourseProgressResponse with lineItems and testOut status
        """
        return get_course_progress_endpoint(
            self._http, course_id, student_id, lesson_id
        )

    def get_lesson_plan(self, lesson_plan_id: str) -> LessonPlan:
        """Get complete lesson plan tree by ID.

        Returns the lesson plan in syllabus-like format with only
        non-skipped items (visible content) and all metadata.

        Args:
            lesson_plan_id: The ID of the lesson plan

        Returns:
            LessonPlan object with complete tree structure
        """
        return get_lesson_plan_endpoint(self._http, lesson_plan_id)

    def get_lesson_plan_structure(
        self, lesson_plan_id: str
    ) -> TimebackLessonPlanStructureResponse:
        """Get simplified lesson plan structure for debugging.

        Returns a lightweight view showing both skipped and non-skipped
        items with order information and IDs.

        Args:
            lesson_plan_id: The ID of the lesson plan

        Returns:
            TimebackLessonPlanStructureResponse with structure tree
        """
        return get_lesson_plan_structure_endpoint(self._http, lesson_plan_id)

    def update_student_item_response(
        self, request: TimebackUpdateStudentItemResponseRequest
    ) -> TimebackUpdateStudentItemResponseResponse:
        """Update student item response for a component or resource.

        Updates the student's response with score information, status,
        and optional learning objective results.

        Args:
            request: Request with studentId, componentResourceId, and result

        Returns:
            TimebackUpdateStudentItemResponseResponse with line item and result
        """
        return update_student_item_response_endpoint(self._http, request)

    # ==========================================================================
    # SYLLABUS ENDPOINTS
    # ==========================================================================
    # Endpoints for retrieving course syllabus information.
    # Base path: /powerpath/syllabus/...
    # ==========================================================================

    def get_course_syllabus(
        self, course_sourced_id: str
    ) -> TimebackSyllabusResponse:
        """Get the syllabus for a course.

        Args:
            course_sourced_id: The sourcedId of the course

        Returns:
            TimebackSyllabusResponse with syllabus content
        """
        return get_course_syllabus_endpoint(self._http, course_sourced_id)

    # ==========================================================================
    # ASSESSMENT ENDPOINTS
    # ==========================================================================
    # Endpoints for adaptive assessment flow (attempts, questions, responses).
    # Base path: /powerpath/...
    # ==========================================================================

    def create_new_attempt(
        self, request: TimebackCreateNewAttemptRequest
    ) -> TimebackCreateNewAttemptResponse:
        """Create a new attempt for a student in a lesson.

        Creates a new attempt if the current attempt is completed.
        For Assessment Bank lessons, this updates the state to serve
        a different sub-test using round-robin logic.

        Args:
            request: Request with student and lesson IDs

        Returns:
            TimebackCreateNewAttemptResponse with attempt data
        """
        return create_new_attempt_endpoint(self._http, request)

    def final_student_assessment_response(
        self, request: TimebackFinalStudentAssessmentRequest
    ) -> TimebackFinalStudentAssessmentResponse:
        """Finalize a test assessment.

        Finalizes a lesson of type quiz, test-out, or placement.
        Evaluates responses and creates/updates assessment records.

        Args:
            request: Request with student and lesson IDs

        Returns:
            TimebackFinalStudentAssessmentResponse with finalization status
        """
        return final_student_assessment_response_endpoint(self._http, request)

    def get_assessment_progress(
        self,
        student: str,
        lesson: str,
        attempt: Optional[int] = None,
    ) -> TimebackAssessmentProgressResponse:
        """Get assessment progress for a student in a lesson.

        Returns progress including scores, questions, and metrics.

        Args:
            student: The sourcedId of the student
            lesson: The sourcedId of the lesson (ComponentResource)
            attempt: Optional attempt number

        Returns:
            TimebackAssessmentProgressResponse with progress data
        """
        return get_assessment_progress_endpoint(self._http, student, lesson, attempt)

    def get_attempts(self, student: str, lesson: str) -> TimebackGetAttemptsResponse:
        """Get all attempts for a student in a lesson.

        For Assessment Bank lessons, each attempt may represent a different
        sub-test of the bank.

        Args:
            student: The sourcedId of the student
            lesson: The sourcedId of the lesson (ComponentResource)

        Returns:
            TimebackGetAttemptsResponse with list of all attempts
        """
        return get_attempts_endpoint(self._http, student, lesson)

    def get_next_question(
        self, student: str, lesson: str
    ) -> TimebackNextQuestionResponse:
        """Get the next question for a student in a PowerPath-100 lesson.

        Note: This endpoint only works with lessons of type 'powerpath-100'.

        Args:
            student: The sourcedId of the student
            lesson: The sourcedId of the lesson (ComponentResource)

        Returns:
            TimebackNextQuestionResponse with score and next question
        """
        return get_next_question_endpoint(self._http, student, lesson)

    def reset_attempt(
        self, request: TimebackResetAttemptRequest
    ) -> TimebackResetAttemptResponse:
        """Reset a student's attempt for a lesson.

        Resets the attempt by:
        - Soft-deleting previous question responses
        - Resetting test score to 0
        - Updating scoreStatus to "not submitted"

        For external tests, only resets the score to 0.
        For Assessment Bank lessons, keeps user in same bank test.

        Args:
            request: Request with student and lesson IDs

        Returns:
            TimebackResetAttemptResponse with success status and score
        """
        return reset_attempt_endpoint(self._http, request)

    def update_student_question_response(
        self, request: TimebackUpdateStudentQuestionResponseRequest
    ) -> TimebackUpdateStudentQuestionResponseResponse:
        """Update a student's response to a question.

        Checks correctness using QTI response declarations and updates
        the score accordingly. Creates/updates AssessmentLineItem and
        AssessmentResult objects.

        Args:
            request: Request with student, question, lesson, and response(s)

        Returns:
            TimebackUpdateStudentQuestionResponseResponse with updated scores
        """
        return update_student_question_response_endpoint(self._http, request)

    # TODO: Implement test-assignments endpoints

