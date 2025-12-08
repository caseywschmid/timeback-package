"""Request model for updating a demographic (PUT).

PUT /ims/oneroster/rostering/v1p2/demographics/{sourcedId}
"""

from typing import Optional, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus


class TimebackUpdateDemographicBody(BaseModel):
    """Body payload for demographic update under the top-level 'demographics' key."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    # Optional fields for update
    sourcedId: Optional[str] = Field(None, description="Unique identifier (should match path)")
    status: Optional[TimebackStatus] = Field(None, description="Status")
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


class TimebackUpdateDemographicRequest(BaseModel):
    """Top-level request wrapper for PUT /demographics/{sourcedId}."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    sourced_id: str = Field(..., description="The sourcedId of the demographic (path parameter)")
    demographics: TimebackUpdateDemographicBody = Field(..., description="Demographic data to update")

