from .base import *
import dj_database_url
from  decouple import config
 


DEBUG = False

SECRET_KEY = config('SECRET_KEY')

#production host
ALLOWED_HOSTS = ['xtentionblog.herokuapp.com']


AUTHENTICATION_BACKENDS += [
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    
]



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2vqdg4ootrp2d',
        'USER': 'wtfrbdlsuexefe',

        'PASSWORD': '6baae01ea2b014287bc6777c51108a01b27bddb80efbaf077a582e2b68b3ee92',
        'HOST': 'ec2-3-220-86-239.compute-1.amazonaws.com',
        'PORT': '5432',
    }
    
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Email Host 

EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)
LOGIN_REDIRECT_URL='post_list'
PASSWORD_RESET_TIMEOUT_DAY = config('PASSWORD_RESET_TIMEOUT_DAY', default=1, cast=int)
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
SOCIAL_AUTH_GITHUB_KEY = config('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = config('SOCIAL_AUTH_GITHUB_SECRET')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' #new




#DATABASES = {'default': dj_database_url.config(default='postgres://bszaqvyawctsvy:27d7bcd9d800a26cb5de6b9061768a44b6837310bb78619deabf26dbebc147ec@ec2-174-129-254-223.compute-1.amazonaws.com:5432/dfe2s7ni7l3jmq')}