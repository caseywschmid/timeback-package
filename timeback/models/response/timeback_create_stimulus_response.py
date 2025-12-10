"""Response model for creating a QTI stimulus.

POST /stimuli

Used by:
- timeback/services/qti/endpoints/create_stimulus.py
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_qti_stimulus import TimebackQTIStimulus


class TimebackCreateStimulusResponse(TimebackQTIStimulus):
    """Response model for creating a QTI stimulus.
    
    The response is the created stimulus object with all fields populated
    by the server, including rawXml and timestamps.
    
    Inherits all attributes from TimebackQTIStimulus:
        - identifier (str): Unique identifier for the stimulus
        - title (str): Human-readable title
        - catalogInfo (list): Array of catalog cards
        - label (str, optional): Human-readable label
        - language (str): Language code (default: 'en')
        - stylesheet (TimebackQTIStylesheet, optional): External stylesheet
        - toolName (str, optional): Tool name
        - toolVersion (str, optional): Tool version
        - metadata (dict, optional): Custom metadata
        - rawXml (str): Generated raw XML representation
        - content (dict, optional): Parsed XML content structure
        - createdAt (datetime): Creation timestamp
        - updatedAt (datetime): Last update timestamp
    """
    
    pass

