# TODO

## OneRoster

### /ims/oneroster/gradebook/v1p2/scoreScales/

- [x] `get_all_score_scales`
- [x] `create_score_scale`

### /ims/oneroster/gradebook/v1p2/scoreScales/{sourcedId}

- [x] `get_score_scale`
- [x] `put_score_scale`
- [x] `delete_score_scale`

### /ims/oneroster/gradebook/v1p2/schools/{sourcedId}/scoreScales

- [x] `get_score_scales_for_school`

### /ims/oneroster/rostering/v1p2/schools/

- [x] `get_all_schools`
- [x] `create_school`

### /ims/oneroster/rostering/v1p2/schools/{sourcedId}

- [x] `get_school`
- [x] `update_school`
- [x] `delete_school`

### /ims/oneroster/gradebook/v1p2/results/

- [x] `get_all_results`
- [x] `create_result`

### /ims/oneroster/gradebook/v1p2/results/{sourcedId}

- [x] `get_result`
- [x] `put_result`
- [x] `delete_result`

### /ims/oneroster/gradebook/v1p2/lineItems/

- [x] `get_all_line_items`
- [x] `create_line_item`

### /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}

- [x] `get_line_item`
- [x] `put_line_item`
- [x] `delete_line_item`

### /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}/results

- [x] `create_result_for_line_item`

### /ims/oneroster/gradebook/v1p2/schools/{sourcedId}/lineItems

- [x] `get_line_items_for_school`
- [x] `create_line_items_for_school`

### /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/academicSessions/{academicSessionSourcedId}/results

- [x] `post_results_for_academic_session_for_class`

### /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/lineItems

- [x] `post_line_items_for_class`

### /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/lineItems/{lineItemSourcedId}/results

- [x] `get_results_for_line_item_for_class`

### /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/students/{studentSourcedId}/results

- [x] `get_results_for_student_for_class`

### /ims/oneroster/gradebook/v1p2/classes/{sourcedId}/categories

- [x] `get_categories_for_class`

### /ims/oneroster/gradebook/v1p2/classes/{sourcedId}/lineItems

- [x] `get_line_items_for_class`

### /ims/oneroster/gradebook/v1p2/classes/{sourcedId}/results

- [x] `get_results_for_class`

### /ims/oneroster/gradebook/v1p2/classes/{sourcedId}/scoreScales

- [x] `get_score_scales_for_class`

### /ims/oneroster/rostering/v1p2/classes/

- [x] `get_all_classes`
- [x] `create_class`

### /ims/oneroster/rostering/v1p2/classes/{sourcedId}

- [x] `get_class`
- [x] `update_class`
- [x] `delete_class`

### /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes

- [x] `get_classes_for_school`

### /ims/oneroster/gradebook/v1p2/categories/

- [x] `get_all_categories`
- [x] `create_category`

### /ims/oneroster/gradebook/v1p2/categories/{sourcedId}

- [x] `get_category`
- [x] `put_category`
- [ ] `delete_category`

### /ims/oneroster/gradebook/v1p2/assessmentResults/

- [ ] `get_all_assessment_results`
- [ ] `create_assessment_result`

### /ims/oneroster/gradebook/v1p2/assessmentResults/{sourcedId}

- [ ] `get_assessment_result`
- [ ] `put_assessment_result`
- [ ] `patch_assessment_result`
- [ ] `delete_assessment_result`

### /ims/oneroster/gradebook/v1p2/assessmentLineItems/

- [ ] `get_all_assessment_line_items`
- [ ] `create_assessment_line_item`

### /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}

- [ ] `get_assessment_line_item`
- [ ] `put_assessment_line_item`
- [ ] `patch_assessment_line_item`
- [ ] `delete_assessment_line_item`

### /ims/oneroster/resources/v1p2/resources/

- [ ] `get_all_resources`
- [ ] `create_resource`

### /ims/oneroster/resources/v1p2/resources/{sourcedId}

- [ ] `get_resource`
- [ ] `update_resource`
- [ ] `delete_resource`

### /ims/oneroster/resources/v1p2/resources/classes/{classSourcedId}/resources

- [ ] `get_resources_for_class`

### /ims/oneroster/resources/v1p2/resources/courses/{courseSourcedId}/resources

- [ ] `get_resources_for_course`

### /ims/oneroster/resources/v1p2/resources/export/{sourceId}

- [ ] `export_resource_to_common_cartridge`

### /ims/oneroster/resources/v1p2/resources/users/{userSourcedId}/resources

- [ ] `get_resources_for_user`

### /ims/oneroster/rostering/v1p2/users/

- [x] `get_all_users`
- [x] `create_user`

### /ims/oneroster/rostering/v1p2/users/{sourcedId}

- [x] `get_user`
- [x] `update_user`
- [x] `delete_user`

### /ims/oneroster/rostering/v1p2/users/{sourcedId}/demographics

- [x] `get_user_with_demographics`

### /ims/oneroster/rostering/v1p2/users/{userId}/agentFor

- [x] `get_agent_for`

### /ims/oneroster/rostering/v1p2/users/{userId}/agents

- [x] `get_agents`
- [x] `add_agent`

### /ims/oneroster/rostering/v1p2/users/{sourcedId}/agents/{agentSourcedId}

- [x] `delete_agent`

### /ims/oneroster/rostering/v1p2/users/{userId}/credentials

- [x] `register_student_credentials`

### /ims/oneroster/rostering/v1p2/users/{userId}/credentials/{credentialId}/decrypt

- [x] `decrypt_credential`

### /ims/oneroster/rostering/v1p2/users/{userSourcedId}/classes

- [ ] `get_classes_for_user`

### /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/terms

- [ ] `get_terms_for_school`

### /ims/oneroster/rostering/v1p2/terms/

- [ ] `get_all_terms`

### /ims/oneroster/rostering/v1p2/terms/{sourcedId}

- [ ] `get_term`

### /ims/oneroster/rostering/v1p2/terms/{termSourcedId}/classes

- [ ] `get_classes_for_term`

### /ims/oneroster/rostering/v1p2/classes/{classSourcedId}/teachers

- [ ] `get_teachers_for_class`
- [ ] `add_teacher_to_class`

### /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes/{classSourcedId}/teachers

- [ ] `get_teachers_for_class_in_school`

### /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/teachers

- [ ] `get_teachers_for_school`

### /ims/oneroster/rostering/v1p2/teachers/

- [ ] `get_all_teachers`

### /ims/oneroster/rostering/v1p2/teachers/{sourcedId}

- [ ] `get_teacher`

### /ims/oneroster/rostering/v1p2/teachers/{teacherSourcedId}/classes

- [ ] `get_classes_for_teacher`

### /ims/oneroster/rostering/v1p2/classes/{classSourcedId}/students

- [ ] `get_students_for_class`
- [ ] `add_student_to_class`

### /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes/{classSourcedId}/students

- [ ] `get_students_for_class_in_school`

### /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/students

- [ ] `get_students_for_school`

### /ims/oneroster/rostering/v1p2/students/

- [ ] `get_all_students`

### /ims/oneroster/rostering/v1p2/students/{sourcedId}

- [ ] `get_student`

### /ims/oneroster/rostering/v1p2/students/{studentSourcedId}/classes

- [ ] `get_classes_for_student`

### /ims/oneroster/rostering/v1p2/orgs/

- [ ] `get_all_orgs`
- [ ] `create_org`

### /ims/oneroster/rostering/v1p2/orgs/{sourcedId}

- [ ] `get_org`
- [ ] `update_org`
- [ ] `delete_org`

### /ims/oneroster/rostering/v1p2/gradingPeriods/

- [ ] `get_all_grading_periods`
- [ ] `create_grading_period`

### /ims/oneroster/rostering/v1p2/gradingPeriods/{sourcedId}

- [ ] `get_grading_period`
- [ ] `update_grading_period`
- [ ] `delete_grading_period`

### /ims/oneroster/rostering/v1p2/terms/{termSourcedId}/gradingPeriods

- [ ] `get_grading_periods_for_term`
- [ ] `create_grading_period_for_term`

### /ims/oneroster/rostering/v1p2/enrollments/

- [ ] `get_all_enrollments`
- [ ] `create_enrollment`

### /ims/oneroster/rostering/v1p2/enrollments/{sourcedId}

- [ ] `get_enrollment`
- [ ] `update_enrollment`
- [ ] `partially_update_enrollment`
- [ ] `delete_enrollment`

### /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes/{classSourcedId}/enrollments

- [ ] `get_enrollments_for_class_in_school`

### /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/enrollments

- [ ] `get_enrollments_for_school`

### /ims/oneroster/rostering/v1p2/demographics/

- [ ] `get_all_demographics`
- [ ] `post_demographics`

### /ims/oneroster/rostering/v1p2/demographics/{sourcedId}

- [ ] `get_demographics`
- [ ] `put_demographics`
- [ ] `delete_demographics`

### /ims/oneroster/rostering/v1p2/courses/

- [ ] `get_all_courses`
- [ ] `create_course`

### /ims/oneroster/rostering/v1p2/courses/{courseSourcedId}/classes

- [ ] `get_classes_for_course`

### /ims/oneroster/rostering/v1p2/courses/{sourcedId}

- [ ] `get_course`
- [ ] `put_course`
- [ ] `delete_course`

### /ims/oneroster/rostering/v1p2/courses/component-resources

- [ ] `get_all_component_resources`
- [ ] `create_component_resource`

### /ims/oneroster/rostering/v1p2/courses/component-resources/{sourcedId}

- [ ] `get_component_resource`
- [ ] `put_component_resource`
- [ ] `delete_component_resource`

### /ims/oneroster/rostering/v1p2/courses/components

- [ ] `get_all_course_components`
- [ ] `create_course_component`

### /ims/oneroster/rostering/v1p2/courses/components/{sourcedId}

- [ ] `get_course_component`
- [ ] `put_course_component`
- [ ] `delete_course_component`

### /ims/oneroster/rostering/v1p2/courses/structure

- [ ] `create_course_structure`

### /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/courses

- [ ] `get_courses_for_school`

### /ims/oneroster/rostering/v1p2/academicSessions/

- [ ] `get_all_academic_sessions`
- [ ] `post_academic_session`

### /ims/oneroster/rostering/v1p2/academicSessions/{sourcedId}

- [ ] `get_academic_session`
- [ ] `put_academic_session`
- [ ] `delete_academic_session`

## PowerPath

### /powerpath/placement/getAllPlacementTests:

- [ ] `get_all_placement_tests`

### /powerpath/placement/getCurrentLevel:

- [ ] `get_current_level`

### /powerpath/placement/getNextPlacementTest:

- [ ] `get_next_placement_test`

### /powerpath/placement/getSubjectProgress:

- [ ] `get_subject_progress`

### /powerpath/screening/results/{userId}:

- [ ] `get_results`

### /powerpath/screening/session/{userId}:

- [ ] `get_session`

### /powerpath/screening/tests/assign:

- [ ] `assign_test`

### /powerpath/createExternalPlacementTest:

- [ ] `create_external_placement_test`

### /powerpath/createExternalTestOut:

- [ ] `create_external_test_out`

### /powerpath/createInternalTest:

- [ ] `create_internal_test`

### /powerpath/importExternalTestAssignmentResults:

- [ ] `import_external_test_assignment_results`

### /powerpath/makeExternalTestAssignment:

- [ ] `make_external_test_assignment`

### /powerpath/testOut:

- [ ] `test_out`

### /powerpath/lessonPlans/:

- [ ] `create_lesson_plan`

### /powerpath/lessonPlans/{courseId}/{userId}:

- [ ] `get_tree`

### /powerpath/lessonPlans/{courseId}/deleteAll:

- [ ] `delete_lesson_plans_by_course_id`

### /powerpath/lessonPlans/{lessonPlanId}/operations:

- [ ] `store_operation`
- [ ] `get_operations`

### /powerpath/lessonPlans/{lessonPlanId}/operations/sync:

- [ ] `sync_operations`

### /powerpath/lessonPlans/{lessonPlanId}/recreate:

- [ ] `recreate_lesson_plan`

### /powerpath/lessonPlans/course/{courseId}/sync:

- [ ] `sync_course_lesson_plans`

### /powerpath/lessonPlans/getCourseProgress/{courseId}/student/{studentId}:

- [ ] `get_course_progress`

### /powerpath/lessonPlans/tree/{lessonPlanId}:

- [ ] `get_lesson_plan`

### /powerpath/lessonPlans/tree/{lessonPlanId}/structure:

- [ ] `get_lesson_plan_structure`

### /powerpath/lessonPlans/updateStudentItemResponse:

- [ ] `update_student_item_response`

### /powerpath/syllabus/{courseSourcedId}:

- [ ] `get_course_syllabus`

### /powerpath/createNewAttempt:

- [ ] `create_new_attempt`

### /powerpath/finalStudentAssessmentResponse:

- [ ] `final_student_assessment_response`

### /powerpath/getAssessmentProgress:

- [ ] `get_assessment_progress`

### /powerpath/getAttempts:

- [ ] `get_attempts`

### /powerpath/getNextQuestion:

- [ ] `get_next_question`

### /powerpath/resetAttempt:

- [ ] `reset_attempt`

### /powerpath/updateStudentQuestionResponse:

- [ ] `update_student_question_response`

## QTI API - All Endpoints

### /stimuli:

- [ ] `search_stimuli`
- [ ] `create_stimulus`

### /stimuli/{identifier}:

- [ ] `get_stimulus`
- [ ] `update_stimulus`
- [ ] `delete_stimulus`

### /assessment-items:

- [ ] `search_assessment_items`
- [ ] `create_assessment_item`

### /assessment-items/{identifier}:

- [ ] `get_assessment_item`
- [ ] `update_assessment_item`
- [ ] `delete_assessment_item`

### /assessment-items/metadata:

- [ ] `update_metadata`

### /assessment-items/{identifier}/process-response:

- [ ] `process_response`

### /assessment-tests:

- [ ] `search_assessment_tests`
- [ ] `create_assessment_test`

### /assessment-tests/{identifier}:

- [ ] `get_assessment_test`
- [ ] `update_assessment_test`
- [ ] `delete_assessment_test`

### /assessment-tests/{identifier}/questions:

- [ ] `get_all_questions`

### /assessment-tests/{identifier}/metadata:

- [ ] `update_assessment_test_metadata`

### /assessment-tests/{assessmentTestIdentifier}/test-parts:

- [ ] `search_test_parts`
- [ ] `create_test_part`

### /assessment-tests/{assessmentTestIdentifier}/test-parts/{identifier}:

- [ ] `get_test_part`
- [ ] `update_test_part`
- [ ] `delete_test_part`

### /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections:

- [ ] `search_sections`
- [ ] `create_section`

### /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections/{identifier}:

- [ ] `get_section`
- [ ] `update_section`
- [ ] `delete_section`

### /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections/{identifier}/items:

- [ ] `add_assessment_item`

### /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections/{identifier}/items/{itemIdentifier}:

- [ ] `remove_assessment_item`

### /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections/{identifier}/items/order:

- [ ] `update_assessment_item_order`

### /question:

- [ ] `create_question_feedback`

### /lesson:

- [ ] `create_lesson_feedback`

### /lesson/{lessonId}:

- [ ] `get_feedback_by_lesson_id`

### /{id}:

- [ ] `delete_feedback`

### /validate:

- [ ] `validate_xml`

### /validate/batch:

- [ ] `validate_batch`

## Caliper Events API - All Endpoints

### /caliper/event:

- [ ] `create_caliper_event`

### /caliper/event/validate:

- [ ] `validate_caliper_event`

### /caliper/events:

- [ ] `list_caliper_events`

## CASE API

### /ims/case/v1p1/CFAssociations/{sourcedId}

- [ ] `get_cf_association`

### /ims/case/v1p1/CFDocuments

- [ ] `get_all_cf_documents`

### /ims/case/v1p1/CFDocuments/{sourcedId}

- [ ] `get_cf_document`

### /ims/case/v1p1/CFItems

- [ ] `get_all_cf_items`

### /ims/case/v1p1/CFItems/{sourcedId}

- [ ] `get_cf_item`

### /ims/case/v1p1/CFPackages

- [ ] `upload_cf_package`

### /ims/case/v1p1/CFPackages/{sourcedId}

- [ ] `get_cf_package`

### /ims/case/v1p1/CFPackages/{sourcedId}/groups

- [ ] `get_cf_package_with_groups`
