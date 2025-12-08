"""Request model for creating a demographic.

POST /ims/oneroster/rostering/v1p2/demographics
"""

from typing import Optional, Dict, Any, Literal
from uuid import uuid4
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus


class TimebackCreateDemographicBody(BaseModel):
    """Body payload for demographic creation under the top-level 'demographics' key.
    
    Attributes:
        Required:
            - sourcedId (str): Unique identifier (auto-generated UUID if omitted)
        
        Optional:
            - status (TimebackStatus, optional): Demographic status. Defaults to "active".
            - metadata (Dict[str, Any], optional): Custom metadata
            - birthDate (str, optional): Birth date (YYYY-MM-DD)
            - sex (str, optional): Sex (male/female)
            - Race/ethnicity fields as string "true"/"false" or None
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    # Required field
    sourcedId: Optional[str] = Field(default_factory=lambda: str(uuid4()), description="Unique identifier")
    
    # Common fields
    status: Optional[TimebackStatus] = Field(default=TimebackStatus.ACTIVE, description="Status")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    
    # Birth information
    birthDate: Optional[str] = Field(None, description="Birth date (YYYY-MM-DD)")
    sex: Optional[Literal["male", "female"]] = Field(None, description="Sex (male/female)")
    
    # Race/ethnicity fields
    americanIndianOrAlaskaNative: Optional[str] = Field(None, description="American Indian or Alaska Native")
    asian: Optional[str] = Field(None, description="Asian")
    blackOrAfricanAmerican: Optional[str] = Field(None, description="Black or African American")
    nativeHawaiianOrOtherPacificIslander: Optional[str] = Field(None, description="Native Hawaiian or Other Pacific Islander")
    white: Optional[str] = Field(None, description="White")
    demographicRaceTwoOrMoreRaces: Optional[str] = Field(None, description="Two or more races")
    hispanicOrLatinoEthnicity: Optional[str] = Field(None, description="Hispanic or Latino ethnicity")
    
    # Birth location
    countryOfBirthCode: Optional[str] = Field(None, description="Country of birth code")
    stateOfBirthAbbreviation: Optional[str] = Field(None, description="State of birth abbreviation")
    cityOfBirth: Optional[str] = Field(None, description="City of birth")
    
    # Residence
    publicSchoolResidenceStatus: Optional[str] = Field(None, description="Public school residence status")


class TimebackCreateDemographicRequest(BaseModel):
    """Top-level request wrapper for POST /demographics."""
    
    model_config = ConfigDict(populate_by_name=True)
    demographics: TimebackCreateDemographicBody = Field(..., description="Demographic data to create")

