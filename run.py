import settings
from gungnir import urls
from gungnir import wsdl

if __name__ == "__main__":
    wsdl.Flask(__name__).run(url_config=settings.settings["config"], url_prefix=urls.url_prefix, url_system=settings.settings["system"], urls=urls.urls, **settings.settings["server"])
