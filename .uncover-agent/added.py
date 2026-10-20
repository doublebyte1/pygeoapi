        content = render_j2_template(api.tpl_config,
                                     api.config['server']['templates'],
        content = render_j2_template(api.tpl_config,
                                     api.config['server']['templates'],
                query = {"status": status}
                query = {}
            cursor = collection.find(query)
            if offset:
                cursor = cursor.skip(offset)
            if limit:
                cursor = cursor.limit(limit)
            jobs = list(cursor)
            if offset:
                results = results.offset(offset)
            if limit:
                results = results.limit(limit)

from typing import Optional, Any, Union
from sqlalchemy.engine import URL, Engine, make_url
    conn_str: Optional[Union[str, URL]] = None,
    else:
        # A caller-provided URL with a bare driver name (e.g. "postgresql://")
        # resolves to SQLAlchemy's default DBAPI for that backend (psycopg v3
        # for PostgreSQL), which may not be installed. Honour the provider's
        # driver_name when the URL does not already pin one.
        parsed = make_url(conn_str)
        if '+' not in parsed.drivername and '+' in driver_name:
            backend = driver_name.split('+', 1)[0]
            if parsed.drivername == backend:
                conn_str = parsed.set(
                    drivername=driver_name
                )