# Load environment variables and manage application secrets/settings

import environ

# Initialize environment variable handler with default values and types
env = environ.Env(
    DEBUG=(bool, False),                
    ALLOWED_HOSTS=(list, []),          
    SECRET_KEY=(str, ''),               

    # PostgreSQL database configuration
    PGSQL_NAME=(str, ''),              
    PGSQL_USER=(str, ''),              
    PGSQL_PASSWORD=(str, ''),           
    PGSQL_HOST=(str, ''),              
    PGSQL_PORT=(str, ''),              

    # Session cookie settings
    SESSION_COOKIE_NAME=(str, ''), 
    SESSION_COOKIE_SECURE=(bool, ),
    SESSION_COOKIE_HTTPONLY=(bool,), 
    SESSION_COOKIE_SAMESITE=(str, ''),

    # Email settings
    EMAIL_BACKEND=(str, ''),
    EMAIL_HOST=(str, ''),
    EMAIL_PORT=(int, ),
    EMAIL_USE_TLS=(bool,),
    EMAIL_HOST_USER=(str, ''),
    EMAIL_HOST_PASSWORD=(str, ''),
    DEFAULT_FROM_EMAIL=(str, ''),
)

# Read variables from a .env file located at the project root
env.read_env()
