from timeback.services.oneroster.rostering.endpoints.delete_user import delete_user
from timeback.errors import NotFoundError


class MockHttp:
    def __init__(self):
        self.called_with = None

    def delete(self, path):
        self.called_with = path
        return None


def test_delete_user_success():
    http = MockHttp()
    result = delete_user(http, "u1")
    assert http.called_with.endswith("/ims/oneroster/rostering/v1p2/users/u1")
    assert result is None


def test_delete_user_not_found_propagates():
    class MockHttpNotFound:
        def delete(self, path):
            raise NotFoundError("Resource not found")

    try:
        delete_user(MockHttpNotFound(), "missing")
        assert False, "Expected NotFoundError"
    except NotFoundError:
        pass


