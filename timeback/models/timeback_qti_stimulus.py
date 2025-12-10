"""QTI 3.0 compliant stimulus that can be referenced by assessment items.

This model represents the stimulus data structure returned from the QTI API.
Used by:
- timeback/services/qti/endpoints/search_stimuli.py
- timeback/services/qti/endpoints/get_stimulus.py
- timeback/services/qti/endpoints/create_stimulus.py
- timeback/services/qti/endpoints/update_stimulus.py
"""

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from timeback.models.timeback_catalog_entry import TimebackCatalogEntry


class TimebackQTIStylesheet(BaseModel):
    """Stylesheet reference for a QTI stimulus.
    
    Attributes:
        - href (str): The identifier or location of the external stylesheet
        - type (str): The type of the external stylesheet (e.g., "text/css")
    """
    
    href: str = Field(..., description="The identifier or location of the external stylesheet")
    type: str = Field(..., description="The type of the external stylesheet")


class TimebackQTIStimulus(BaseModel):
    """QTI 3.0 compliant stimulus that can be referenced by assessment items.
    
    Stimuli are shared content pieces (text, images, audio, video) that provide
    context for assessment items and can be referenced by multiple questions.
    
    Attributes:
        - identifier (str): Unique identifier for the stimulus
        - title (str): Human-readable title of the stimulus
        - catalogInfo (list): Array of catalog cards with accessibility support info.
          See TimebackCatalogEntry for structure.
        - label (str, optional): A human readable label that can describe the stimulus
        - language (str, optional): Language code for the stimulus content (default: "en")
        - stylesheet (TimebackQTIStylesheet, optional): External stylesheet associated with
          the stimulus. See TimebackQTIStylesheet for structure.
        - toolName (str, optional): Tool name that created the stimulus
        - toolVersion (str, optional): Version of the tool that created the stimulus
        - metadata (dict, optional): Additional custom metadata
        - rawXml (str): Raw XML representation of the stimulus (auto-generated)
        - content (dict, optional): Parsed XML content (use rawXml for production)
        - createdAt (datetime): Timestamp when the stimulus was created
        - updatedAt (datetime): Timestamp when the stimulus was last updated
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    identifier: str = Field(..., description="Unique identifier for the stimulus")
    title: str = Field(..., description="Human-readable title of the stimulus")
    catalog_info: List[TimebackCatalogEntry] = Field(
        default_factory=list,
        alias="catalogInfo",
        description="Array of catalog cards with accessibility support info"
    )
    label: Optional[str] = Field(
        None, description="A human readable label that can describe the stimulus"
    )
    language: str = Field(
        default="en", description="Language code for the stimulus content"
    )
    stylesheet: Optional[TimebackQTIStylesheet] = Field(
        None, description="External stylesheet associated with the stimulus"
    )
    tool_name: Optional[str] = Field(
        None,
        alias="toolName",
        description="Tool name that created the stimulus"
    )
    tool_version: Optional[str] = Field(
        None,
        alias="toolVersion",
        description="Version of the tool that created the stimulus"
    )
    metadata: Optional[Dict[str, Any]] = Field(
        None, description="Additional custom metadata"
    )
    raw_xml: str = Field(
        ...,
        alias="rawXml",
        description="Raw XML representation of the stimulus (auto-generated from JSON/XML input)"
    )
    content: Optional[Dict[str, Any]] = Field(
        None,
        description="Parsed XML content structure. For production use, rawXml is recommended."
    )
    created_at: datetime = Field(
        ...,
        alias="createdAt",
        description="Timestamp when the stimulus was created"
    )
    updated_at: datetime = Field(
        ...,
        alias="updatedAt",
        description="Timestamp when the stimulus was last updated"
    )
