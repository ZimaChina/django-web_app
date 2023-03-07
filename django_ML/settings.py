
#Things to add on settings.py so far


INSTALLED_APPS = [
    "crispy_bootstrap4",
    "crispy_forms",
    "users.apps.UsersConfig",
    "blog.apps.BlogConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]


STATIC_URL = "static/"

CRISPY_TEMPLATE_PACK = "bootstrap4"

LOGIN_REDIRECT_URL = 'blog-home'

LOGIN_URL = 'login'
