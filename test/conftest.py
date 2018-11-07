import os
import tempfile

import pytest
import sqlite3
from homework.app import create_app
#from homework.app.variant import db


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///' + db_path
    })

    sql_migration = os.path.join(os.path.dirname(os.path.realpath('__file__')), 'app/schema.sql')
    with open(sql_migration, 'r') as schema:
        db = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
        db.executescript(schema.read())
        db.close()

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()