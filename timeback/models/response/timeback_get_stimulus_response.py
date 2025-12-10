"""Response model for getting a QTI stimulus.

GET /stimuli/{identifier}

Used by:
- timeback/services/qti/endpoints/get_stimulus.py
"""

from timeback.models.timeback_qti_stimulus import TimebackQTIStimulus


class TimebackGetStimulusResponse(TimebackQTIStimulus):
    """Response model for getting a QTI stimulus.
    
    The response is the complete stimulus object with all fields.
    
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
        - rawXml (str): Raw XML representation
        - content (dict, optional): Parsed XML content structure
        - createdAt (datetime): Creation timestamp
        - updatedAt (datetime): Last update timestamp
    """
    
    pass

