import logging

import settings
from gungnir import urls
from gungnir import wsdl
from gungnir.utils.LogHandler import Logger

if __name__ == "__main__":
    Logger(settings.settings.pop("logger")).basic_config(logging.getLogger())
    wsdl.Flask(__name__).run(**settings.settings, errors=urls.errors, urls=urls.urls, url_prefix=urls.url_prefix)
