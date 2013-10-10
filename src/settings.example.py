#! coding: utf-8
# pylint: disable-msg=W0311

# Make this unique, and don't share it with anybody.
SECRET_KEY = '<replace with a secret key>'

DEBUG = False


PRIMARY_DOMAIN = 'play.jupo.com'
EMAIL_REPLY_TO_DOMAIN = 'reply.jupo.com'


MONGOD_SERVERS = "127.0.0.1:27017"


ELASTICSEARCH_SERVER = '127.0.0.1:9200'


MEMCACHED_SERVERS = ['127.0.0.1:11211']


REDIS_SERVER = '127.0.0.1:6379'
REDIS_PUBSUB_SERVER = '127.0.0.1:6379'
REDIS_PINGPONG_SERVER = '127.0.0.1:6379'
REDIS_TASKQUEUE_SERVER = '127.0.0.1:6379'


SNOWFLAKE_SERVER = '127.0.0.1:2300'


HTTP_PROXY = None  
ITEMS_PER_PAGE = 5


# [Email Notifications]
SMTP_HOST = 'smtp.mandrillapp.com'
SMTP_PORT = 587
SMTP_USERNAME = ''
SMTP_PASSWORD = ''
SMTP_SENDER = 'Jupo Team <hello@jupo.com>'
SMTP_USE_TLS = False


# [Use Amazon's AWS S3 file-storage service to store static and uploaded files]
AWS_KEY = None
AWS_SECRET = None
S3_BUCKET_NAME = None


# [Login with Google]
# 1. Visit to Google Api Console https://code.google.com/apis/console/
# 2. under "API Access", choose "Create an OAuth 2.0 Client ID"
# 3. Edit the application settings, and list the Redirect URI(s) where you will run your application. For example: https://internalapp.yourcompany.com/oauth/google/authorized
# 4. Make a note of the Client ID, and Client Secret
GOOGLE_CLIENT_ID = None
GOOGLE_CLIENT_SECRET = None
GOOGLE_REDIRECT_URI = 'https://www.jupo.com/oauth/google/authorized'
GOOGLE_API_KEY = None


# [Login with Facebook]
# 1. Visit https://developers.facebook.com/apps and click the 'Create New App' button.
# 2. Fill in the App Display Name and leave the Namespace field blank.
# 3. Note the App ID and App Secret. 
FACEBOOK_APP_ID = None
FACEBOOK_APP_SECRET = None


# [Dropbox File Chooser]
DROPBOX_APP_KEY = None


# Customer.io
CUSTOMER_IO_SITE_ID = None
CUSTOMER_IO_API_KEY = None

# Mixpanel
MIXPANEL_TOKEN = None

SENTRY_DSN = None

# Avatar renderer, values : initials, robohash
AVATAR_RENDERER = 'initials'

# Zopim
ZOPIM_ENABLE = False