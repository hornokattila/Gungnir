import settings
import urls
import wsdl

if __name__ == "__main__":
    wsdl.Flask(__name__).run(url_prefix=urls.url_prefix, **settings.settings["wsdl"], urls=urls.urls)
