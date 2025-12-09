"""CASE service for the IMS CASE API.

This service provides methods for managing Competency and Academic Standards Exchange (CASE)
content including CF Documents, CF Items, CF Associations, and CF Packages.

CASE uses the same base URL as OneRoster (api.alpha-1edtech.ai) with path prefix /ims/case/v1p1/

Used by:
- timeback/client.py - exposed as client.case
"""

from timeback.services.case.case_service import CASEService

__all__ = ["CASEService"]

