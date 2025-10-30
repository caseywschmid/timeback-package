import os
import pytest

from timeback import Timeback


@pytest.mark.integration
def test_get_all_users_integration():
    """Integration test calling real API: list users (read-only).

    Requires env vars:
    - TIMEBACK_CLIENT_ID
    - TIMEBACK_CLIENT_SECRET
    - TIMEBACK_ENVIRONMENT

    To run: pytest -m integration
    """
    required_vars = [
        "TIMEBACK_CLIENT_ID",
        "TIMEBACK_CLIENT_SECRET",
        "TIMEBACK_ENVIRONMENT",
    ]
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        pytest.skip(f"Missing required environment variables: {missing_vars}")

    client = Timeback()
    resp = client.oneroster.rostering.get_all_users(limit=1)

    assert resp is not None
    assert resp.limit >= 1
    assert resp.pageNumber >= 1
    assert resp.pageCount >= 1
    assert isinstance(resp.users, list)
    if resp.users:
        user = resp.users[0]
        assert user.sourcedId
        assert user.givenName is not None
        assert user.familyName is not None


