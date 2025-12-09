from enum import Enum


class TimebackGrade(str, Enum):
    """Valid grade levels in the TimeBack API.
    Grade levels. -1 is Pre-K, 0 is Kindergarten, 1-12 are grades 1-12, 13 is AP.
    """

    PRE_K = "-1"
    KINDERGARTEN = "0"
    GRADE_1 = "1"
    GRADE_2 = "2"
    GRADE_3 = "3"
    GRADE_4 = "4"
    GRADE_5 = "5"
    GRADE_6 = "6"
    GRADE_7 = "7"
    GRAGE_8 = "8"
    GRADE_9 = "9"
    GRADE_10 = "10"
    GRADE_11 = "11"
    GRADE_12 = "12"
    AP = "13"
