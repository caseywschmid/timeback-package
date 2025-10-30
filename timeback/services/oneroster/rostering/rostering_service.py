from typing import Optional, Sequence, Union
from timeback.http import HttpClient
from timeback.models.timeback_user import TimebackUser
from timeback.services.oneroster.rostering.endpoints.get_user import (
    get_user as get_user_endpoint,
)


class RosteringService:
    """Rostering service methods for OneRoster."""

    def __init__(self, http: HttpClient):
        self._http = http

    def get_user(
        self,
        sourced_id: str,
        fields: Optional[Union[str, Sequence[str]]] = None,
    ) -> TimebackUser:
        """Fetch a single user by sourcedId."""
        return get_user_endpoint(self._http, sourced_id, fields=fields)
