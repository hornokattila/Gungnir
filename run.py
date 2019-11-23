import settings
import urls
import wsdl

if __name__ == "__main__":
    wsdl.Flask(__name__).run(url_config=settings.settings["urls"], url_prefix=urls.url_prefix, urls=urls.urls, **settings.settings["wsdl"])
