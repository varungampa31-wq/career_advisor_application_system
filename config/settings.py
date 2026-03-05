ALLOWED_HOSTS = [
    '98.80.216.180',
    'localhost',
    '127.0.0.1'
]

CSRF_TRUSTED_ORIGINS = [
    'http://98.80.216.180',
    'https://98.80.216.180'
]

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = 'role_redirect'
LOGOUT_REDIRECT_URL = '/accounts/login/'