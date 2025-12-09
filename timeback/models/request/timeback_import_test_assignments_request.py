"""Request model for importing test assignments from Google Sheets.

POST /powerpath/test-assignments/import
"""

from pydantic import BaseModel, ConfigDict, Field


class TimebackImportTestAssignmentsRequest(BaseModel):
    """Request model for importing test assignments from Google Sheets.
    
    Fetches a public Google Sheet tab as CSV and creates test
    assignments in bulk. Requires columns: student, subject, grade.
    
    All-or-nothing operation.
    
    Attributes:
        - spreadsheetUrl (str): Publicly readable Google Sheets URL
        - sheet (str): The Sheet/tab name to read (case-sensitive)
    """

    model_config = ConfigDict(populate_by_name=True)

    spreadsheetUrl: str = Field(..., description="Google Sheets URL")
    sheet: str = Field(..., description="Sheet/tab name")

