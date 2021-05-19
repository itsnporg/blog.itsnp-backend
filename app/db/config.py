import peewee

# pg_db = peewee.PostgresqlDatabase('itson', user='postgres', password='secret',
#                                   host='127.0.0.1', port=5432)

db = peewee.SqliteDatabase('./trial.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1024 * 64})
