"""Request model for updating a QTI stimulus.

PUT /stimuli/{identifier}

Used by:
- timeback/services/qti/endpoints/update_stimulus.py
"""

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, ConfigDict, Field
from timeback.models.timeback_catalog_entry import TimebackCatalogEntry
from timeback.models.timeback_qti_stimulus import TimebackQTIStylesheet


class TimebackUpdateStimulusRequest(BaseModel):
    """Request model for updating a QTI stimulus.
    
    The identifier in this model is used for both the URL path and the request body.
    All other fields are updated in the stimulus.
    
    Attributes:
        Required:
            - identifier (str): Unique identifier of the stimulus to update (used in path)
            - title (str): Human-readable title of the stimulus
            - content (str): HTML content for the stimulus body
        
        Optional:
            - label (str, optional): Human-readable label describing the stimulus
            - language (str, optional): Language code (default: 'en')
            - stylesheet (TimebackQTIStylesheet, optional): External stylesheet reference.
              See TimebackQTIStylesheet for structure.
            - catalog_info (list, optional): Array of catalog cards for accessibility.
              See TimebackCatalogEntry for structure.
            - tool_name (str, optional): Name of the tool updating the stimulus
            - tool_version (str, optional): Version of the tool
            - metadata (dict, optional): Additional custom metadata
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    # Required fields
    identifier: str = Field(
        ...,
        description="Unique identifier of the stimulus to update"
    )
    title: str = Field(
        ...,
        description="Human-readable title of the stimulus"
    )
    content: str = Field(
        ...,
        description="HTML content for the stimulus body"
    )
    
    # Optional fields
    label: Optional[str] = Field(
        None,
        description="Human-readable label describing the stimulus"
    )
    language: Optional[str] = Field(
        default="en",
        description="Language code for the stimulus content"
    )
    stylesheet: Optional[TimebackQTIStylesheet] = Field(
        None,
        description="External stylesheet reference"
    )
    catalog_info: Optional[List[TimebackCatalogEntry]] = Field(
        None,
        alias="catalogInfo",
        description="Array of catalog cards for accessibility support"
    )
    tool_name: Optional[str] = Field(
        None,
        alias="toolName",
        description="Name of the tool updating the stimulus"
    )
    tool_version: Optional[str] = Field(
        None,
        alias="toolVersion",
        description="Version of the tool updating the stimulus"
    )
    metadata: Optional[Dict[str, Any]] = Field(
        None,
        description="Additional custom metadata"
    )

