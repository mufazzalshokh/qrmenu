from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
	'registration',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.humanize',
	'ckeditor',
	'ckeditor_uploader',
	'rest_framework',
	'corsheaders',
	# 'qrcode',
	'widget_tweaks',
	'restaurant',
]
MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'qrmenu.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR / 'templates']
		,
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

WSGI_APPLICATION = 'qrmenu.wsgi.application'

# DATABASES = {
# 	'default': {
# 		'ENGINE': 'django.db.backends.postgresql_psycopg2',
# 		'NAME': config('DB_NAME'),
# 		'USER': config('DB_USER'),
# 		'PASSWORD': config('DB_PASS'),
# 		'HOST': config('DB_HOST'),
# 		'PORT': config('DB_PORT'),
# 	}
# }

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
}
AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

LANGUAGE_CODE = 'en-uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_DIRS = BASE_DIR / 'assets',

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'
CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
	'default': {
		'toolbar': 'full',
		'height': 300,
		'width': 1080,

	}
}

REST_FRAMEWORK = {
	# Use Django's standard `django.contrib.auth` permissions,
	# or allow read-only access for unauthenticated users.
	'DEFAULT_PERMISSION_CLASSES': [
		'rest_framework.permissions.AllowAny'
	]
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ORIGIN_WHITELIST = (
	'http://192.168.43.89:8080/',
	"http://localhost:8080",
	"http://127.0.0.1:8000",
	'https://food-shop-uz.netlify.app/',
)

CORS_ALLOW_METHODS = (
	'DELETE',
	'GET',
	'OPTIONS',
	'PATCH',
	'POST',
	'PUT',
)
# CORS_ALLOW_ALL_ORIGINS
CORS_ALLOWED_ORIGINS = [
	'http://192.168.43.89:8080',
	"http://localhost:8080",
	"http://127.0.0.1:8000",
	'https://food-shop-uz.netlify.app',
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = [
	'accept',
	'accept-encoding',
	'authorization',
	'content-type',
	'dnt',
	'origin',
	'user-agent',
	'x-csrftoken',
	'x-requested-with',
]
ACCOUNT_ACTIVATION_DAYS = 21

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = config('EMAIL_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_PASS')

# '5055885408:AAHw9rqAwkHBwQUp3aR8p0Kb8HQn4XDsP4M'
try:
	from settings_local import *
except ImportError:
	pass
