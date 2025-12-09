"""PowerPath service for the PowerPath API.

This service provides methods for placement tests, lesson plans, screening,
and adaptive assessment functionality.

Used by:
- timeback/client.py - exposed as client.powerpath
"""

from timeback.services.powerpath.powerpath_service import PowerPathService

__all__ = ["PowerPathService"]

