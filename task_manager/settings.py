from pathlib import Path
SECRET_KEY = 'Bhaskarhazarika@123'

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',  # Admin app  # If you're using allauth for account management
    'tasks',
    'social_django',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': 'client_id', # i have removed this for security purposes
            'secret': 'secret',
            'key': ''
        }
    }
}

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
DEBUG = True
ROOT_URLCONF = 'task_manager.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# URL to use when referring to static files
STATIC_URL = '/static/'

# Directory to collect static files during deployment
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Directories where Django will search for additional static files
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",  # This should be the correct static directory for your project
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Ensure templates directory is correctly set
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
