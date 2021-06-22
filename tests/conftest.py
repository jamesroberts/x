import logging
import pytest

from x.app import init_app


@pytest.fixture
def client():
    app = init_app()

    with app.test_client() as client:
        with app.app_context():
            yield client
