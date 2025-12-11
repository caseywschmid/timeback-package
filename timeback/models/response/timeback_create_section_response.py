"""Response model for creating a section.

POST /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections

Used by:
- timeback/services/qti/endpoints/create_section.py
"""

from pydantic import ConfigDict
from timeback.models.timeback_qti_section import TimebackQTISection


class TimebackCreateSectionResponse(TimebackQTISection):
    """Response model for creating a section.
    
    Inherits all fields from TimebackQTISection.
    Returns the created section with all its properties.
    """
    
    model_config = ConfigDict(populate_by_name=True)

