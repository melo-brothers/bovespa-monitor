# https://github.com/psenna/fast-api-tutorial/blob/tutorial007-testes-automatizados/cria_tabelas.py
import os

import pytest
from fastapi.testclient import TestClient

from main import app

DATABASE_URL = "sqlite:///./test_db.db"
os.environ["DATABASE_URL"] = DATABASE_URL
os.environ["DATABASE_URL_SYNC"] = DATABASE_URL
os.environ["TEST_DB"] = "True"


@pytest.fixture(scope="function")
def client():
    with TestClient(app) as c:
        yield c
