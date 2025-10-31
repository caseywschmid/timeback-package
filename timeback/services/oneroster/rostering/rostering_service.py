from typing import Optional, Sequence, Union
from timeback.http import HttpClient
from timeback.models.timeback_user import TimebackUser
from timeback.models.response import TimebackGetAllUsersResponse
from timeback.models.request import (
    TimebackUpdateUserRequest,
)
from timeback.services.oneroster.rostering.endpoints.get_user import (
    get_user as get_user_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.get_all_users import (
    get_all_users as get_all_users_endpoint,
)
from timeback.services.oneroster.rostering.endpoints.update_user import (
    update_user as update_user_endpoint,
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

    def get_all_users(
        self,
        *,
        fields: Optional[Union[str, Sequence[str]]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        order_by: Optional[str] = None,
        filter: Optional[str] = None,
        search: Optional[str] = None,
    ) -> TimebackGetAllUsersResponse:
        """Fetch a paginated list of users."""
        return get_all_users_endpoint(
            self._http,
            fields=fields,
            limit=limit,
            offset=offset,
            sort=sort,
            order_by=order_by,
            filter=filter,
            search=search,
        )

    def update_user(
        self, sourced_id: str, request: TimebackUpdateUserRequest
    ) -> TimebackUser:
        """Update an existing user by sourcedId."""
        return update_user_endpoint(self._http, sourced_id, request)
