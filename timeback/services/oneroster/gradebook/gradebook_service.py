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
)
from timeback.models.response import (
    TimebackGetAllScoreScalesResponse,
    TimebackCreateScoreScaleResponse,
    TimebackGetScoreScaleResponse,
    TimebackPutScoreScaleResponse,
    TimebackGetScoreScalesForSchoolResponse,
    TimebackGetAllResultsResponse,
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





