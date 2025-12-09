"""Response model for getting screening results.

GET /powerpath/screening/results/{userId}
"""

from typing import Dict, Optional
from pydantic import BaseModel, RootModel

from timeback.models.timeback_screening_result import TimebackScreeningResult


class TimebackGetScreeningResultsResponse(RootModel[Dict[str, Optional[TimebackScreeningResult]]]):
    """Response model for getting screening results.
    
    The response is a dictionary where keys are subject names and values are
    screening results for that subject (or null if no result exists).
    
    Example response structure:
        {
            "Reading": {"grade": "5", "ritScore": 210, "testName": "...", "completedAt": "..."},
            "Math": null,
            "Language": {"grade": "4", "ritScore": 195, "testName": "...", "completedAt": "..."}
        }
    """
    pass

