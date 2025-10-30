import pytest


def test_missing_env_vars_raise_configuration_error(monkeypatch):
    # Clear env vars
    for key in ("TIMEBACK_CLIENT_ID", "TIMEBACK_CLIENT_SECRET", "TIMEBACK_ENVIRONMENT"):
        monkeypatch.delenv(key, raising=False)

    from timeback.errors import ConfigurationError
    from timeback import Timeback

    with pytest.raises(ConfigurationError):
        _ = Timeback()


def test_invalid_environment_raises_configuration_error(monkeypatch):
    monkeypatch.setenv("TIMEBACK_CLIENT_ID", "id")
    monkeypatch.setenv("TIMEBACK_CLIENT_SECRET", "secret")
    monkeypatch.setenv("TIMEBACK_ENVIRONMENT", "invalid-env")

    from timeback.errors import ConfigurationError
    from timeback import Timeback

    with pytest.raises(ConfigurationError):
        _ = Timeback()
