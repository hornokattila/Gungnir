import settings
from gungnir import urls
from gungnir import wsdl

if __name__ == "__main__":
    wsdl.Flask(__name__).run(urls_config=settings.settings["config"], urls_prefix=urls.urls_prefix, urls_system=settings.settings["system"], urls=urls.urls, **settings.settings["server"])
