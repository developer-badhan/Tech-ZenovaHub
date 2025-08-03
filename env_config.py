'''  Use for maintain secreates '''

import environ

env = environ.Env(
    DEBUG=(bool, False),

    ALLOWED_HOSTS=(list, []),

    SECRET_KEY=(str, ''),

    PGSQL_NAME=(str, ''),
    PGSQL_USER=(str, ''),
    PGSQL_PASSWORD=(str, ''),
    PGSQL_HOST=(str, ''),
    PGSQL_PORT=(str, ''),
)

env.read_env()

