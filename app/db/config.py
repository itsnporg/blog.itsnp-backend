
from contextvars import ContextVar

import peewee

DATABASE_NAME = "trial.db"
db_state_default = {"closed": None, "conn": None,
                    "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(peewee._ConnectionState):
    '''
    Just to make peewee async compatible
    https://fastapi.tiangolo.com/advanced/sql-databases-peewee/#make-peewee-async-compatible-peeweeconnectionstate
    '''

    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


db = peewee.SqliteDatabase(DATABASE_NAME, check_same_thread=False)

db._state = PeeweeConnectionState()

