"""pytest conftest for fotmob_service."""
import pytest


@pytest.fixture(autouse=True)
def reset_db(db):  # noqa: ARG001
    pass
