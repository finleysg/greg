import os
import structlog


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_DIR = os.path.join(BASE_DIR, 'var/log')
FLAT_LOG_FILE = '/nsc.log'
FLAT_LOG_PATH = LOG_DIR + FLAT_LOG_FILE

if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

if not os.path.exists(FLAT_LOG_PATH):
    f = open(FLAT_LOG_PATH, "a").close()
else:
    f = open(FLAT_LOG_PATH, "w").close()

SITE_ID = 1

INSTALLED_APPS = (
    "django.contrib.contenttypes",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.humanize",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    "corsheaders",
    "storages",
    "anymail",
    "content",
    "core",
    "documents",
    "messaging",
)

MIDDLEWARE = (
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.RemoteUserMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_structlog.middlewares.RequestMiddleware",
    "core.middleware.auth_token",
)

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates"), ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticatedOrReadOnly",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
    ),
    "EXCEPTION_HANDLER": "core.exception_handler.custom_exception_handler",
}

DJOSER = {
    "LOGIN_FIELD": "email",
    "DEFAULT_FROM_EMAIL": "postmaster@northernsummitconstruction.com",
    "SERIALIZERS": {
        "current_user": "core.serializers.UserDetailSerializer",
    },
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "plain_console": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.dev.ConsoleRenderer(),
        },
        "key_value": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.processors.KeyValueRenderer(key_order=['timestamp', 'level', 'event', 'logger']),
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "plain_console",
        },
        "flat_line_file": {
            "class": "logging.handlers.WatchedFileHandler",
            "filename": FLAT_LOG_PATH,
            "formatter": "key_value",
        },
    },
    "loggers": {
        "django_structlog": {
            "handlers": ["console", "flat_line_file"],
            "level": "ERROR",
        },
        "content": {
            "handlers": ["console", "flat_line_file"],
            "level": "ERROR",
        },
        "core": {
            "handlers": ["console", "flat_line_file"],
            "level": "ERROR",
        },
        "documents": {
            "handlers": ["console", "flat_line_file"],
            "level": "ERROR",
        },
        "messaging": {
            "handlers": ["console", "flat_line_file"],
            "level": "ERROR",
        },
        "projects": {
            "handlers": ["console", "flat_line_file"],
            "level": "ERROR",
        },
    }
}

structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.filter_by_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

# IMAGEKIT_DEFAULT_CACHEFILE_STRATEGY = "imagekit.cachefiles.strategies.Optimistic"

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

ROOT_URLCONF = "bizsite.urls"

WSGI_APPLICATION = "bizsite.wsgi.application"

LANGUAGE_CODE = "en-us"

TIME_ZONE = 'America/Chicago'

USE_I18N = False

USE_L10N = False

USE_TZ = True
