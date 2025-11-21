from enum import Enum


class TimebackSubject(str, Enum):
    """Valid subjects in the TimeBack API."""

    READING = "Reading"
    LANGUAGE = "Language"
    VOCABULARY = "Vocabulary"
    SOCIAL_STUDIES = "Social Studies"
    WRITING = "Writing"
    SCIENCE = "Science"
    FAST_MATH = "FastMath"
    MATH = "Math"
