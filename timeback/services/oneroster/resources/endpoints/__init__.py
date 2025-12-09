"""Resources endpoints for OneRoster Resources API."""

from timeback.services.oneroster.resources.endpoints.get_all_resources import get_all_resources
from timeback.services.oneroster.resources.endpoints.create_resource import create_resource
from timeback.services.oneroster.resources.endpoints.get_resource import get_resource
from timeback.services.oneroster.resources.endpoints.update_resource import update_resource
from timeback.services.oneroster.resources.endpoints.delete_resource import delete_resource
from timeback.services.oneroster.resources.endpoints.get_resources_for_class import get_resources_for_class
from timeback.services.oneroster.resources.endpoints.get_resources_for_course import get_resources_for_course
from timeback.services.oneroster.resources.endpoints.get_resources_for_user import get_resources_for_user

__all__ = [
    "get_all_resources",
    "create_resource",
    "get_resource",
    "update_resource",
    "delete_resource",
    "get_resources_for_class",
    "get_resources_for_course",
    "get_resources_for_user",
]

