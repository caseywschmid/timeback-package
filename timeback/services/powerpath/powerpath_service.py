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
from timeback.models.request import (
    TimebackGetAllPlacementTestsRequest,
    TimebackGetCurrentLevelRequest,
    TimebackGetNextPlacementTestRequest,
    TimebackGetSubjectProgressRequest,
    TimebackAssignScreeningTestRequest,
    TimebackCreateExternalPlacementTestRequest,
)
from timeback.models.response import (
    TimebackGetAllPlacementTestsResponse,
    TimebackGetCurrentLevelResponse,
    TimebackGetNextPlacementTestResponse,
    TimebackGetSubjectProgressResponse,
    TimebackGetScreeningResultsResponse,
    TimebackCreateExternalTestResponse,
)
from timeback.models import TimebackScreeningSession
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

    # ==========================================================================
    # EXTERNAL TEST ENDPOINTS
    # ==========================================================================
    # Endpoints for managing external tests and test assignments.
    # Base path: /powerpath/...
    #
    # TODO: Implement the following endpoints:
    # - create_external_test_out: POST /powerpath/createExternalTestOut
    # - create_internal_test: POST /powerpath/createInternalTest
    # - import_external_test_assignment_results: POST /powerpath/importExternalTestAssignmentResults
    # - make_external_test_assignment: POST /powerpath/makeExternalTestAssignment
    # - test_out: POST /powerpath/testOut
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

    # ==========================================================================
    # LESSON PLAN ENDPOINTS
    # ==========================================================================
    # Endpoints for managing lesson plans, operations, and course progress.
    # Base path: /powerpath/lessonPlans/...
    #
    # TODO: Implement the following endpoints:
    # - create_lesson_plan: POST /powerpath/lessonPlans/
    # - get_tree: GET /powerpath/lessonPlans/{courseId}/{userId}
    # - delete_lesson_plans_by_course_id: DELETE /powerpath/lessonPlans/{courseId}/deleteAll
    # - store_operation: POST /powerpath/lessonPlans/{lessonPlanId}/operations
    # - get_operations: GET /powerpath/lessonPlans/{lessonPlanId}/operations
    # - sync_operations: POST /powerpath/lessonPlans/{lessonPlanId}/operations/sync
    # - recreate_lesson_plan: POST /powerpath/lessonPlans/{lessonPlanId}/recreate
    # - sync_course_lesson_plans: POST /powerpath/lessonPlans/course/{courseId}/sync
    # - get_course_progress: GET /powerpath/lessonPlans/getCourseProgress/{courseId}/student/{studentId}
    # - get_lesson_plan: GET /powerpath/lessonPlans/tree/{lessonPlanId}
    # - get_lesson_plan_structure: GET /powerpath/lessonPlans/tree/{lessonPlanId}/structure
    # - update_student_item_response: POST /powerpath/lessonPlans/updateStudentItemResponse
    # ==========================================================================

    # ==========================================================================
    # SYLLABUS ENDPOINTS
    # ==========================================================================
    # Endpoints for retrieving course syllabus information.
    # Base path: /powerpath/syllabus/...
    #
    # TODO: Implement the following endpoints:
    # - get_course_syllabus: GET /powerpath/syllabus/{courseSourcedId}
    # ==========================================================================

    # ==========================================================================
    # ASSESSMENT ENDPOINTS
    # ==========================================================================
    # Endpoints for adaptive assessment flow (attempts, questions, responses).
    # Base path: /powerpath/...
    #
    # TODO: Implement the following endpoints:
    # - create_new_attempt: POST /powerpath/createNewAttempt
    # - final_student_assessment_response: POST /powerpath/finalStudentAssessmentResponse
    # - get_assessment_progress: GET /powerpath/getAssessmentProgress
    # - get_attempts: GET /powerpath/getAttempts
    # - get_next_question: GET /powerpath/getNextQuestion
    # - reset_attempt: POST /powerpath/resetAttempt
    # - update_student_question_response: POST /powerpath/updateStudentQuestionResponse
    # ==========================================================================

