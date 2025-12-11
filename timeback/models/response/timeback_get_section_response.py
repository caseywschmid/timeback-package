"""Response model for getting a section.

GET /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections/{identifier}

Used by:
- timeback/services/qti/endpoints/get_section.py
"""

from pydantic import ConfigDict
from timeback.models.timeback_qti_section import TimebackQTISection


class TimebackGetSectionResponse(TimebackQTISection):
    """Response model for getting a section.
    
    Inherits all fields from TimebackQTISection.
    Returns the section with all its properties and item references.
    """
    
    model_config = ConfigDict(populate_by_name=True)

