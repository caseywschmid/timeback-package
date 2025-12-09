"""Resources service for OneRoster Resources API.

This service provides methods for managing educational resources.
"""

from typing import Any, Dict, Optional

from timeback.http import HttpClient
from timeback.models.request import (
    TimebackGetAllResourcesRequest,
    TimebackCreateResourceRequest,
    TimebackGetResourceRequest,
    TimebackUpdateResourceRequest,
    TimebackGetResourcesForClassRequest,
    TimebackGetResourcesForCourseRequest,
    TimebackGetResourcesForUserRequest,
)
from timeback.models.response import (
    TimebackGetAllResourcesResponse,
    TimebackCreateResourceResponse,
    TimebackGetResourceResponse,
    TimebackUpdateResourceResponse,
)
from timeback.services.oneroster.resources.endpoints.get_all_resources import (
    get_all_resources as get_all_resources_endpoint,
)
from timeback.services.oneroster.resources.endpoints.create_resource import (
    create_resource as create_resource_endpoint,
)
from timeback.services.oneroster.resources.endpoints.get_resource import (
    get_resource as get_resource_endpoint,
)
from timeback.services.oneroster.resources.endpoints.update_resource import (
    update_resource as update_resource_endpoint,
)
from timeback.services.oneroster.resources.endpoints.delete_resource import (
    delete_resource as delete_resource_endpoint,
)
from timeback.services.oneroster.resources.endpoints.get_resources_for_class import (
    get_resources_for_class as get_resources_for_class_endpoint,
)
from timeback.services.oneroster.resources.endpoints.get_resources_for_course import (
    get_resources_for_course as get_resources_for_course_endpoint,
)
from timeback.services.oneroster.resources.endpoints.get_resources_for_user import (
    get_resources_for_user as get_resources_for_user_endpoint,
)


class ResourcesService:
    """Resources service methods for OneRoster Resources API."""

    def __init__(self, http: HttpClient):
        self._http = http

    def get_all_resources(
        self, request: TimebackGetAllResourcesRequest
    ) -> TimebackGetAllResourcesResponse:
        """Fetch a paginated list of resources."""
        return get_all_resources_endpoint(self._http, request)

    def create_resource(
        self, request: TimebackCreateResourceRequest
    ) -> TimebackCreateResourceResponse:
        """Create a new resource."""
        return create_resource_endpoint(self._http, request)

    def get_resource(
        self, request: TimebackGetResourceRequest
    ) -> TimebackGetResourceResponse:
        """Fetch a single resource by sourcedId."""
        return get_resource_endpoint(self._http, request)

    def update_resource(
        self, request: TimebackUpdateResourceRequest
    ) -> TimebackUpdateResourceResponse:
        """Update a resource by sourcedId."""
        return update_resource_endpoint(self._http, request)

    def delete_resource(self, sourced_id: str) -> Optional[Dict[str, Any]]:
        """Delete (tombstone) a resource by sourcedId."""
        return delete_resource_endpoint(self._http, sourced_id)

    def get_resources_for_class(
        self, request: TimebackGetResourcesForClassRequest
    ) -> TimebackGetAllResourcesResponse:
        """Fetch resources for a specific class."""
        return get_resources_for_class_endpoint(self._http, request)

    def get_resources_for_course(
        self, request: TimebackGetResourcesForCourseRequest
    ) -> TimebackGetAllResourcesResponse:
        """Fetch resources for a specific course."""
        return get_resources_for_course_endpoint(self._http, request)

    def get_resources_for_user(
        self, request: TimebackGetResourcesForUserRequest
    ) -> TimebackGetAllResourcesResponse:
        """Fetch resources for a specific user."""
        return get_resources_for_user_endpoint(self._http, request)

