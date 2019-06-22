import settings
import urls
import wsdl

if __name__ == "__main__":
    wsdl.Flask(__name__).run(urls=urls.urls, version=urls.version, **settings.settings["wsdl"])
