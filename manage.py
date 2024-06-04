import logging

import settings
from gungnir import urls
from gungnir.utils.LogHandler import LogHandler
from gungnir.wsdl import Flask

if __name__ == "__main__":
    LogHandler(settings.settings.pop("logger")).basic_config(logging.getLogger())
    Flask(__name__).run(**settings.settings, errors=urls.errors, urls=urls.urls, url_prefix=urls.url_prefix)
