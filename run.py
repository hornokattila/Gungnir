import settings
from gungnir import urls
from gungnir import wsdl

if __name__ == "__main__":
    wsdl.Flask(__name__).run(urls_folder=settings.settings["folder"], urls_prefix=urls.urls_prefix, urls_system=settings.settings["system"], urls=urls.urls, **settings.settings["server"])
