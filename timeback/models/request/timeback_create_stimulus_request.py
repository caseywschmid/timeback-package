"""Request model for creating a QTI stimulus.

POST /stimuli

Used by:
- timeback/services/qti/endpoints/create_stimulus.py
"""

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, ConfigDict, Field
from timeback.models.timeback_catalog_entry import TimebackCatalogEntry
from timeback.models.timeback_qti_stimulus import TimebackQTIStylesheet


class TimebackCreateStimulusRequest(BaseModel):
    """Request model for creating a QTI stimulus.
    
    Supports two formats for creating stimuli:
    1. JSON format: Provide HTML content in the `content` field
    2. XML format: Provide raw QTI XML in the `xml` field with format='xml'
    
    Attributes:
        Required:
            - identifier (str): Unique identifier for the stimulus
            - title (str): Human-readable title of the stimulus
            - content (str): HTML content for the stimulus body (required for JSON format)
        
        Optional:
            - format (str, optional): Format type ('json' or 'xml', default: 'json')
            - xml (str, optional): Raw QTI XML (required when format='xml')
            - label (str, optional): Human-readable label describing the stimulus
            - language (str, optional): Language code (default: 'en')
            - stylesheet (TimebackQTIStylesheet, optional): External stylesheet reference.
              See TimebackQTIStylesheet for structure.
            - catalog_info (list, optional): Array of catalog cards for accessibility.
              See TimebackCatalogEntry for structure.
            - tool_name (str, optional): Name of the tool creating the stimulus
            - tool_version (str, optional): Version of the tool
            - metadata (dict, optional): Additional custom metadata
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    # Required fields
    identifier: str = Field(
        ...,
        description="Unique identifier for the stimulus on the service provider"
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
    format: Optional[str] = Field(
        default="json",
        description="Format type: 'json' for HTML content or 'xml' for raw QTI XML"
    )
    xml: Optional[str] = Field(
        None,
        description="Raw QTI XML content (required when format='xml')"
    )
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
        description="Name of the tool creating the stimulus"
    )
    tool_version: Optional[str] = Field(
        None,
        alias="toolVersion",
        description="Version of the tool creating the stimulus"
    )
    metadata: Optional[Dict[str, Any]] = Field(
        None,
        description="Additional custom metadata"
    )

