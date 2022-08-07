AUTHOR = 'Jeremy Guillette'
SITENAME = 'Larson Media Archive'
SITEURL = 'http://localhost:8000'
MEDIA_BASE = 'https://jagpublic.s3.amazonaws.com'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "./theme"

STATIC_PATHS = ['extra/robots.txt']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'}
}

ARTICLE_ORDER_BY = "title"
