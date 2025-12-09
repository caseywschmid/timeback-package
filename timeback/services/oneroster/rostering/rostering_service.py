from typing import Any, Dict, Optional
from timeback.http import HttpClient
from timeback.models.response import (
    TimebackGetAllUsersResponse,
    TimebackUpdateUserResponse,
    TimebackGetUserResponse,
    TimebackRegisterStudentCredentialsResponse,
    TimebackDecryptCredentialResponse,
    TimebackGetAllSchoolsResponse,
    TimebackCreateSchoolResponse,
    TimebackGetSchoolResponse,
    TimebackUpdateSchoolResponse,
    TimebackGetAllClassesResponse,
    TimebackCreateClassResponse,
    TimebackGetClassResponse,
    TimebackUpdateClassResponse,
)
from timeback.models.request import (
    TimebackUpdateUserRequest,
    TimebackCreateUserRequest,
    TimebackAddAgentRequest,
    TimebackDeleteAgentRequest,
    TimebackGetUserRequest,
    TimebackGetAllUsersRequest,
    TimebackGetAllSchoolsRequest,
    TimebackCreateSchoolRequest,
    TimebackGetSchoolRequest,
    TimebackUpdateSchoolRequest,
    TimebackRegisterStudentCredentialsRequest,
    TimebackDecryptCredentialRequest,
    TimebackGetAllClassesRequest,
    TimebackCreateClassRequest,
    TimebackGetClassRequest,
    TimebackUpdateClassRequest,
    TimebackGetClassesForSchoolRequest,
    TimebackGetClassesForUserRequest,
    TimebackGetTermsForSchoolRequest,
    TimebackGetAllTermsRequest,
    TimebackGetTermRequest,
    TimebackGetClassesForTermRequest,
    TimebackGetTeachersForClassRequest,
    TimebackAddTeacherToClassRequest,
    TimebackGetTeachersForClassInSchoolRequest,
    TimebackGetTeachersForSchoolRequest,
    TimebackGetAllTeachersRequest,
    TimebackGetTeacherRequest,
    TimebackGetClassesForTeacherRequest,
    TimebackGetStudentsForClassRequest,
    TimebackAddStudentToClassRequest,
    TimebackGetStudentsForClassInSchoolRequest,
    TimebackGetStudentsForSchoolRequest,
    TimebackGetAllStudentsRequest,
    TimebackGetStudentRequest,
    TimebackGetClassesForStudentRequest,
    TimebackGetAllOrgsRequest,
    TimebackCreateOrgRequest,
    TimebackGetOrgRequest,
    TimebackUpdateOrgRequest,
    TimebackGetAllGradingPeriodsRequest,
    TimebackCreateGradingPeriodRequest,
    TimebackGetGradingPeriodRequest,
    TimebackUpdateGradingPeriodRequest,
    TimebackGetGradingPeriodsForTermRequest,
    TimebackCreateGradingPeriodForTermRequest,
    TimebackGetAllEnrollmentsRequest,
    TimebackCreateEnrollmentRequest,
    TimebackGetEnrollmentRequest,
    TimebackUpdateEnrollmentRequest,
    TimebackPatchEnrollmentRequest,
    TimebackGetEnrollmentsForClassInSchoolRequest,
    TimebackGetEnrollmentsForSchoolRequest,
    TimebackGetAllDemographicsRequest,
    TimebackCreateDemographicRequest,
    TimebackGetDemographicRequest,
    TimebackUpdateDemographicRequest,
    TimebackGetAllCoursesRequest,
    TimebackCreateCourseRequest,
    TimebackGetCourseRequest,
    TimebackUpdateCourseRequest,
    TimebackGetClassesForCourseRequest,
    TimebackGetAllComponentResourcesRequest,
    TimebackCreateComponentResourceRequest,
    TimebackGetComponentResourceRequest,
    TimebackUpdateComponentResourceRequest,
)
from timeback.models.response import TimebackCreateUserResponse
from timeback.services.oneroster.rostering.endpoints.get_user import (
    get_user as get_user_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_user_with_demographics import (
    get_user_with_demographics as get_user_with_demographics_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_all_users import (
    get_all_users as get_all_users_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_all_schools import (
    get_all_schools as get_all_schools_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_all_classes import (
    get_all_classes as get_all_classes_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.create_class import (
    create_class as create_class_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_class import (
    get_class as get_class_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.update_class import (
    update_class as update_class_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.delete_class import (
    delete_class as delete_class_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_classes_for_school import (
    get_classes_for_school as get_classes_for_school_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.create_school import (
    create_school as create_school_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_school import (
    get_school as get_school_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.update_school import (
    update_school as update_school_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.delete_school import (
    delete_school as delete_school_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.update_user import (
    update_user as update_user_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.create_user import (
    create_user as create_user_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.delete_user import (
    delete_user as delete_user_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.delete_agent import (
    delete_agent as delete_agent_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_agent_for import (
    get_agent_for as get_agent_for_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_agents import (
    get_agents as get_agents_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.add_agent import (
    add_agent as add_agent_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.register_student_credentials import (
    register_student_credentials as register_student_credentials_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.decrypt_credential import (
    decrypt_credential as decrypt_credential_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_classes_for_user import (
    get_classes_for_user as get_classes_for_user_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_terms_for_school import (
    get_terms_for_school as get_terms_for_school_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_all_terms import (
    get_all_terms as get_all_terms_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_term import (
    get_term as get_term_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_classes_for_term import (
    get_classes_for_term as get_classes_for_term_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_teachers_for_class import (
    get_teachers_for_class as get_teachers_for_class_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.add_teacher_to_class import (
    add_teacher_to_class as add_teacher_to_class_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_teachers_for_class_in_school import (
    get_teachers_for_class_in_school as get_teachers_for_class_in_school_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_teachers_for_school import (
    get_teachers_for_school as get_teachers_for_school_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_all_teachers import (
    get_all_teachers as get_all_teachers_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_teacher import (
    get_teacher as get_teacher_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_classes_for_teacher import (
    get_classes_for_teacher as get_classes_for_teacher_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_students_for_class import (
    get_students_for_class as get_students_for_class_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.add_student_to_class import (
    add_student_to_class as add_student_to_class_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_students_for_class_in_school import (
    get_students_for_class_in_school as get_students_for_class_in_school_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_students_for_school import (
    get_students_for_school as get_students_for_school_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_all_students import (
    get_all_students as get_all_students_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_student import (
    get_student as get_student_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_classes_for_student import (
    get_classes_for_student as get_classes_for_student_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_all_orgs import (
    get_all_orgs as get_all_orgs_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.create_org import (
    create_org as create_org_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_org import (
    get_org as get_org_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.update_org import (
    update_org as update_org_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.delete_org import (
    delete_org as delete_org_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_all_grading_periods import (
    get_all_grading_periods as get_all_grading_periods_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.create_grading_period import (
    create_grading_period as create_grading_period_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_grading_period import (
    get_grading_period as get_grading_period_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.update_grading_period import (
    update_grading_period as update_grading_period_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.delete_grading_period import (
    delete_grading_period as delete_grading_period_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_grading_periods_for_term import (
    get_grading_periods_for_term as get_grading_periods_for_term_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.create_grading_period_for_term import (
    create_grading_period_for_term as create_grading_period_for_term_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_all_enrollments import (
    get_all_enrollments as get_all_enrollments_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.create_enrollment import (
    create_enrollment as create_enrollment_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_enrollment import (
    get_enrollment as get_enrollment_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.update_enrollment import (
    update_enrollment as update_enrollment_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.patch_enrollment import (
    patch_enrollment as patch_enrollment_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.delete_enrollment import (
    delete_enrollment as delete_enrollment_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_enrollments_for_class_in_school import (
    get_enrollments_for_class_in_school as get_enrollments_for_class_in_school_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_enrollments_for_school import (
    get_enrollments_for_school as get_enrollments_for_school_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_all_demographics import (
    get_all_demographics as get_all_demographics_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.create_demographic import (
    create_demographic as create_demographic_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_demographic import (
    get_demographic as get_demographic_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.update_demographic import (
    update_demographic as update_demographic_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.delete_demographic import (
    delete_demographic as delete_demographic_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_all_courses import (
    get_all_courses as get_all_courses_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.create_course import (
    create_course as create_course_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_course import (
    get_course as get_course_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.update_course import (
    update_course as update_course_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.delete_course import (
    delete_course as delete_course_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_classes_for_course import (
    get_classes_for_course as get_classes_for_course_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_all_component_resources import (
    get_all_component_resources as get_all_component_resources_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.create_component_resource import (
    create_component_resource as create_component_resource_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_component_resource import (
    get_component_resource as get_component_resource_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.update_component_resource import (
    update_component_resource as update_component_resource_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.delete_component_resource import (
    delete_component_resource as delete_component_resource_endpoint,
)
from timeback.models.response import TimebackGetAgentForResponse
from timeback.models.response import TimebackGetAllComponentResourcesResponse
from timeback.models.response import TimebackCreateComponentResourceResponse
from timeback.models.response import TimebackGetComponentResourceResponse
from timeback.models.response import TimebackUpdateComponentResourceResponse
from timeback.models.response import TimebackGetAllCoursesResponse
from timeback.models.response import TimebackCreateCourseResponse
from timeback.models.response import TimebackGetCourseResponse
from timeback.models.response import TimebackUpdateCourseResponse
from timeback.models.response import TimebackGetAllDemographicsResponse
from timeback.models.response import TimebackCreateDemographicResponse
from timeback.models.response import TimebackGetDemographicResponse
from timeback.models.response import TimebackUpdateDemographicResponse
from timeback.models.response import TimebackGetAllEnrollmentsResponse
from timeback.models.response import TimebackCreateEnrollmentResponse
from timeback.models.response import TimebackGetEnrollmentResponse
from timeback.models.response import TimebackUpdateEnrollmentResponse
from timeback.models.response import TimebackCreateGradingPeriodResponse
from timeback.models.response import TimebackUpdateGradingPeriodResponse
from timeback.models.response import TimebackGetAgentsResponse
from timeback.models.response import TimebackGetAllTermsResponse
from timeback.models.response import TimebackGetTermResponse
from timeback.models.response import TimebackAddTeacherToClassResponse
from timeback.models.response import TimebackAddStudentToClassResponse
from timeback.models.response import TimebackGetAllOrgsResponse
from timeback.models.response import TimebackGetOrgResponse
from timeback.models.response import TimebackCreateOrgResponse
from timeback.models.response import TimebackUpdateOrgResponse


class RosteringService:
    """Rostering service methods for OneRoster."""

    def __init__(self, http: HttpClient):
        self._http = http

    def get_user(self, request: TimebackGetUserRequest) -> TimebackGetUserResponse:
        """Fetch a single user by sourcedId."""
        return get_user_endpoint(self._http, request)

    def get_user_with_demographics(self, request: TimebackGetUserRequest) -> TimebackGetUserResponse:
        """Get a specific user with demographics by sourcedId."""
        return get_user_with_demographics_endpoint(self._http, request)

    def get_all_users(
        self,
        request: TimebackGetAllUsersRequest,
    ) -> TimebackGetAllUsersResponse:
        """Fetch a paginated list of users."""
        return get_all_users_endpoint(self._http, request)

    def get_all_schools(
        self,
        request: TimebackGetAllSchoolsRequest,
    ) -> TimebackGetAllSchoolsResponse:
        """Fetch a paginated list of schools."""
        return get_all_schools_endpoint(self._http, request)

    def get_all_classes(
        self,
        request: TimebackGetAllClassesRequest,
    ) -> TimebackGetAllClassesResponse:
        """Fetch a paginated list of classes."""
        return get_all_classes_endpoint(self._http, request)

    def create_class(
        self,
        request: TimebackCreateClassRequest,
    ) -> TimebackCreateClassResponse:
        """Create a new class."""
        return create_class_endpoint(self._http, request)

    def get_class(self, request: TimebackGetClassRequest) -> TimebackGetClassResponse:
        """Fetch a single class by sourcedId."""
        return get_class_endpoint(self._http, request)

    def update_class(
        self, request: TimebackUpdateClassRequest
    ) -> TimebackUpdateClassResponse:
        """Update an existing class by sourcedId."""
        return update_class_endpoint(self._http, request)

    def delete_class(self, sourced_id: str):
        """Delete (tombstone) a class by sourcedId. Returns raw provider response (None for 204)."""
        return delete_class_endpoint(self._http, sourced_id)

    def get_classes_for_school(
        self, request: TimebackGetClassesForSchoolRequest
    ) -> TimebackGetAllClassesResponse:
        """Fetch a paginated list of classes for a specific school."""
        return get_classes_for_school_endpoint(self._http, request)

    def create_school(
        self,
        request: TimebackCreateSchoolRequest,
    ) -> TimebackCreateSchoolResponse:
        """Create a new school."""
        return create_school_endpoint(self._http, request)

    def get_school(self, request: TimebackGetSchoolRequest) -> TimebackGetSchoolResponse:
        """Fetch a single school by sourcedId."""
        return get_school_endpoint(self._http, request)

    def update_school(
        self, request: TimebackUpdateSchoolRequest
    ) -> TimebackUpdateSchoolResponse:
        """Update an existing school by sourcedId."""
        return update_school_endpoint(self._http, request)

    def delete_school(self, sourced_id: str):
        """Delete (tombstone) a school by sourcedId. Returns raw provider response (None for 204)."""
        return delete_school_endpoint(self._http, sourced_id)

    def update_user(
        self, request: TimebackUpdateUserRequest
    ) -> Optional[TimebackUpdateUserResponse]:
        """Update an existing user by sourcedId. Returns None if server returned no content."""
        return update_user_endpoint(self._http, request)

    def create_user(self, request: TimebackCreateUserRequest) -> TimebackCreateUserResponse:
        """Create a new user."""
        return create_user_endpoint(self._http, request)

    def delete_user(self, sourced_id: str):
        """Delete (tombstone) a user by sourcedId. Returns raw provider response (None for 204)."""
        return delete_user_endpoint(self._http, sourced_id)

    def delete_agent(self, request: TimebackDeleteAgentRequest) -> Optional[Dict[str, Any]]:
        """Delete an agent for a user. Returns raw provider response (None for no-content)."""
        return delete_agent_endpoint(self._http, request)

    def get_agent_for(self, user_id: str) -> TimebackGetAgentForResponse:
        """Get users this user is an agent for (e.g., parents getting children list)."""
        return get_agent_for_endpoint(self._http, user_id)

    def get_agents(self, user_id: str) -> TimebackGetAgentsResponse:
        """Get agent users for the specified user."""
        return get_agents_endpoint(self._http, user_id)

    def add_agent(self, request: TimebackAddAgentRequest) -> Dict[str, Any]:
        """Add an agent for a user. Returns raw provider response."""
        return add_agent_endpoint(self._http, request)

    def register_student_credentials(
        self, request: TimebackRegisterStudentCredentialsRequest
    ) -> TimebackRegisterStudentCredentialsResponse:
        """Register student credentials for third-party applications."""
        return register_student_credentials_endpoint(self._http, request)

    def decrypt_credential(
        self, request: TimebackDecryptCredentialRequest
    ) -> TimebackDecryptCredentialResponse:
        """Decrypt and return the password for a specific user credential."""
        return decrypt_credential_endpoint(self._http, request)

    def get_classes_for_user(
        self, request: TimebackGetClassesForUserRequest
    ) -> TimebackGetAllClassesResponse:
        """Fetch classes for a specific user."""
        return get_classes_for_user_endpoint(self._http, request)

    def get_terms_for_school(
        self, request: TimebackGetTermsForSchoolRequest
    ) -> TimebackGetAllTermsResponse:
        """Fetch terms for a specific school."""
        return get_terms_for_school_endpoint(self._http, request)

    def get_all_terms(
        self, request: TimebackGetAllTermsRequest
    ) -> TimebackGetAllTermsResponse:
        """Fetch all terms (paginated list)."""
        return get_all_terms_endpoint(self._http, request)

    def get_term(
        self, request: TimebackGetTermRequest
    ) -> TimebackGetTermResponse:
        """Fetch a single term by sourcedId."""
        return get_term_endpoint(self._http, request)

    def get_classes_for_term(
        self, request: TimebackGetClassesForTermRequest
    ) -> TimebackGetAllClassesResponse:
        """Fetch classes for a specific term."""
        return get_classes_for_term_endpoint(self._http, request)

    def get_teachers_for_class(
        self, request: TimebackGetTeachersForClassRequest
    ) -> TimebackGetAllUsersResponse:
        """Fetch teachers for a specific class."""
        return get_teachers_for_class_endpoint(self._http, request)

    def add_teacher_to_class(
        self, request: TimebackAddTeacherToClassRequest
    ) -> TimebackAddTeacherToClassResponse:
        """Add a teacher to a class."""
        return add_teacher_to_class_endpoint(self._http, request)

    def get_teachers_for_class_in_school(
        self, request: TimebackGetTeachersForClassInSchoolRequest
    ) -> TimebackGetAllUsersResponse:
        """Fetch teachers for a class in a specific school."""
        return get_teachers_for_class_in_school_endpoint(self._http, request)

    def get_teachers_for_school(
        self, request: TimebackGetTeachersForSchoolRequest
    ) -> TimebackGetAllUsersResponse:
        """Fetch teachers for a specific school."""
        return get_teachers_for_school_endpoint(self._http, request)

    def get_all_teachers(
        self, request: TimebackGetAllTeachersRequest
    ) -> TimebackGetAllUsersResponse:
        """Fetch all teachers (paginated list)."""
        return get_all_teachers_endpoint(self._http, request)

    def get_teacher(
        self, request: TimebackGetTeacherRequest
    ) -> TimebackGetUserResponse:
        """Fetch a single teacher by sourcedId."""
        return get_teacher_endpoint(self._http, request)

    def get_classes_for_teacher(
        self, request: TimebackGetClassesForTeacherRequest
    ) -> TimebackGetAllClassesResponse:
        """Fetch classes for a specific teacher."""
        return get_classes_for_teacher_endpoint(self._http, request)

    def get_students_for_class(
        self, request: TimebackGetStudentsForClassRequest
    ) -> TimebackGetAllUsersResponse:
        """Fetch students for a specific class."""
        return get_students_for_class_endpoint(self._http, request)

    def add_student_to_class(
        self, request: TimebackAddStudentToClassRequest
    ) -> TimebackAddStudentToClassResponse:
        """Add a student to a class."""
        return add_student_to_class_endpoint(self._http, request)

    def get_students_for_class_in_school(
        self, request: TimebackGetStudentsForClassInSchoolRequest
    ) -> TimebackGetAllUsersResponse:
        """Fetch students for a class in a specific school."""
        return get_students_for_class_in_school_endpoint(self._http, request)

    def get_students_for_school(
        self, request: TimebackGetStudentsForSchoolRequest
    ) -> TimebackGetAllUsersResponse:
        """Fetch students for a specific school."""
        return get_students_for_school_endpoint(self._http, request)

    def get_all_students(
        self, request: TimebackGetAllStudentsRequest
    ) -> TimebackGetAllUsersResponse:
        """Fetch all students (paginated list)."""
        return get_all_students_endpoint(self._http, request)

    def get_student(
        self, request: TimebackGetStudentRequest
    ) -> TimebackGetUserResponse:
        """Fetch a single student by sourcedId."""
        return get_student_endpoint(self._http, request)

    def get_classes_for_student(
        self, request: TimebackGetClassesForStudentRequest
    ) -> TimebackGetAllClassesResponse:
        """Fetch classes for a specific student."""
        return get_classes_for_student_endpoint(self._http, request)

    def get_all_orgs(
        self, request: TimebackGetAllOrgsRequest
    ) -> TimebackGetAllOrgsResponse:
        """Fetch all orgs (paginated list)."""
        return get_all_orgs_endpoint(self._http, request)

    def create_org(
        self, request: TimebackCreateOrgRequest
    ) -> TimebackCreateOrgResponse:
        """Create a new org."""
        return create_org_endpoint(self._http, request)

    def get_org(
        self, request: TimebackGetOrgRequest
    ) -> TimebackGetOrgResponse:
        """Fetch a single org by sourcedId."""
        return get_org_endpoint(self._http, request)

    def update_org(
        self, request: TimebackUpdateOrgRequest
    ) -> TimebackUpdateOrgResponse:
        """Update an existing org."""
        return update_org_endpoint(self._http, request)

    def delete_org(self, sourced_id: str) -> Optional[Dict[str, Any]]:
        """Delete (tombstone) an org by sourcedId."""
        return delete_org_endpoint(self._http, sourced_id)

    def get_all_grading_periods(
        self, request: TimebackGetAllGradingPeriodsRequest
    ) -> TimebackGetAllTermsResponse:
        """Fetch all grading periods (paginated list)."""
        return get_all_grading_periods_endpoint(self._http, request)

    def create_grading_period(
        self, request: TimebackCreateGradingPeriodRequest
    ) -> TimebackCreateGradingPeriodResponse:
        """Create a new grading period."""
        return create_grading_period_endpoint(self._http, request)

    def get_grading_period(
        self, request: TimebackGetGradingPeriodRequest
    ) -> TimebackGetTermResponse:
        """Fetch a single grading period by sourcedId."""
        return get_grading_period_endpoint(self._http, request)

    def update_grading_period(
        self, request: TimebackUpdateGradingPeriodRequest
    ) -> TimebackUpdateGradingPeriodResponse:
        """Update an existing grading period."""
        return update_grading_period_endpoint(self._http, request)

    def delete_grading_period(self, sourced_id: str) -> Optional[Dict[str, Any]]:
        """Delete (tombstone) a grading period by sourcedId."""
        return delete_grading_period_endpoint(self._http, sourced_id)

    def get_grading_periods_for_term(
        self, request: TimebackGetGradingPeriodsForTermRequest
    ) -> TimebackGetAllTermsResponse:
        """Fetch grading periods for a specific term."""
        return get_grading_periods_for_term_endpoint(self._http, request)

    def create_grading_period_for_term(
        self, request: TimebackCreateGradingPeriodForTermRequest
    ) -> TimebackCreateGradingPeriodResponse:
        """Create a grading period for a specific term."""
        return create_grading_period_for_term_endpoint(self._http, request)

    # -------------------------------------------------------------------------
    # Enrollment Endpoints
    # -------------------------------------------------------------------------

    def get_all_enrollments(
        self, request: TimebackGetAllEnrollmentsRequest
    ) -> TimebackGetAllEnrollmentsResponse:
        """Fetch all enrollments (paginated list)."""
        return get_all_enrollments_endpoint(self._http, request)

    def create_enrollment(
        self, request: TimebackCreateEnrollmentRequest
    ) -> TimebackCreateEnrollmentResponse:
        """Create a new enrollment."""
        return create_enrollment_endpoint(self._http, request)

    def get_enrollment(
        self, request: TimebackGetEnrollmentRequest
    ) -> TimebackGetEnrollmentResponse:
        """Fetch a single enrollment by sourcedId."""
        return get_enrollment_endpoint(self._http, request)

    def update_enrollment(
        self, request: TimebackUpdateEnrollmentRequest
    ) -> TimebackUpdateEnrollmentResponse:
        """Update an existing enrollment (PUT)."""
        return update_enrollment_endpoint(self._http, request)

    def patch_enrollment(
        self, request: TimebackPatchEnrollmentRequest
    ) -> TimebackUpdateEnrollmentResponse:
        """Partially update an existing enrollment (PATCH) with metadata merging."""
        return patch_enrollment_endpoint(self._http, request)

    def delete_enrollment(self, sourced_id: str) -> Optional[Dict[str, Any]]:
        """Delete (tombstone) an enrollment by sourcedId."""
        return delete_enrollment_endpoint(self._http, sourced_id)

    def get_enrollments_for_class_in_school(
        self, request: TimebackGetEnrollmentsForClassInSchoolRequest
    ) -> TimebackGetAllEnrollmentsResponse:
        """Fetch enrollments for a specific class in a school."""
        return get_enrollments_for_class_in_school_endpoint(self._http, request)

    def get_enrollments_for_school(
        self, request: TimebackGetEnrollmentsForSchoolRequest
    ) -> TimebackGetAllEnrollmentsResponse:
        """Fetch enrollments for a specific school."""
        return get_enrollments_for_school_endpoint(self._http, request)

    # -------------------------------------------------------------------------
    # Demographics Endpoints
    # -------------------------------------------------------------------------

    def get_all_demographics(
        self, request: TimebackGetAllDemographicsRequest
    ) -> TimebackGetAllDemographicsResponse:
        """Fetch all demographics (paginated list)."""
        return get_all_demographics_endpoint(self._http, request)

    def create_demographic(
        self, request: TimebackCreateDemographicRequest
    ) -> TimebackCreateDemographicResponse:
        """Create a new demographic."""
        return create_demographic_endpoint(self._http, request)

    def get_demographic(
        self, request: TimebackGetDemographicRequest
    ) -> TimebackGetDemographicResponse:
        """Fetch a single demographic by sourcedId."""
        return get_demographic_endpoint(self._http, request)

    def update_demographic(
        self, request: TimebackUpdateDemographicRequest
    ) -> TimebackUpdateDemographicResponse:
        """Update an existing demographic."""
        return update_demographic_endpoint(self._http, request)

    def delete_demographic(self, sourced_id: str) -> Optional[Dict[str, Any]]:
        """Delete (tombstone) a demographic by sourcedId."""
        return delete_demographic_endpoint(self._http, sourced_id)

    # -------------------------------------------------------------------------
    # Course Endpoints
    # -------------------------------------------------------------------------

    def get_all_courses(
        self, request: TimebackGetAllCoursesRequest
    ) -> TimebackGetAllCoursesResponse:
        """Fetch all courses (paginated list)."""
        return get_all_courses_endpoint(self._http, request)

    def create_course(
        self, request: TimebackCreateCourseRequest
    ) -> TimebackCreateCourseResponse:
        """Create a new course."""
        return create_course_endpoint(self._http, request)

    def get_course(
        self, request: TimebackGetCourseRequest
    ) -> TimebackGetCourseResponse:
        """Fetch a single course by sourcedId."""
        return get_course_endpoint(self._http, request)

    def update_course(
        self, request: TimebackUpdateCourseRequest
    ) -> TimebackUpdateCourseResponse:
        """Update an existing course."""
        return update_course_endpoint(self._http, request)

    def delete_course(self, sourced_id: str) -> Optional[Dict[str, Any]]:
        """Delete (tombstone) a course by sourcedId."""
        return delete_course_endpoint(self._http, sourced_id)

    def get_classes_for_course(
        self, request: TimebackGetClassesForCourseRequest
    ) -> TimebackGetAllClassesResponse:
        """Fetch classes for a specific course."""
        return get_classes_for_course_endpoint(self._http, request)

    # -------------------------------------------------------------------------
    # Component Resource Endpoints
    # -------------------------------------------------------------------------

    def get_all_component_resources(
        self, request: TimebackGetAllComponentResourcesRequest
    ) -> TimebackGetAllComponentResourcesResponse:
        """Fetch all component resources (paginated list)."""
        return get_all_component_resources_endpoint(self._http, request)

    def create_component_resource(
        self, request: TimebackCreateComponentResourceRequest
    ) -> TimebackCreateComponentResourceResponse:
        """Create a new component resource."""
        return create_component_resource_endpoint(self._http, request)

    def get_component_resource(
        self, request: TimebackGetComponentResourceRequest
    ) -> TimebackGetComponentResourceResponse:
        """Fetch a single component resource by sourcedId."""
        return get_component_resource_endpoint(self._http, request)

    def update_component_resource(
        self, request: TimebackUpdateComponentResourceRequest
    ) -> TimebackUpdateComponentResourceResponse:
        """Update an existing component resource."""
        return update_component_resource_endpoint(self._http, request)

    def delete_component_resource(self, sourced_id: str) -> Optional[Dict[str, Any]]:
        """Delete (tombstone) a component resource by sourcedId."""
        return delete_component_resource_endpoint(self._http, sourced_id)


