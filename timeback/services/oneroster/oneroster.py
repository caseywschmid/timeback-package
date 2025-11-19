from timeback.http import HttpClient
from timeback.services.oneroster.rostering import RosteringService
from timeback.services.oneroster.gradebook import GradebookService


class OneRosterService:
    """Container for OneRoster services."""

    def __init__(self, http: HttpClient):
        self.rostering = RosteringService(http)
        self.gradebook = GradebookService(http)

