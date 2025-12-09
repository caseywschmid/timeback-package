from timeback.services.oneroster.rostering.endpoints.delete_class import delete_class
from timeback.errors import NotFoundError


class MockHttp:
    def __init__(self):
        self.called_with = None

    def delete(self, path):
        self.called_with = path
        return None


def test_delete_class_success():
    """Test successful class deletion."""
    http = MockHttp()
    result = delete_class(http, "class1")
    assert http.called_with.endswith("/ims/oneroster/rostering/v1p2/classes/class1")
    assert result is None


def test_delete_class_not_found_propagates():
    """Test that NotFoundError is propagated when class doesn't exist."""
    class MockHttpNotFound:
        def delete(self, path):
            raise NotFoundError("Resource not found")

    try:
        delete_class(MockHttpNotFound(), "missing")
        assert False, "Expected NotFoundError"
    except NotFoundError:
        pass

