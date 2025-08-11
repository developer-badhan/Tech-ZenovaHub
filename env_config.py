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

    SESSION_COOKIE_NAME=(str, 'zenovahub_sessionid'), # Session cookie name
    SESSION_COOKIE_SECURE=(bool, True), # Whether to use HTTPS for the session cookie
    SESSION_COOKIE_HTTPONLY=(bool, True), # Whether to make the session cookie HTTP-only
    SESSION_COOKIE_SAMESITE=(str, 'Lax') # SameSite attribute for the session cookie
)

# Read variables from a .env file located at the project root
env.read_env()
