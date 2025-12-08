"""Demographic model for the TimeBack API.

This module provides a Pydantic model for working with demographic data
in the TimeBack API following the OneRoster 1.2 specification.
"""

from typing import Optional, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from timeback.enums import TimebackStatus


class TimebackDemographic(BaseModel):
    """
    Represents demographic information about a user.

    Demographics include birth information, sex, and race/ethnicity data.
    Most fields are nullable as demographic data is often incomplete.
    """

    model_config = ConfigDict(populate_by_name=True)

    # Required field
    sourcedId: str = Field(..., description="Unique identifier for this demographic record")
    
    # Common fields
    status: Optional[TimebackStatus] = Field(default=TimebackStatus.ACTIVE, description="Status of the record")
    dateLastModified: Optional[str] = Field(None, description="Last modification timestamp")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")
    
    # Birth information
    birthDate: Optional[str] = Field(None, description="Birth date (YYYY-MM-DD)")
    sex: Optional[Literal["male", "female"]] = Field(None, description="Sex (male/female)")
    
    # Race/ethnicity fields - per OneRoster these are string booleans ("true"/"false") or null
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

