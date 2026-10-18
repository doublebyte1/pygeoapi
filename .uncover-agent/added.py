from sqlalchemy.engine import make_url
    else:
        url = make_url(conn_str)
        if url.drivername == url.get_backend_name():
            url = url.set(drivername=driver_name)
        conn_str = url


def test_get_engine_use_provider_driver():
    engine = postgresql_provider_module.get_engine(
        'postgresql+psycopg2', 'host', '5432', 'db', 'user', 'password',
        'postgresql://user:password@host:5432/db'
    )
    assert engine.dialect.driver == 'psycopg2'