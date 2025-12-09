"""Subject Progress model for the PowerPath API.

This module defines models for the subject progress response from the PowerPath API.
"""

from typing import Optional, List
from pydantic import BaseModel, Field


class TimebackSubjectProgressCourse(BaseModel):
    """Course information within subject progress.
    
    Attributes:
        - sourcedId (str): Unique identifier for the course
        - title (str): Title of the course
        - courseCode (str, optional): Course code identifier
        - level (str, optional): The level of the course
        - grades (List[str], optional): List of grade levels for the course
        - subjects (List[str], optional): List of subjects covered by the course
        - status (str): Status of the course
        - orgSourcedId (str): The organization's sourcedId
        - dateLastModified (str): Last modification timestamp
    """

    sourcedId: str = Field(..., description="Unique identifier for the course")
    title: str = Field(..., description="Title of the course")
    courseCode: Optional[str] = Field(None, description="Course code identifier")
    level: Optional[str] = Field(None, description="The level of the course")
    grades: Optional[List[str]] = Field(None, description="List of grade levels for the course")
    subjects: Optional[List[str]] = Field(None, description="List of subjects covered by the course")
    status: str = Field(..., description="Status of the course")
    orgSourcedId: str = Field(..., description="The organization's sourcedId")
    dateLastModified: str = Field(..., description="Last modification timestamp")


class TimebackSubjectProgressItem(BaseModel):
    """Progress information for a single course within a subject.
    
    Attributes:
        - course (TimebackSubjectProgressCourse): Course information
        - inEnrolled (bool): Whether the student is enrolled in the course
        - hasUsedTestOut (bool): Whether the student has a fully graded assessment 
          result for a test-out lesson in the course
        - testOutLessonId (str, optional): The sourcedId of the test-out lesson 
          (ComponentResource) in the course
        - completedLessons (int): Number of lessons with 'fully graded' assessment results
        - totalLessons (int): Total number of lessons in the course
        - totalAttainableXp (int): Total XP that can be earned, not considering multipliers
        - totalXpEarned (int): Total XP earned considering calculated multipliers
    """

    course: TimebackSubjectProgressCourse = Field(..., description="Course information")
    inEnrolled: bool = Field(..., description="Whether the student is enrolled in the course")
    hasUsedTestOut: bool = Field(
        ..., description="Whether the student has a fully graded test-out result"
    )
    testOutLessonId: Optional[str] = Field(
        None, description="The sourcedId of the test-out lesson (ComponentResource)"
    )
    completedLessons: int = Field(
        ..., description="Number of lessons with 'fully graded' assessment results"
    )
    totalLessons: int = Field(..., description="Total number of lessons in the course")
    totalAttainableXp: int = Field(
        ..., description="Total XP that can be earned, not considering multipliers"
    )
    totalXpEarned: int = Field(
        ..., description="Total XP earned considering calculated multipliers"
    )

