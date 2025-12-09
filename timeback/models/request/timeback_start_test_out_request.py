"""Request model for starting a test-out assignment.

POST /powerpath/lessonPlans/startTestOut
"""

from pydantic import BaseModel, ConfigDict, Field


class TimebackStartTestOutRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """Request model for starting a test-out assignment for a student.
    
    Creates an on-demand test-out assignment for a student in a course.
    This endpoint validates eligibility and creates an unlisted test assignment.
    
    After calling this endpoint, call make_external_test_assignment to start
    the test with the provider (Edulastic or MasteryTrack).
    
    Attributes:
        Required:
            - course_id (str): The sourcedId of the course
            - student_id (str): The sourcedId of the student
    """

    course_id: str = Field(..., alias="courseId", description="The sourcedId of the course")
    student_id: str = Field(..., alias="studentId", description="The sourcedId of the student")

