"""Response model for updating a section.

PUT /assessment-tests/{assessmentTestIdentifier}/test-parts/{testPartIdentifier}/sections/{identifier}

Used by:
- timeback/services/qti/endpoints/update_section.py
"""

from pydantic import ConfigDict
from timeback.models.timeback_qti_section import TimebackQTISection


class TimebackUpdateSectionResponse(TimebackQTISection):
    """Response model for updating a section.
    
    Inherits all fields from TimebackQTISection.
    Returns the updated section with all its properties.
    """
    
    model_config = ConfigDict(populate_by_name=True)

