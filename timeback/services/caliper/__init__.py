"""Caliper service for the Caliper Events API.

This service provides methods for creating, validating, and listing Caliper events
following the IMS Caliper Analytics specification for learning analytics.

Caliper uses a dedicated base URL separate from the OneRoster API:
- Production: https://caliper.alpha-1edtech.ai
- Staging: https://caliper-staging.alpha-1edtech.ai

Used by:
- timeback/client.py - exposed as client.caliper
"""

from timeback.services.caliper.caliper_service import CaliperService

__all__ = ["CaliperService"]

