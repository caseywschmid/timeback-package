from timeback.models.request.timeback_update_user_request import (
    TimebackUpdateUserRequest,
    TimebackUpdateUserBody,
)


def test_enabled_user_string_normalizes_to_bool_true():
    body = TimebackUpdateUserBody(
        enabledUser="true",
        givenName="A",
        familyName="B",
        email="a@example.com",
        roles=[],
    )
    req = TimebackUpdateUserRequest(user=body)
    data = req.to_dict()
    assert data["user"]["enabledUser"] is True

