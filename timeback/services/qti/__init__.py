"""QTI service for the QTI API.

This service provides methods for managing QTI (Question and Test Interoperability)
content including stimuli, assessment items, assessment tests, test parts, and sections.

QTI uses a dedicated base URL separate from the OneRoster API:
- Production: https://qti.alpha-1edtech.ai/api
- Staging: https://qti-staging.alpha-1edtech.ai/api

Used by:
- timeback/client.py - exposed as client.qti
"""

from timeback.services.qti.qti_service import QTIService

__all__ = ["QTIService"]

