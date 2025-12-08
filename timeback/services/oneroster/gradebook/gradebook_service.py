from typing import Optional, Dict, Any
from timeback.http import HttpClient
from timeback.models.request import (
    TimebackGetAllScoreScalesRequest,
    TimebackCreateScoreScaleRequest,
    TimebackGetScoreScaleRequest,
    TimebackPutScoreScaleRequest,
    TimebackDeleteScoreScaleRequest,
    TimebackGetScoreScalesForSchoolRequest,
    TimebackGetAllResultsRequest,
    TimebackCreateResultRequest,
    TimebackGetResultRequest,
    TimebackPutResultRequest,
    TimebackDeleteResultRequest,
    TimebackGetAllLineItemsRequest,
    TimebackCreateLineItemRequest,
    TimebackGetLineItemRequest,
    TimebackPutLineItemRequest,
    TimebackDeleteLineItemRequest,
    TimebackCreateResultForLineItemRequest,
    TimebackGetLineItemsForSchoolRequest,
    TimebackCreateLineItemsForSchoolRequest,
    TimebackPostResultsForAcademicSessionForClassRequest,
    TimebackPostLineItemsForClassRequest,
    TimebackGetResultsForLineItemForClassRequest,
    TimebackGetResultsForStudentForClassRequest,
    TimebackGetCategoriesForClassRequest,
    TimebackGetLineItemsForClassRequest,
    TimebackGetResultsForClassRequest,
    TimebackGetScoreScalesForClassRequest,
    TimebackGetAllCategoriesRequest,
)
from timeback.models.response import (
    TimebackGetAllScoreScalesResponse,
    TimebackCreateScoreScaleResponse,
    TimebackGetScoreScaleResponse,
    TimebackPutScoreScaleResponse,
    TimebackGetScoreScalesForSchoolResponse,
    TimebackGetAllResultsResponse,
    TimebackCreateResultResponse,
    TimebackGetResultResponse,
    TimebackPutResultResponse,
    TimebackGetAllLineItemsResponse,
    TimebackCreateLineItemResponse,
    TimebackGetLineItemResponse,
    TimebackPutLineItemResponse,
    TimebackCreateResultForLineItemResponse,
    TimebackCreateLineItemsForSchoolResponse,
    TimebackPostResultsForAcademicSessionForClassResponse,
    TimebackPostLineItemsForClassResponse,
    TimebackGetAllCategoriesResponse,
)
from timeback.services.oneroster.gradebook.endpoints.get_all_score_scales import (
    get_all_score_scales as get_all_score_scales_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.create_score_scale import (
    create_score_scale as create_score_scale_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.get_score_scale import (
    get_score_scale as get_score_scale_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.put_score_scale import (
    put_score_scale as put_score_scale_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.delete_score_scale import (
    delete_score_scale as delete_score_scale_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.get_score_scales_for_school import (
    get_score_scales_for_school as get_score_scales_for_school_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.get_all_results import (
    get_all_results as get_all_results_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.create_result import (
    create_result as create_result_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.get_result import (
    get_result as get_result_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.put_result import (
    put_result as put_result_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.delete_result import (
    delete_result as delete_result_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.get_all_line_items import (
    get_all_line_items as get_all_line_items_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.create_line_item import (
    create_line_item as create_line_item_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.get_line_item import (
    get_line_item as get_line_item_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.put_line_item import (
    put_line_item as put_line_item_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.delete_line_item import (
    delete_line_item as delete_line_item_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.create_result_for_line_item import (
    create_result_for_line_item as create_result_for_line_item_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.get_line_items_for_school import (
    get_line_items_for_school as get_line_items_for_school_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.create_line_items_for_school import (
    create_line_items_for_school as create_line_items_for_school_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.post_results_for_academic_session_for_class import (
    post_results_for_academic_session_for_class as post_results_for_academic_session_for_class_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.post_line_items_for_class import (
    post_line_items_for_class as post_line_items_for_class_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.get_results_for_line_item_for_class import (
    get_results_for_line_item_for_class as get_results_for_line_item_for_class_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.get_results_for_student_for_class import (
    get_results_for_student_for_class as get_results_for_student_for_class_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.get_categories_for_class import (
    get_categories_for_class as get_categories_for_class_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.get_all_categories import (
    get_all_categories as get_all_categories_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.get_line_items_for_class import (
    get_line_items_for_class as get_line_items_for_class_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.get_results_for_class import (
    get_results_for_class as get_results_for_class_endpoint,
)
from timeback.services.oneroster.gradebook.endpoints.get_score_scales_for_class import (
    get_score_scales_for_class as get_score_scales_for_class_endpoint,
)


class GradebookService:
    """Gradebook service methods for OneRoster."""

    def __init__(self, http: HttpClient):
        self._http = http

    def get_all_score_scales(
        self, request: TimebackGetAllScoreScalesRequest
    ) -> TimebackGetAllScoreScalesResponse:
        """Fetch a paginated list of score scales."""
        return get_all_score_scales_endpoint(self._http, request)

    def create_score_scale(
        self, request: TimebackCreateScoreScaleRequest
    ) -> TimebackCreateScoreScaleResponse:
        """Create a new score scale."""
        return create_score_scale_endpoint(self._http, request)

    def get_score_scale(
        self, request: TimebackGetScoreScaleRequest
    ) -> TimebackGetScoreScaleResponse:
        """Fetch a single score scale by sourcedId."""
        return get_score_scale_endpoint(self._http, request)

    def put_score_scale(
        self, request: TimebackPutScoreScaleRequest
    ) -> TimebackPutScoreScaleResponse:
        """Update or create a score scale."""
        return put_score_scale_endpoint(self._http, request)

    def delete_score_scale(
        self, request: TimebackDeleteScoreScaleRequest
    ) -> Optional[Dict[str, Any]]:
        """Delete a score scale."""
        return delete_score_scale_endpoint(self._http, request)

    def get_score_scales_for_school(
        self, request: TimebackGetScoreScalesForSchoolRequest
    ) -> TimebackGetScoreScalesForSchoolResponse:
        """Fetch score scales for a specific school."""
        return get_score_scales_for_school_endpoint(self._http, request)

    def get_all_results(
        self, request: TimebackGetAllResultsRequest
    ) -> TimebackGetAllResultsResponse:
        """Fetch a paginated list of results."""
        return get_all_results_endpoint(self._http, request)

    def create_result(
        self, request: TimebackCreateResultRequest
    ) -> TimebackCreateResultResponse:
        """Create a new result."""
        return create_result_endpoint(self._http, request)

    def get_result(
        self, request: TimebackGetResultRequest
    ) -> TimebackGetResultResponse:
        """Fetch a single result by sourcedId."""
        return get_result_endpoint(self._http, request)

    def put_result(
        self, request: TimebackPutResultRequest
    ) -> TimebackPutResultResponse:
        """Update or create a result."""
        return put_result_endpoint(self._http, request)

    def delete_result(
        self, request: TimebackDeleteResultRequest
    ) -> Optional[Dict[str, Any]]:
        """Delete a result."""
        return delete_result_endpoint(self._http, request)

    def get_all_line_items(
        self, request: TimebackGetAllLineItemsRequest
    ) -> TimebackGetAllLineItemsResponse:
        """Fetch a paginated list of line items."""
        return get_all_line_items_endpoint(self._http, request)

    def create_line_item(
        self, request: TimebackCreateLineItemRequest
    ) -> TimebackCreateLineItemResponse:
        """Create a new line item."""
        return create_line_item_endpoint(self._http, request)

    def get_line_item(
        self, request: TimebackGetLineItemRequest
    ) -> TimebackGetLineItemResponse:
        """Fetch a single line item by sourcedId."""
        return get_line_item_endpoint(self._http, request)

    def put_line_item(
        self, request: TimebackPutLineItemRequest
    ) -> TimebackPutLineItemResponse:
        """Update or create a line item."""
        return put_line_item_endpoint(self._http, request)

    def delete_line_item(
        self, request: TimebackDeleteLineItemRequest
    ) -> Optional[Dict[str, Any]]:
        """Soft delete a line item."""
        return delete_line_item_endpoint(self._http, request)

    def create_result_for_line_item(
        self, request: TimebackCreateResultForLineItemRequest
    ) -> TimebackCreateResultForLineItemResponse:
        """Create results for a specific line item."""
        return create_result_for_line_item_endpoint(self._http, request)

    def get_line_items_for_school(
        self, request: TimebackGetLineItemsForSchoolRequest
    ) -> TimebackGetAllLineItemsResponse:
        """Get line items for a specific school."""
        return get_line_items_for_school_endpoint(self._http, request)

    def create_line_items_for_school(
        self, request: TimebackCreateLineItemsForSchoolRequest
    ) -> TimebackCreateLineItemsForSchoolResponse:
        """Create line items for a specific school."""
        return create_line_items_for_school_endpoint(self._http, request)

    def post_results_for_academic_session_for_class(
        self, request: TimebackPostResultsForAcademicSessionForClassRequest
    ) -> TimebackPostResultsForAcademicSessionForClassResponse:
        """Create results for a specific academic session and class."""
        return post_results_for_academic_session_for_class_endpoint(self._http, request)

    def post_line_items_for_class(
        self, request: TimebackPostLineItemsForClassRequest
    ) -> TimebackPostLineItemsForClassResponse:
        """Create line items for a specific class."""
        return post_line_items_for_class_endpoint(self._http, request)

    def get_results_for_line_item_for_class(
        self, request: TimebackGetResultsForLineItemForClassRequest
    ) -> TimebackGetAllResultsResponse:
        """Get results for a specific line item and class."""
        return get_results_for_line_item_for_class_endpoint(self._http, request)

    def get_results_for_student_for_class(
        self, request: TimebackGetResultsForStudentForClassRequest
    ) -> TimebackGetAllResultsResponse:
        """Get results for a specific student and class."""
        return get_results_for_student_for_class_endpoint(self._http, request)

    def get_categories_for_class(
        self, request: TimebackGetCategoriesForClassRequest
    ) -> TimebackGetAllCategoriesResponse:
        """Get categories for a specific class."""
        return get_categories_for_class_endpoint(self._http, request)

    def get_all_categories(
        self, request: TimebackGetAllCategoriesRequest
    ) -> TimebackGetAllCategoriesResponse:
        """Fetch a paginated list of all categories."""
        return get_all_categories_endpoint(self._http, request)

    def get_line_items_for_class(
        self, request: TimebackGetLineItemsForClassRequest
    ) -> TimebackGetAllLineItemsResponse:
        """Get line items for a specific class."""
        return get_line_items_for_class_endpoint(self._http, request)

    def get_results_for_class(
        self, request: TimebackGetResultsForClassRequest
    ) -> TimebackGetAllResultsResponse:
        """Get results for a specific class."""
        return get_results_for_class_endpoint(self._http, request)

    def get_score_scales_for_class(
        self, request: TimebackGetScoreScalesForClassRequest
    ) -> TimebackGetScoreScalesForSchoolResponse:
        """Get score scales for a specific class."""
        return get_score_scales_for_class_endpoint(self._http, request)





