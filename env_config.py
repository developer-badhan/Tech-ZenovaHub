# Load environment variables and manage application secrets/settings

import environ

# Initialize environment variable handler with default values and types
env = environ.Env(
    DEBUG=(bool, False),                 # Default DEBUG to False
    ALLOWED_HOSTS=(list, []),           # Default ALLOWED_HOSTS to empty list
    SECRET_KEY=(str, ''),               # Django secret key for cryptographic signing

    # PostgreSQL database configuration
    PGSQL_NAME=(str, ''),               # Database name
    PGSQL_USER=(str, ''),               # Database user
    PGSQL_PASSWORD=(str, ''),           # Database password
    PGSQL_HOST=(str, ''),               # Database host
    PGSQL_PORT=(str, ''),               # Database port
)

# Read variables from a .env file located at the project root
env.read_env()
