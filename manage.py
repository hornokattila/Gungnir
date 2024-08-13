import settings
from gungnir import urls
from gungnir.wsdl import Flask

if __name__ == "__main__":
    Flask(__name__).run(**settings.settings, errors=urls.errors, urls=urls.urls, url_prefix=urls.url_prefix)
