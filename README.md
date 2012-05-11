# django-celery-mailer

Django email backend that utilizes Celery for background execution. This is a 
fork of django-celery-email, with additional inspiration from django-mailer.

## Installation

Install `django-celery-mailer` (available on PyPi):

	pip install django-celery-mailer

Requires a Django Celery stack.

## Usage

To enable `django-celery-mailer` for your project you need to add `celery_mailer` to
`INSTALLED_APPS`:

	INSTALLED_APPS += ('celery_mailer',)

You must then set it as your `EMAIL_BACKEND`:

	EMAIL_BACKEND = 'celery_mailer.backends.CeleryEmailBackend'

As long as you're using the Django builtin `SMTP` email backend, you're set! All
mail sent with Django's standard mechanisms will now be sent in the background 
with Celery.

## Customization

By default `django-celery-mailer` will use Django's builtin `SMTP` email backend
for the actual sending of the mail. If you'd like to use another backend, you
may set it in `CELERY_EMAIL_BACKEND` just like you would normally have set
`EMAIL_BACKEND` before you were using Celery. In fact, the normal installation
procedure will most likely be to get your email working using only Django, then
change `EMAIL_BACKEND` to `CELERY_EMAIL_BACKEND`, and then add the new
`EMAIL_BACKEND` setting from above.

## Acknowledgements

* Based upon Paul McLanahan's [django-celery-email](https://bitbucket.org/pmclanahan/django-celery-email).
