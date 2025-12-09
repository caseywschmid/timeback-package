from timeback.services.oneroster.rostering.endpoints.delete_school import delete_school
from timeback.errors import NotFoundError


class MockHttp:
    def __init__(self):
        self.called_with = None

    def delete(self, path):
        self.called_with = path
        return None


def test_delete_school_success():
    """Test successful school deletion."""
    http = MockHttp()
    result = delete_school(http, "school1")
    assert http.called_with.endswith("/ims/oneroster/rostering/v1p2/schools/school1")
    assert result is None


def test_delete_school_not_found_propagates():
    """Test that NotFoundError is propagated when school doesn't exist."""
    class MockHttpNotFound:
        def delete(self, path):
            raise NotFoundError("Resource not found")

    try:
        delete_school(MockHttpNotFound(), "missing")
        assert False, "Expected NotFoundError"
    except NotFoundError:
        pass

