# TODO

## OneRoster

### /ims/oneroster/gradebook/v1p2/scoreScales/

- [ ] `get_all_score_scales`
- [ ] `create_score_scale`

### /ims/oneroster/gradebook/v1p2/scoreScales/{sourcedId}

- [ ] `get_score_scale`
- [ ] `put_score_scale`
- [ ] `delete_score_scale`

### /ims/oneroster/gradebook/v1p2/schools/{sourcedId}/scoreScales

- [ ] `get_score_scales_for_school`

### /ims/oneroster/rostering/v1p2/schools/

- [ ] `get_all_schools`
- [ ] `create_school`

### /ims/oneroster/rostering/v1p2/schools/{sourcedId}

- [ ] `get_school`
- [ ] `update_school`
- [ ] `delete_school`

### /ims/oneroster/gradebook/v1p2/results/

- [ ] `get_all_results`
- [ ] `create_result`

### /ims/oneroster/gradebook/v1p2/results/{sourcedId}

- [ ] `get_result`
- [ ] `put_result`
- [ ] `delete_result`

### /ims/oneroster/gradebook/v1p2/lineItems/

- [ ] `get_all_line_items`
- [ ] `create_line_item`

### /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}

- [ ] `get_line_item`
- [ ] `put_line_item`
- [ ] `delete_line_item`

### /ims/oneroster/gradebook/v1p2/lineItems/{sourcedId}/results

- [ ] `create_result_for_line_item`

### /ims/oneroster/gradebook/v1p2/schools/{sourcedId}/lineItems

- [ ] `get_line_items_for_school`
- [ ] `create_line_items_for_school`

### /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/academicSessions/{academicSessionSourcedId}/results

- [ ] `post_results_for_academic_session_for_class`

### /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/lineItems

- [ ] `post_line_items_for_class`

### /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/lineItems/{lineItemSourcedId}/results

- [ ] `get_results_for_line_item_for_class`

### /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/students/{studentSourcedId}/results

- [ ] `get_results_for_student_for_class`

### /ims/oneroster/gradebook/v1p2/classes/{sourcedId}/categories

- [ ] `get_categories_for_class`

### /ims/oneroster/gradebook/v1p2/classes/{sourcedId}/lineItems

- [ ] `get_line_items_for_class`

### /ims/oneroster/gradebook/v1p2/classes/{sourcedId}/results

- [ ] `get_results_for_class`

### /ims/oneroster/gradebook/v1p2/classes/{sourcedId}/scoreScales

- [ ] `get_score_scales_for_class`

### /ims/oneroster/rostering/v1p2/classes/

- [ ] `get_all_classes`
- [ ] `create_class`

### /ims/oneroster/rostering/v1p2/classes/{sourcedId}

- [ ] `get_class`
- [ ] `update_class`
- [ ] `delete_class`

### /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/classes

- [ ] `get_classes_for_school`

### /ims/oneroster/gradebook/v1p2/categories/

- [ ] `get_all_categories`
- [ ] `create_category`

### /ims/oneroster/gradebook/v1p2/categories/{sourcedId}

- [ ] `get_category`
- [ ] `put_category`
- [ ] `delete_category`

### /ims/oneroster/gradebook/v1p2/assessmentResults/

- [ ] `get_all_assessment_results`
- [ ] `create_assessment_result`

### /ims/oneroster/gradebook/v1p2/assessmentResults/{sourcedId}

- [ ] `get_assessment_result`
- [ ] `put_assessment_result`
- [ ] `delete_assessment_result`

### /ims/oneroster/gradebook/v1p2/assessmentLineItems/

- [ ] `get_all_assessment_line_items`
- [ ] `create_assessment_line_item`

### /ims/oneroster/gradebook/v1p2/assessmentLineItems/{sourcedId}

- [ ] `get_assessment_line_item`
- [ ] `put_assessment_line_item`
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

- [ ] `get_user_with_demographics`

### /ims/oneroster/rostering/v1p2/users/{userId}/credentials

- [ ] `register_student_credentials`

### /ims/oneroster/rostering/v1p2/users/{userId}/credentials/{credentialId}/decrypt

- [ ] `decrypt_credential`

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

### /ims/oneroster/rostering/v1p2/schools/{schoolSourcedId}/courses

- [ ] `get_courses_for_school`

### /ims/oneroster/rostering/v1p2/academicSessions/

- [ ] `get_all_academic_sessions`
- [ ] `post_academic_session`

### /ims/oneroster/rostering/v1p2/academicSessions/{sourcedId}

- [ ] `get_academic_session`
- [ ] `put_academic_session`
- [ ] `delete_academic_session`
